from flask import Flask
from myapp.tasks import add, app as celery_app

app = Flask(__name__)
app.debug = True

hyperlinks = '</br><a href="/">Overview</a> <a href="/start">Start task</a>'

@app.route('/')
def index():
    try:
        i = celery_app.control.inspect()
        return str(i.active()) + hyperlinks
    except Exception as e:
        return str(e)

@app.route('/start')
def start():
    add.delay(4, 4)
    return 'Hi there, I started the task!' + hyperlinks
