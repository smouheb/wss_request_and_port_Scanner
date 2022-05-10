import websocket
import nmap3
import json
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from websocket import create_connection


class Connection:

    def __init__(self, nbre_of_threads=None, ip_address="209.126.82.146") -> None:
        self.NBRE_THREADS = nbre_of_threads
        self.NBRE_PORTS = []
        self.IP_ADDRESS = ip_address
        self.queue = Queue()

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
        except Exception as e:
            print('Issue with : '+str(e))

    '''
        Looping through the ports retieved from check_port_status
        And checking whether we can connect to the WS server with it
    '''

    def run_connection_test(self):
        ports = self.check_port_status()
        print(ports)
        if len(ports) > 0:
            for p in ports:
                self.test_connection(p)

    '''
        Thread manager, executes the run_con_test for each port
    '''

    def start_threads(self):
        prt_nbre = self.chec_port_status()

        with ThreadPoolExecutor(self.NBRE_THREADS) as executor:
            results = executor.map(self.run_con_test, prt_nbre)
        for result in results:
            print(result)

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
                on_error=self.on_error
            )
            ws.run_forever()

        except Exception as e:
            print('Issue with: '+str(e))

    def on_message(self, ws, message):
        message = json.loads(message)
        for msg in message:
            print(message[msg])

    def on_error(self, ws):
        print(ws)

    def on_open(self, ws):
        print("opened")

    def on_close(self, ws):
        print("closed connection")
