from django.core.cache import cache
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from tasks.models import Task
from tasks.serializers import CreateTaskSerializer, ResponseTaskSerializer


class ListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'list_count': self.page.paginator.count,
            'results': data
        })


class TaskViewSet(ViewSet):
    pagination_class = ListPagination
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def list(self, request):
        tasks = cache.get('tasks_list')
        if tasks is None:
            queryset = Task.objects.all()
            serializer = ResponseTaskSerializer(queryset, many=True)
            tasks = serializer.data
            cache.set('tasks_list', tasks, timeout=60 * 10)

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(tasks, request)
        if page is not None:
            return paginator.get_paginated_response(page)

        return Response(tasks)

    def create(self, request):
        serializer = CreateTaskSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            cache.delete('tasks_list')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, slug=None):
        queryset = Task.objects.filter(slug=slug, user=request.user).prefetch_related('tags').first()
        serializer = ResponseTaskSerializer(queryset)

        return Response(serializer.data)


