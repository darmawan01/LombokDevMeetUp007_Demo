# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from api import api_pb2 as api_dot_api__pb2


class TodoServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTodo = channel.unary_unary(
        '/api.TodoService/GetTodo',
        request_serializer=api_dot_api__pb2.TodoRequest.SerializeToString,
        response_deserializer=api_dot_api__pb2.TodoResponse.FromString,
        )


class TodoServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTodo': grpc.unary_unary_rpc_method_handler(
          servicer.GetTodo,
          request_deserializer=api_dot_api__pb2.TodoRequest.FromString,
          response_serializer=api_dot_api__pb2.TodoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.TodoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
