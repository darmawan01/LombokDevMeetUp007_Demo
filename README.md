# LombokDev MeetUp 007

[LombokDev MeetUp Issue](https://github.com/LombokDev/Talks-Proposal/issues/40)

## Talk
    Introduce Microservice using gRPC + ProtoBuff

## Slide
[Link To Slide](https://docs.google.com/presentation/d/1WdZNYq94qDnrH7S6TJwt7qvRm8QgeRsKAPbBkmc5wR8/edit?usp=sharing)

# Run in your local machine

## Code Structure
```
┣ api
┃ ┗ api.proto
┣ golang
┃ ┣ api
┃ ┃ ┗ api.pb.go
┃ ┣ client
┃ ┃ ┗ main.go
┃ ┗ main.go
┣ nodejs
┃ ┣ client.js
┃ ┣ package-lock.json
┃ ┗ package.json
┣ python
┃ ┣ api
┃ ┃ ┣ __init__.py
┃ ┃ ┣ api_pb2.py
┃ ┃ ┣ api_pb2_grpc.py
┃ ┗ client.py
┣ .gitignore
┣ Makefile
┣ README.md
┣ go.mod
┗ go.sum
```

## Require dependency
Make sure you have instaled go, python, and nodejs.

- Sycn go dependency with `go get`
- `pip install grpcio-tools` for python 
- `cd nodejs && npm i` to download nodejs node_modules

if all okey..

Use `make` command to run server and client request.

## `Make` Command

- `make go_generate` - converting `api/api.proto` to `go` syntax
- `make py_generate` - converting `api/api.proto` to `python` syntax
- `make go_server` - serve grpc server
- `make go_client` - start request to server
- `make py_client` - start request to server
- `make node_client` - start request to server