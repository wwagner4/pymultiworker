
# worker
docker run --net host -e HOST=localhost --name worker -d pymultiworker python -m worker

# core async
docker run --net host -e HOST=localhost --name corea -d pymultiworker python -m core_async

# core blocking
docker run --net host -e HOST=localhost --name coreb -d pymultiworker python -m core_blocking
