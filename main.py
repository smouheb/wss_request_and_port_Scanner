from data_processing import GenerateOuput
from connection_pool import Connection

con = Connection()
con.connect('8080')

# while True:
#     queue = Queue()
#     end_time = time.time() + 60
#     counter = 0
#     while time.time() < end_time:
#         payload = [random.randint(0, 100) for i in range(100)]
#         for i in payload:
#             queue.put(i)
#         time.sleep(0.1)
#     output = GenerateOuput(queue)
#     output.print_data(output.structure_data())
