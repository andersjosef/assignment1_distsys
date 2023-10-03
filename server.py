from concurrent import futures

import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


class Assignment1Service(pb2_grpc.Assignment1Servicer):

    def Calculate(self, request_iterator, context):
        message = request_iterator
        
        response = pb2.MessageResponse()
        split_words = message.message.strip().split()

        # returns every word and number 1 from 
        for word in split_words:
            #checking for characters that are not letters , ? : etc.
            while word[-1].lower() not in "abcdefghijklmnopqrstuvwxyzæøå":
                word = word[0:-1]
            response.message = word.strip()
            response.num = 1
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