import grpc
from api import api_pb2
from api import api_pb2_grpc as apiRpc

def getTodo(stub):
    res = stub.GetTodo(api_pb2.TodoRequest())
    if not res:
        print("Failed to connecting the server....")
        return
    
    print("===========Response=========")
    print("Id           \t: %s" % res.todos.id)
    print("Title        \t: %s" % res.todos.title)
    print("Description  \t: %s" % res.todos.description)
    print("===========Response=========")


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        print("Client start request......")
        stub = apiRpc.TodoServiceStub(channel)
        try:
            getTodo(stub)
        except grpc.RpcError:
            print("Failed to connecting the server....")


if __name__ == '__main__':
    run()
    

