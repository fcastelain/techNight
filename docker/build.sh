# now we create the network of production
docker network create --subnet=172.19.0.0/16 prodNetwork

# add the mysql prod to the network
docker run --net prodNetwork --ip 172.19.0.2 -dti --name mysqlProdContainer fcastelain/mysql:latest
