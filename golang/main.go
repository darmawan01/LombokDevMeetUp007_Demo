package main

import (
	"context"
	"log"
	"net"

	api "demo/golang/api"

	"google.golang.org/grpc"
)

const (
	port = ":50051"
)

type server struct {
}

func (s server) GetTodo(ctx context.Context, req *api.TodoRequest) (*api.TodoResponse, error) {
	payload := &api.Todo{
		Id:          1,
		Title:       "Hello",
		Description: "Hello Lombok Dev Audience....",
	}
	return &api.TodoResponse{Todos: payload}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	log.Println("Server started, waiting for client.....")
	serve := grpc.NewServer()
	api.RegisterTodoServiceServer(serve, &server{})
	if err := serve.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
