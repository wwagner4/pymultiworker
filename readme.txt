
# worker
docker run --net host -e HOST=localhost --name worker -d pymultiworker python -m worker

# core async
docker run --net host -e HOST=localhost --name corea -d pymultiworker python -m core_async

# core blocking
docker run --net host -e HOST=localhost --name coreb -d pymultiworker python -m core_blocking


---------------------------------------------------------------------------

docker swarm init
docker swarm leave -f

docker stack deploy -c stack.yml pymw
docker stack rm pymw

docker service logs pymw_core -f
docker service logs pymw_worker -f
