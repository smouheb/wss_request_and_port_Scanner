import websockets
import asyncio
import nmap3


class Connection:

    def __init__(self) -> None:
        self.port = None

    '''
        Method to find the ports whether filtered or open
    '''

    def find_port(self, ip_address: str):
        # nmap_instance = nmap3.Nmap()
        # result = nmap_instance.scan_top_ports(ip_address, args='-Pn')

        for i in range(0, 65535):
            try:
                self.port = str(i)
                asyncio.run(self.test_connection(self.port))
                print('This is the ' + str(i) + 'running')
            except Exception as e:
                print('This is not working for port ' +
                      str(i), str(e))

        # for k, v in result[ip_address].items():
        #     if k == 'ports':
        #         for n in range(len(v)):
        #             try:
        #                 self.port = v[n]['portid']
        #                 asyncio.run(self.test_connection(self.port))
        #                 print('This is the ' + str(self.port) + 'running')
        #             except Exception as e:
        #                 print('This is not working for port ' +
        #                       str(self.port), str(e))

    '''
        Connection method to ws
    '''
    async def connect(self):
        pass

    '''
        Method used to test the connection wih the port retrieved by "find_port()"
    '''
    async def test_connection(self, port):
        async with websockets.connect("ws://209.126.82.14:"+str(port)) as websocket:
            try:
                print('Seems to work', str(port))
                msg = await websocket.recv()
                print(msg)

            except Exception as e:
                print('Exception within the socket connection ')
