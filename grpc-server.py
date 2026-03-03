
from concurrent import futures
import rpc_pb2_grpc
import grpc
import rpc_pb2

import logging
from PIL import Image
import io
import jsonpickle
import base64


# RouteGuideServicer provides an implementation of the methods of the RouteGuide service.
class RouteGuideServicer(rpc_pb2_grpc.RouteGuideServicer):

    def dotProduct(self, request, context):
        a = request.a
        b = request.b
        sum = 0
        for i in range(len(a)):
            sum = sum + (a[i] * b[i])
        return rpc_pb2.dotProductReply(dotproduct=sum)
    
    def add(self, request, context):
        return rpc_pb2.addReply(sum=request.a + request.b)

    def rawImage(self, request, context):
        ioBuffer = io.BytesIO(request.img)
        img = Image.open(ioBuffer)
        width = img.size[0]
        height = img.size[1]
        return rpc_pb2.imageReply(width=width, height=height)

    def jsonImage(self, request, context):
        image = request.img
        image = jsonpickle.decode(image)
        image = base64.b64decode(image)
        ioBuffer = io.BytesIO(image)
        img = Image.open(ioBuffer)
        width = img.size[0]
        height = img.size[1]
        return rpc_pb2.imageReply(width=width, height=height)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port("[::]:2222")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()