from concurrent import futures

import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


class Assignment1Service(pb2_grpc.Assignment1Servicer):

    def GetServerResponse(self, request_iterator, context):
        print("get server response")
        print("first one",request_iterator)
        message = request_iterator
        print(message)
        
        response = pb2.MessageResponse()
        split_words = message.message.strip().split()
        for word in split_words:
            response.message = word
            response.num = 1
        # print("response, serverside: ", response)
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_Assignment1Servicer_to_server(Assignment1Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("starting server...")
    serve()