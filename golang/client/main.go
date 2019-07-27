package main

import (
	"context"
	"log"
	"time"

	api "demo/golang/api"

	"google.golang.org/grpc"
)

const (
	address     = "localhost:50051"
	defaultName = "world"
)

func main() {
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	log.Println("Client start request......")
	c := api.NewTodoServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.GetTodo(ctx, &api.TodoRequest{})
	if err != nil {
		log.Println("Failed to connecting the server....")
	}

	log.Println("===========Response=========")
	log.Printf("Id          : %d", r.Todos.Id)
	log.Printf("Title       : %s", r.Todos.Title)
	log.Printf("Description : %s", r.Todos.Description)
	log.Println("===========Response=========")
}
