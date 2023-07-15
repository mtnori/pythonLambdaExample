# Commands for docker build and push

```
docker build -t python-lambda-sample:latest .
docker tag python-lambda-sample:latest <account_id>.dkr.ecr.ap-northeast-1.amazonaws.com/python-lambda-sample:latest
docker push <account_id>.dkr.ecr.ap-northeast-1.amazonaws.com/python-lambda-sample:latest
```
