import websockets
import asyncio
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


class Connection:

    def __init__(self, nbre_of_threads=None) -> None:
        self.port = None
        self.NBRE_THREADS = nbre_of_threads
        self.NBRE_PORTS = 65535
        self.queue = Queue()

    '''
        Method to find the ports whether filtered or open
    '''
    async def test_connection(self, port):
        try:
            print(f'trying for ws://209.126.82.14:{port}')
            print('-----------------')
            connection = await websockets.connect('ws://209.126.82.14:'+str(port))
            print('Seems to work ', str(port))
            msg = await connection.recv()
            with open('./log.txt', 'r') as file:
                file.write(msg)
            print(msg)
            print('-----------------')

        except Exception as e:
            print('issuer with'+str(e))
    '''
        Method to run the test and keep track of the number of iteration (per nbre of ports)
    '''

    def run_con_test(self, port):
        asyncio.run(self. test_connection(port))

    '''
        Thread manager, executes the run_con_test for each port
    '''

    def start_threads(self):
        port_nbre = [i for i in range(self.NBRE_PORTS)]
        with ThreadPoolExecutor(self.NBRE_THREADS) as executor:
            results = executor.map(self.run_con_test, port_nbre)
        for result in results:
            print(result)

    '''
        Connection method to ws 
    '''
    async def connect(self):
        pass
