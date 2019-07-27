const grpc = require('grpc')
const PROTO_PATH = '../api/api.proto'
const protoLoader = require('@grpc/proto-loader')
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

var proto = grpc.loadPackageDefinition(packageDefinition);
const client = new proto.api.TodoService('localhost:50051', grpc.credentials.createInsecure())

console.log("Client start request......");


client.GetTodo({}, (error, res) => {
    if (!error) {
        console.log('=================Response=================')
        console.log("Id          \t: "+ res.todos.id)
        console.log("Title       \t: "+ res.todos.title)
        console.log("Description \t: "+ res.todos.description)
        console.log('=================Response=================')
    } else {
        console.error("Failed to connecting the server....")
    }
})