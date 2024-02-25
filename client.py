import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2
import threading

import glob

# need to implement threading
# need to implement and repeated

class FrequencyCalculatorClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.FrequencyCalculatorStub(self.channel)



# get the files from the computer
def send_files():
    global liste
    thread_list = []
    for i, file in enumerate(glob.glob("input/file*.txt")):
        with open(file, "r") as f:
            string = f.read()
            thread_list.append(
                threading.Thread(target=run_calculate, name=i+1, args=(string,))
            )
            thread_list[-1].start()
    for th in thread_list:
        th.join()
    # print(thread_list)


def run_calculate(string):
    message = pb2.Message(message=string)
    responses = client.stub.Calculate(message)
    for response in responses.word:
        liste.append((response.message, response.num))
    

def run_combine():
    global liste
    being_sent = pb2.Liste()
    for obj in liste:
        being_sent.word.extend([
            pb2.MessageResponse(
                message=obj[0],
                num=obj[1])
        ])

    responses = client.stub.Combine(being_sent)
    liste = []
    for response in responses.word:
        liste.append(response.message + ": " + str(response.num))

if __name__ == '__main__':
    client = FrequencyCalculatorClient()
    liste = list()
    send_files()
    run_combine()
    print("freq =", liste)