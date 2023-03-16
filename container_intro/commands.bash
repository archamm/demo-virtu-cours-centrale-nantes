docker build -t container-info .

docker run --rm --name container1 -e CONTAINER_ID=CONTAINER_1 container-info
docker run --rm --name container2 -e CONTAINER_ID=CONTAINER_2 container-info
