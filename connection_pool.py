import websocket
import nmap3
import json
import time
from collections import deque
from websocket import create_connection
from data_processing import GenerateOuput


class Connection:

    def __init__(self, nbre_of_threads=None, ip_address="209.126.82.146") -> None:
        self.NBRE_THREADS = nbre_of_threads
        self.NBRE_PORTS = []
        self.IP_ADDRESS = ip_address
        self.timing = time.time() + 60
        self.queue = deque()

    def check_port_status(self):
        n = nmap3.NmapHostDiscovery()
        nres = n.nmap_portscan_only(self.IP_ADDRESS, args="-Pn")
        result_set = nres[self.IP_ADDRESS]['ports']

        for index in range(len(result_set)):
            port = result_set[index]['portid']
            status = result_set[index]['state']
            if status == 'open':
                self.NBRE_PORTS.append(port)

        return self.NBRE_PORTS

    '''
        Method to find the ports whether filtered or open
    '''

    def test_connection(self, port):
        try:
            ws_ser_addr = f'ws://209.126.82.146:{port}'
            connection = create_connection(ws_ser_addr)
            if str(connection.status) == '101':
                print(f'You can connect to this addr : {ws_ser_addr}')
                connection.close()
                return ws_ser_addr
            else:
                print(ws_ser_addr + ' Did not work')
        except Exception:
            pass

    '''
        Looping through the ports retieved from check_port_status
        And checking whether we can connect to the WS server with it
    '''

    def run_connection_test(self):
        ports = self.check_port_status()
        if len(ports) > 0:
            for p in ports:
                self.test_connection(p)

    '''
        Connection method to ws 
    '''

    def connect(self, port):
        try:
            address = f'ws://209.126.82.146:{port}'
            ws = websocket.WebSocketApp(
                address,
                on_open=self.on_open,
                on_message=self.on_message,
                on_close=self.on_close,
            )
            ws.run_forever()

        except Exception as e:
            print('Issue with: '+str(e))

    '''
        Process messages and dispatch for analysis
    '''

    def on_message(self, ws, message):
        try:
            messages = json.loads(message)
            for k, msg in messages.items():
                try:
                    if time.time() < self.timing:
                        if k == 'b':
                            self.queue.appendleft(msg)
                    else:
                        output = GenerateOuput(self.queue)
                        output.print_data(output.structure_data())
                        self.timing = time.time() + 60
                        self.queue = deque()
                        print('\n Next output in one minute \n')

                except Exception as e:
                    print(
                        'Issue thrown in the Inner block on on_message method: ', str(e))

        except Exception as e:
            print('Issue thrown in the Outer block on on_message method: ', str(e))

    def on_open(self, ws):
        print("\n Stream has been opened we're collecting the data now \n \n ")

    def on_close(self, ws):
        print("\n closed connection \n \n")
