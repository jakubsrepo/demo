from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Whatsssaappp'

if __name__ == '__main__':
    print("Whatsssaaapp")
    app.run(host='localhost', port=9874)
