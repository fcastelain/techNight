# now we create the network of production
docker network create --subnet=172.19.0.0/16 prodNetwork

# add the mysql prod to the network
docker run --net prodNetwork --ip 172.19.0.2 -dti --name mysqlProdContainer iterator/mysql:latest
# add the python prod to the network
docker run --net prodNetwork --ip 172.19.0.3 -dti --name pythonProdContainer iterator/python:latest
# add the python prod to the network (to make some test)
#docker run --net prodNetwork -t iterator/newman:latest --collection="collection/iterator-test-nrg.postman_collection.json" --environment="environment/PRD.postman_environment.json" --html="newman-results.html"
