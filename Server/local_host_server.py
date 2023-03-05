from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_file():
    file = request.files['file']
    file.save('received_file.txt')
    return 'File received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
