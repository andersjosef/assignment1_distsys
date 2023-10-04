import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2

import glob


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
    for file in glob.glob("input/file*.txt"):
        with open(file, "r") as f:
            string = f.read()
            run_calculate(string)


def run_calculate(string):
    global liste
    global client
    message = pb2.Message(message=string)
    responses = client.stub.Calculate(message)
    for response in responses.dict:
        liste.append(response + ": " + str(responses.dict[response]))

def get_words_and_nums(liste):
    for entry in liste:
        message = pb2.MessageResponse()
        entry = entry.split(": ")
        message.message = entry[0]
        message.num = int(entry[1])
        yield message




def run_combine():
    global liste
    global client

    responses = client.stub.Combine(get_words_and_nums(liste))
    liste = []
    for response in responses.dict:
        ordbok[response] = responses.dict[response]


if __name__ == '__main__':
    client = FrequencyCalculatorClient()
    liste = list()
    ordbok = dict()
    send_files()
    run_combine()
    ordbok = dict(sorted(ordbok.items(), key=lambda x:x[1], reverse=True))

    print("freq =", ordbok)