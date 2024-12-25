# Automated Continuous Integration and Deployment of Flask Application with CircleCI and Docker

This project is a dynamic Flask-based web application designed to display a dashboard with real-time status, charts, and tables. It uses CircleCI for Continuous Integration (CI) and Continuous Deployment (CD), Docker for containerization, and AWS EC2 for hosting.

![ScreenShot Tool -20241225062720](https://github.com/user-attachments/assets/87f30667-11ff-4519-b33e-cdc2382935e7)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [CI/CD Workflow](#cicd-workflow)
5. [AWS EC2 Deployment](#aws-ec2-deployment)
6. [Commands Used](#commands-used)

## Project Overview

This project involves building a dynamic Flask application with the following features:
- **Real-time Dashboard:** Displays live data such as processed data, active users, and error logs.
- **Data Chart:** A line chart showing data over different months.
- **Data Table:** Displays recent user activity with dynamic updates.
  
The web application is built using **Flask** and is containerized using **Docker**. We use **CircleCI** to automate testing, building, and deployment. After building the Docker image, the application is deployed to an **AWS EC2 instance**.

## Technologies Used
- **Flask:** Python-based web framework to create the application.
- **Docker:** Containerization tool to package the application and run it in isolated environments.
- **CircleCI:** Continuous Integration and Continuous Deployment (CI/CD) tool to automate the deployment pipeline.
- **AWS EC2:** Virtual machine used to host the application in the cloud.
- **Chart.js:** JavaScript library to display dynamic charts in the dashboard.

## Setup Instructions

### Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/r0han01/Dynamic-Interactive-Web-Experience.git
cd Dynamic-Interactive-Web-Experience
```
### Set up a Python Virtual Environment
-  Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
#### Install Dependencies
- Install the required Python packages:

```bash
pip install -r requirements.txt
```
### Docker Setup
- Build the Docker image for your application:

```bash
docker build -t your-image-name .
```
- Run the Docker container:

```bash
docker run -p 5000:5000 your-image-name
```
- The application should now be accessible at http://localhost:5000.

### Testing Locally
- You can test the application by visiting http://localhost:5000. The dashboard will display real-time data and chart information.

## CI/CD Workflow
#### CircleCI Configuration
- This project uses CircleCI for automating the CI/CD pipeline. The configuration file .circleci/config.yml is located in the repository and defines the workflow.

![ScreenShot Tool -20241225063306](https://github.com/user-attachments/assets/dcf86b08-cca3-4840-bc23-28772eb43220)

#### The CircleCI pipeline has the following steps:

- Build Docker Image: The Docker image is built and pushed to Docker Hub.
- Deploy to AWS EC2: Once the Docker image is pushed to Docker Hub, CircleCI triggers the deployment to an AWS EC2 instance using SSH.
#### Here is a breakdown of the CircleCI configuration:

#### 1. Check out the repository
- The workflow starts by checking out the repository to fetch the latest code:

```yaml
- name: Check out the repo
  uses: actions/checkout@v4
```
#### 2. Docker Login
- Logs into Docker Hub using credentials stored as CircleCI secrets:

```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@f4ef78c080cd8ba55a85445d5b36e214a81df20a
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```
#### 3. Build Docker Image
- The Docker image is built using the Dockerfile:

```yaml
- run:
    name: Build Docker Image
    command: |
      docker build -t docker.io/r0han01/circleci .
```
### 4. Push Docker Image
- Once built, the image is pushed to Docker Hub:

```yaml
- run:
    name: Push Docker Image
    command: |
      docker push docker.io/r0han01/circleci:latest
```
### 5. Deploy to AWS EC2
- The application is deployed to the EC2 instance using SSH. CircleCI connects to the remote EC2 instance, stops any running containers, and runs the updated container:

```yaml
- name: Execute SSH commands to deploy Docker container
  uses: appleboy/ssh-action@v1.2.0
  with:
    host: ${{ secrets.HOST }}
    username: ${{ secrets.USERNAME }}
    key: ${{ secrets.SSH_PRIVATE_KEY }}
    port: ${{ secrets.PORT }}
    script: |
      docker stop circleci || true
      docker rm circleci || true
      docker rmi docker.io/r0han01/circleci:latest || true
      docker run --name circleci -d -p 5000:5000 docker.io/r0han01/circleci:latest
```
### AWS EC2 Deployment
#### Setting up AWS EC2
- Launch an EC2 instance: Start an EC2 instance with an Ubuntu AMI.
- SSH into the EC2 instance: You need to SSH into the EC2 instance using the key pair you generated during instance creation:
```bash
ssh -i /path/to/your/key.pem ubuntu@your-ec2-ip
```
- Install Docker: Install Docker on the EC2 instance if not already installed:
```bash
sudo apt-get update
sudo apt-get install -y docker.io
```
### Run the Docker Container on EC2: Once the Docker image is pulled from Docker Hub, you can run it on the EC2 instance using the following command:
```bash
docker run -d -p 5000:5000 docker.io/r0han01/circleci:latest
```
- This will deploy the application on port 5000 of your EC2 instance, and it will be accessible via http://your-ec2-ip:5000.

### Commands Used
- Here is a list of key commands used in this project:

#### Docker Commands
- Build Docker Image:

```bash
docker build -t your-image-name .
```
- Run Docker Container:

```bash
docker run -p 5000:5000 your-image-name
```
- Stop Docker Container:

```bash
docker stop container_name
```
- Remove Docker Container:

```bash
docker rm container_name
```
- Push Docker Image to Docker Hub:

```bash
docker push your-docker-image:latest
```
![ScreenShot Tool -20241225063405](https://github.com/user-attachments/assets/3f01536d-96a2-45b6-8e9b-29cb781aad07)

### CircleCI Commands
- Trigger CircleCI Workflow via API:
```bash
curl -X POST https://api.github.com/repos/${GITHUB_REPOSITORY}/dispatches \
-H "Accept: application/vnd.github.v3+json" \
-H "Authorization: token $GITHUB_TOKEN" \
-d '{"event_type": "docker_push"}'
```
### Conclusion
-This project automates the process of building, testing, and deploying a Flask-based web application using Docker, CircleCI, and AWS EC2. The application is continuously integrated and deployed to AWS EC2 instances with every push to the repository, ensuring that the latest version is always running on the server. By using CircleCI and Docker, the workflow becomes streamlined, and deployment is quick and efficient. The dynamic dashboard can be accessed and used for real-time data monitoring.
### Useful Links 
- https://stackoverflow.com/questions/68147899/whats-is-the-difference-between-repository-dispatch-and-workflow-dispatch-in-git
- https://github.com/armstrong99/circleci-docker-CICD-pipeline-NodeJS/blob/main/.circleci/config.yml

# File Structure
```
/Dynamic-Interactive-Web-Experience
├── app.py                  # Main Flask app file
├── Dockerfile              # Dockerfile for containerization
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
├── venv/                   # Python virtual environment (if used)
└── .github/                # GitHub Actions CI/CD workflow
    └── workflows/          # Workflow definition for GitHub Actions
        └── main.yml        # CI/CD pipeline configuration
```

