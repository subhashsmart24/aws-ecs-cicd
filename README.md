\# End-to-End CI/CD Pipeline with Docker, Terraform \& AWS ECS



\## Project Overview



This project implements an automated CI/CD pipeline for deploying a containerized Flask application to AWS ECS Fargate.



\## Architecture



Developer → GitHub → GitHub Actions → Docker Build → Amazon ECR → Amazon ECS Fargate



\## Technologies Used



\- Python / Flask

\- Docker

\- Git \& GitHub

\- GitHub Actions

\- Terraform

\- AWS ECR

\- AWS ECS Fargate

\- AWS IAM

\- AWS VPC

\- AWS Security Groups



\## Workflow



1\. Developer pushes code to GitHub.

2\. GitHub Actions starts automatically.

3\. Docker image is built.

4\. Image is pushed to Amazon ECR.

5\. Current ECS task definition is retrieved.

6\. Task definition is updated with the new image.

7\. New ECS task definition is deployed.

8\. ECS service runs the updated application.



\## Infrastructure



Terraform provisions:



\- ECS Cluster

\- ECS Service

\- ECS Fargate Task Definition

\- IAM Execution Role

\- IAM Policy Attachment

\- Security Group

\- Default VPC/Subnets



\## Application Endpoints



\- `/` — Application status

\- `/health` — Health check



\## CI/CD



GitHub → Docker Build → ECR Push → ECS Task Definition Update → ECS Deployment



\## Security



\- AWS credentials are stored as GitHub repository secrets.

\- Terraform state files are excluded from Git.

\- Docker images are stored in Amazon ECR.

\- ECS tasks use an IAM execution role.



\## Cost Control



The ECS service is scaled to 0 when not being tested to avoid unnecessary Fargate runtime costs.



\## Repository



https://github.com/subhashsmart24/aws-ecs-cicd

