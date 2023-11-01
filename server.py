from concurrent import futures

import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


class FrequencyCalculatorService(pb2_grpc.FrequencyCalculatorServicer):

    def Calculate(self, request, context):
        print("starting calculate...")
        message = request
        response = pb2.Liste()
        split_words = message.message.strip().split()

        # returns every word and number 1 from 
        for word in split_words:
            #checking for characters that are not letters , ? : etc.
            while word[-1].lower() not in "abcdefghijklmnopqrstuvwxyzæøå":
                word = word[0:-1]
            response.word.extend(
                [
                pb2.MessageResponse(message=word, num=1)
                ]
            )
        return response
    
    def Combine(self, request, context):
        print("starting combine...")
        ordbok = dict()
        for msg in request.word:
            if msg.message.strip() in ordbok:
                ordbok[msg.message] += msg.num
            else:
                ordbok[msg.message] = msg.num
        

        # sorting the dict/tuple list
        ordbok = sorted(ordbok.items(), key=lambda x:x[1])
        ordbok.reverse()
        ordbok = dict(ordbok)


        response = pb2.Liste()
        for key in ordbok:
            response.word.extend([
                pb2.MessageResponse(message=key, num=ordbok[key])
            ])
        
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_FrequencyCalculatorServicer_to_server(FrequencyCalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("starting server...")
    serve()