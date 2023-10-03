import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2

import glob


class Assignment1Client(object):
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
        self.stub = pb2_grpc.Assignment1Stub(self.channel)



# get the files from the computer
def send_files():
    string = ""
    for file in glob.glob("input/file*.txt"):
        print(file)
        with open(file, "r") as f:
            string += f.read()
            run_calculate(string)


def run_calculate(string):
    global liste
    global client
    # client = Assignment1Client()
    message = pb2.Message(message=string)
    responses = client.stub.Calculate(message)
    for response in responses:
        liste.append(response.message + ": " + str(response.num))

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
    # client = Assignment1Client()

    responses = client.stub.Combine(get_words_and_nums(liste))
    liste = []
    for response in responses:
        liste.append(response.message + ": " + str(response.num))

if __name__ == '__main__':
    client = Assignment1Client()
    liste = list()
    send_files()
    run_combine()
    print(liste)