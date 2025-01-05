from rest_framework import serializers

from tasks.models import Task, Tag


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    tags = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        task = Task.objects.create(**validated_data)

        if tags_data:
            tags_names = [name.strip() for name in tags_data.split(',')]
            for tag_name in tags_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                task.tags.add(tag)

        return task

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            tags_names = [name.strip() for name in tags_data.split(',')]
            instance.tags.clear()
            for tag_name in tags_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance


class ResponseTaskSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'tags']
