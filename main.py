import asyncio
from collections import deque
from data_processing import GenerateOuput
from connection_pool import Connection
from concurrent.futures import ThreadPoolExecutor, TimeoutError as ConTimeout
from threading import Thread, Lock
from queue import Queue
import time
import websockets

NBRE_THREADS = 200
NBRE_PORTS = 65535
queue = Queue()


async def test_connection(port):

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


def run_con_test():
    global queue
    while True:
        port = queue.get()
        asyncio.run(test_connection(port))
        queue.task_done()


def main():
    global queue
    for th in range(NBRE_THREADS):
        th = Thread(target=run_con_test)
        th.daemon = True
        th.start()

    for i in range(NBRE_PORTS):
        queue.put(i)
    queue.join()


if __name__ == '__main__':
    main()


# while True:
#     queue = deque()
#     end_time = time.time() + 60
#     counter = 0
#     while time.time() < end_time:
#         payload = [random.randint(0, 100) for i in range(100)]
#         for i in payload:
#             queue.append(i)
#         time.sleep(0.1)
#     output = GenerateOuput(queue)
#     output.print_data(output.structure_data())
