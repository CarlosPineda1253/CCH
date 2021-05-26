import socket
import ssl
import threading
import json


class RouterLoft:
    def __init__(self):
        self.PORT_SERVER = 27500
        self.PORT_CLIENT = 27501
        self.HOST, self.PORT, self.CERT, self.KEY = 'localhost', self.PORT_SERVER, 'cert.pem', 'key.pem'
        self.sock = socket.socket()
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(10)
        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(certfile=self.CERT, keyfile=self.KEY, password='')
        self.context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
        self.context.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')
        self.DEVICES = dict()
        self.DEVICES['Devices'] = dict()
        self.NUM_DEVICES = 0

    def loop(self):
        while True:
            ssock, addr = self.sock.accept()
            conn = self.context.wrap_socket(ssock, server_side=True)
            threading.Thread(self.on_new_client, (self, conn, addr))
        self.sock.close()

    def on_new_client(self, clientsock, addr):
        while True:
            try:
                msg = clientsock.recv()
                data = json.loads(msg)
                self.actions_client(self, data, addr)
            except ssl.SSLError as e:
                print(e)
            finally:
                if clientsock:
                    clientsock.close()
                    return

    def actions_client(self, data, addr):
        if data['IP'] == addr:
            if data['ACTION'] == 'Introduce':
                temp_dic = dict()
                temp_dic['IP'] = addr
                temp_dic['TYPE_DEVICE'] = data['TYPE_DEVICE']
                temp_dic['NAME_DEVICE'] = data['NAME_DEVICE']
                self.DEVICES['Devices'][self.NUM_DEVICES] = temp_dic
                self.NUM_DEVICES + 1
            elif data['ACTION'] == 'ON':
                for device in self.DEVICES.items():
                    if device['TYPE_DEVICE'] == 'Lights' | 'Climate' and device['NAME_DEVICE'] == data['NAME_DEVICE']:
                        temp_data = dict()
                        temp_data['HOST'] = device['IP']
                        temp_data['PORT_CLIENTS'] = self.PORT_CLIENT
                        temp_data['ACTION'] = 'ON'
                        self.sock_client(self, temp_data)

    @staticmethod
    def sock_client(data):
        sock = socket.socket(socket.AF_INET)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
        conn = context.wrap_socket(sock, server_hostname=data.HOST)
        conn.connect((data.HOST, data.PORT))
        temp_json = json.dumps(data)
        conn.send(str(temp_json))