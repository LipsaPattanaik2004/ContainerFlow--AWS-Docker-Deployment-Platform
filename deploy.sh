#!/bin/bash

echo "Starting Deployment..."

# Stop existing container (if exists)
echo "Stopping old container..."
docker stop container-flow 2>/dev/null
docker rm container-flow 2>/dev/null

# Build new Docker image
echo "Building Docker image..."
docker build -t container-flow .

# Run new container
echo "Running container..."
docker run -d -p 80:5000 --name container-flow container-flow

# Check running containers
echo "Checking running containers..."
docker ps

echo "Deployment Completed Successfully!"
