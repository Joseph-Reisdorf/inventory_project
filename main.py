from flask import Flask

app = Flask(__name__)

@app.route('/')
def macy_page():
    return "I love macy"   

@app.route('/test/')
def index():
    return "test"

# comment

if __name__ == '__main__':
    app.run()