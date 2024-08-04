# mle
Machine Learning Engineering (MLE) with a focus on deployment of ML models in production.

**FLAN-T5 Small Text Generation with FastAPI**

- [app.py](./flan-t5/app.py): model inference

To call the inference API, use the following command:

```
curl -X 'GET' \
  'http://localhost:8080/generate?text=what%20is%20the%20meaning%20of%20life%3F' \
  -H 'accept: application/json'
```

The docker image is available on docker hub: 
https://hub.docker.com/repository/docker/vsmolyakov/flan-t5-small-text-gen-fastapi


**RoBERTa sentiment classification**

- [inference.py](./roberta/webapp/inference.py): model inference

To call the inference API, use the following command:

```
curl -X POST -H "Content-Type: application/JSON" --data '["Deploying ML models is fun!"]' http://0.0.0.0:5000/predict
```

The docker image is available on docker hub: 
https://hub.docker.com/repository/docker/vsmolyakov/roberta-sentiment


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

