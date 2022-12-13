# mle
Machine Learning Engineering with a focus on deployment of ML models in production.

**Random Forest Classifier Docker Deployment**

- [train.py](./iris-rfc/train.py): classifier training script
- [inference.py](./iris-rfc/webapp/inference.py): model inference
- [api_call.py](./iris-rfc/api_call.py): API endpoint call

Docker commands:

```
docker build -t iris-rfc .
docker run -p 5000:5000 iris-rfc
```

The docker image is available on docker hub: 
https://hub.docker.com/repository/docker/vsmolyakov/iris-rfc
