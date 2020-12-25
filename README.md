# Kubernetes Celery

This project is used to generate Docker images for my Kubernetes playground:

https://github.com/JorisHartog/k8s-playground


## Development

To run this app locally, make sure you have a RabbitMQ instance ready:

```bash
vagrant up
```

Install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```

Start a Celery worker:

```bash
source venv/bin/activate
celery -A myapp.tasks worker --loglevel=INFO
```

Finally, start the Flask app:

```bash
source venv/bin/activate
./run_myapp.py
```
