# Python AWS Lambda with Docker image example

## On AWS

```
docker build -t python-lambda-sample:latest .
docker tag python-lambda-sample:latest <account_id>.dkr.ecr.ap-northeast-1.amazonaws.com/python-lambda-sample:latest
docker push <account_id>.dkr.ecr.<region_name>.amazonaws.com/python-lambda-sample:latest
```

# On Local

```
docker build -t python-lambda-sample:latest .
docker-compose -f minio/docker-compose.yml up -d
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
