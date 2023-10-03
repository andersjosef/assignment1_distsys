from __future__ import print_function

import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


def make_message(message):
    return pb2.Message(
        message=message
    )


def generate_messages():
    messages = [
        make_message("First message"),
        make_message("Second message"),
        make_message("Third message"),
        make_message("Fourth message"),
        make_message("Fifth message"),
    ]
    for msg in messages:
        print("Hello Server Sending you the %s" % msg.message)
        yield msg


def send_message(stub):
    global liste
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        liste.append((response.message, response.num))
        print("Hello from the server received your %s" % response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.Assignment1Stub(channel)
        # send_message(stub)
        result = get_url(message="hello there")


def get_url(message):
    """
    Client function to call the rpc for GetServerResponse
    """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.Assignment1Stub(channel)
        message = pb2.Message(message=message)

        return stub.GetServerResponse(message)



if __name__ == '__main__':
    liste = list()
    run()
    print(liste)