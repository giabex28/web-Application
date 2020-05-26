from app import app
from flask import Flask
import time
import redis

#app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

def get_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route("/")
def index():
    count = get_count()
    return "Hello World.\n Access number: " + count


#if __name__ == "__main__":
#    app.run()
