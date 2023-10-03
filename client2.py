import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


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
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        responses = self.stub.GetServerResponse(message)
        print(responses)
        for response in responses:
            yield response


if __name__ == '__main__':
    liste = list()
    client = Assignment1Client()
    result = client.get_url(message="Hello Server you there?")
    print(result)
    for t in result:
        print(t)
    # for response in result:
    #     liste.append((response.message, response.num))
    #     print("Hello from the server received your %s" % response.message)
