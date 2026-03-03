
import rpc_pb2_grpc
import rpc_pb2
import grpc
import jsonpickle
import base64
import time
import random
import sys

def create100Vector():
    vector = []
    for i in range(100):
        vector.append(random.random())
    return vector

def doRawImage(addr, debug=True):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    data = rpc_pb2.rawImageMsg(img=img)
    feature = stub.rawImage(data)
    if debug:
        print(feature)

def doAdd(addr, debug=False, a=5, b=10):
    feature = stub.add(rpc_pb2.addMsg(a=a,b=b))
    if debug:
        print(feature)

def doDotProduct(addr, debug=False):
    a = create100Vector()
    b = create100Vector()
    feature = stub.dotProduct(rpc_pb2.dotProductMsg(a=a, b=b))
    if debug:
        print(feature)

def doJsonImage(addr, debug=False):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    img = base64.b64encode(img)
    img = jsonpickle.encode(img)
    feature = stub.jsonImage(rpc_pb2.jsonImageMsg(img=img))
    if debug:
        print(feature)

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

addr = f"{host}:2222"
channel = grpc.insecure_channel(f"{host}:2222")
stub = rpc_pb2_grpc.RouteGuideStub(channel)
print(f"Running {reps} reps against {addr}")

if cmd == 'rawImage':
    start = time.perf_counter()
    for x in range(reps):
        doRawImage(addr, debug=True)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'add':
    start = time.perf_counter()
    for x in range(reps):
        doAdd(addr, debug=True)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'jsonImage':
    start = time.perf_counter()
    for x in range(reps):
        doJsonImage(addr, debug=True)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'dotProduct':
    start = time.perf_counter()
    for x in range(reps):
        doDotProduct(addr, debug=True)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
else:
    print("Unknown option", cmd)
