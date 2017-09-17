import flask
import psycopg2cffi

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flask!'

if '__main__' == __name__:
    app.run()

