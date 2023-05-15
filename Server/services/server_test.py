# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('received_file.txt')

#     with open('log.log', 'a') as f:
#         f.write(request.method + ' ' + request.path + '\n')

#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()






# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('received_file.txt')

#     with open('log.txt', 'a') as f:
#         f.write(request.method + ' ' + request.path + '\n')

#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()
