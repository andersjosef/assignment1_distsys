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

    def get_url(self, message):
        """
        Client function to call the rpc for Calculate
        """
        message = pb2.Message(message=message)
        responses = self.stub.Calculate(message)
        for response in responses:
            yield response

def make_dictionary():
    pass

# get the files from the computer
def send_files():
    string = ""
    for file in glob.glob("input/file*.txt"):
        with open(file, "r") as f:
            string += f.read()
            run(string)


def run(string):
    global liste
    client = Assignment1Client()
    result = client.get_url(message=string)
    for t in result:
        liste.append(t.message + ": " + str(t.num))
if __name__ == '__main__':
    liste = list()
    send_files()
    print(liste)