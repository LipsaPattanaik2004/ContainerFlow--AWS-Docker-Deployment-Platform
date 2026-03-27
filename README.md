# Container-Flow- AWS Docker Deployment Platform 

A DevOps project demonstrating containerization and deployment of a Flask web application using Docker and AWS EC2, along with basic CI/CD integration.

---

## Features

* Containerized Flask web application using Docker
* Automated Docker image build & push using GitHub Actions (CI/CD)
* Deployment on AWS EC2
* Environment variable configuration
* Lightweight and scalable setup

---

## Tech Stack

* Python (Flask)
* Docker
* GitHub Actions (CI/CD)
* AWS EC2

---

## ⚙️ How It Works

1. Flask application is developed using Python
2. Application is containerized using Docker
3. GitHub Actions automatically builds and pushes Docker image to Docker Hub
4. AWS EC2 instance pulls and runs the container
5. Application is accessible via public IP

---

## Project Structure

```
Container-Flow---AWS-Docker-Deployment-Platform/
│── app.py
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── .dockerignore
│── nginx.conf
│── README.md
│── .github/
    └── workflows/
        └── docker-build.yml
```

---

## Run Locally

### Build Docker Image

```
docker build -t container-flow .
```

### Run Container

```
docker run -p 5000:5000 container-flow
```

Visit: http://localhost:5000

---

## CI/CD Pipeline (GitHub Actions)

* Triggered on push to main branch
* Builds Docker image
* Pushes image to Docker Hub automatically

---

## ☁️ AWS EC2 Deployment Steps

### 1. Launch EC2 Instance (Ubuntu)

### 2. Connect via SSH

```
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### 3. Install Docker

```
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
```

### 4. Pull Docker Image

```
docker pull <your-dockerhub-username>/container-flow
```

### 5. Run Container

```
docker run -d -p 80:5000 -e ENV=production <your-dockerhub-username>/container-flow
```

---

## API Endpoints

* `/` → Home route
* `/health` → Application health status
* `/logs` → Logging endpoint

---

## Key Learnings

* Containerization using Docker
* CI/CD automation using GitHub Actions
* Cloud deployment on AWS EC2
* Environment-based configuration
* Basic logging and monitoring concepts

---

## Use Case

This project demonstrates a real-world DevOps workflow where applications are containerized, automatically built, and deployed to cloud infrastructure with minimal manual intervention.

---

## Author

**Lipsa Pattanaik**
