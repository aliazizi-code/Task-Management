FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /src

COPY requirements.txt ./
COPY ./scripts /scripts
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod -R +x /scripts
ENV PATH="/scripts:/py/bin:$PATH"

COPY . .

CMD ["/scripts/run.sh"]
