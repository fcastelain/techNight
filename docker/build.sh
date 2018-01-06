# Build the images of the mysql
docker build ./mysql/ --tag iterator/mysql:latest

# Build the image of the python back
docker build ./python/ --tag iterator/python:latest
