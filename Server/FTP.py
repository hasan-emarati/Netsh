import logging
import argparse

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def start_ftp_server(host, port, username, password, directory):
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, directory, perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizer
    address = (host, port)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start an FTP server.')
    parser.add_argument('--host', type=str, default='0.0.0.0',
                        help='The IP address to bind to.')
    parser.add_argument('--port', type=int, default=21,
                        help='The port number to bind to.')
    parser.add_argument('--username', type=str, default='windowsftp',
                        help='The username to use for authentication.')
    parser.add_argument('--password', type=str, default='winftpass',
                        help='The password to use for authentication.')
    parser.add_argument('--directory', type=str, default='/',
                        help='The directory to serve files from.')
    args = parser.parse_args()

    logging.basicConfig(filename='Log.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug('Debugging mode enabled')
    logging.info('FTP server started on %s:%s', args.host, args.port)
    logging.warning('Permitting foreign addresses')
    logging.error('Non-ASCII characters like Øresund and Malmö are allowed')

    with open('Log.log', 'a') as log_file:
        start_ftp_server(args.host, args.port, args.username, args.password, args.directory)


