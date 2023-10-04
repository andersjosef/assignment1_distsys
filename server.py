from concurrent import futures

import grpc
import assignment1_pb2_grpc as pb2_grpc
import assignment1_pb2 as pb2


class FrequencyCalculatorService(pb2_grpc.FrequencyCalculatorServicer):

    def Calculate(self, request, context):
        print("starting calculate...")

        message = request
        
        split_words = message.message.strip().split()

        tmp_dict = dict()
        # returns every word and number 1 from 
        for word in split_words:
            word = word.strip()
            #checking for characters that are not letters , ? : etc.
            while word[-1].lower() not in "abcdefghijklmnopqrstuvwxyzæøå":
                word = word[0:-1]
            if word in tmp_dict:
                tmp_dict[word] += 1
            else:
                tmp_dict[word] = 1

        response = pb2.Map(dict=tmp_dict)
        return response
    
    def Combine(self, request_iterator, context):
        print("starting combine...")
        ordbok = dict()
        for msg in request_iterator:
            if msg.message.strip() in ordbok:
                ordbok[msg.message] += msg.num
            else:
                ordbok[msg.message] = msg.num
        
        response = pb2.MessageResponse()
        
        # returns every word and number 1 from 
        response = pb2.Map(dict=ordbok)
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