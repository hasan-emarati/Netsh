from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def log_requests():
    with open('requests.txt', 'a') as f:
        f.write(str(request.headers) + '\n' + request.data.decode('utf-8') + '\n\n')
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def receive_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('received_file.txt')
#         return 'File received successfully!'
#     return 'Hello from Flask server!'

# if __name__ == '__main__':
#     app.run()
