# now we create the network of production
docker network create --subnet=172.19.0.0/16 prodNetwork

# add the mysql prod to the network
docker run --net prodNetwork --ip 172.19.0.2 -p 3306:3306 -dti --name mysqlProdContainer iterator/mysql:latest
# add the python prod to the network
docker run --net prodNetwork --ip 172.19.0.3 -p 8081:8081 -dti --name pythonProdContainer iterator/python:latest
