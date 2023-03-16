from flask import Flask, request
import store
import time
app = Flask(__name__)

VERSION = [1, 0, 0] # semver

@app.route("/")
def index():
    return {
        "product": {
            "name": "Sprout",
            "dev": "Callie Fox Games",
            "version": VERSION
        },
        "time": time.time(),
        "live-features": [
            "lb"
        ]
    }

@app.route('/heart')
def heartbeat():
    return "ok"

@app.route('/lb/add')
def lb_add():
    obj = {
        "player": request.args.get("p", "Anon"),
        "level": request.args.get("l", "Lobby"),
        "game": request.args.get("g", "Sprout"),
        "score": request.args.get("s", 0)
    }
    store.add("lb", obj)
    return obj

@app.route('/lb/get')
def lb_get():
    arr = store.get("lb")
    ret = []

    for val in arr:
        if val["game"] == request.args.get("g", "Sprout"):
            ret.append(val)

    return {
        "lb": ret
    }

if __name__ == '__main__':
    app.run(debug=True)
