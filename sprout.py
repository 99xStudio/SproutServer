from flask import Flask
app = Flask(__name__)

@app.route('/heart')
def heartbeat():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)