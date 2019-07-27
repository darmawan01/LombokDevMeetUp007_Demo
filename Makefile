go_generate:
	protoc -I. --go_out=plugins=grpc:golang api/api.proto

py_generate:
	python -m grpc_tools.protoc -I. --python_out=python --grpc_python_out=python api/api.proto

go_serve:
	go run golang/main.go

go_client:
	go run golang/client/main.go

py_client:
	python python/client.py

node_client:
	cd nodejs && npm start