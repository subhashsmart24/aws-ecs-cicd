FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG APP_VERSION=local
ARG BUILD_TIME=local

ENV APP_VERSION=$APP_VERSION
ENV BUILD_TIME=$BUILD_TIME
ENV AWS_REGION=ap-south-1
ENV DEPLOY_ENV="AWS ECS Fargate"

EXPOSE 5000

CMD ["python", "app.py"]