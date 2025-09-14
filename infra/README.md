# Deployment Instructions for Split Expenses Application

This document provides instructions for deploying the Split Expenses application using Docker and Kubernetes.

## Prerequisites

- Docker installed on your machine
- Kubernetes cluster (e.g., Minikube, GKE, EKS, AKS)
- kubectl command-line tool installed and configured
- Docker Compose (optional, for local development)

## Directory Structure

The deployment files are organized as follows:

```
deploy/
├── docker/
│   ├── backend.Dockerfile
│   ├── frontend.Dockerfile
│   └── nginx.Dockerfile
├── nginx/
│   └── nginx.conf
└── kubernetes/
    ├── backend-deployment.yaml
    ├── frontend-deployment.yaml
    ├── postgres-deployment.yaml
    └── nginx-deployment.yaml
```

## Docker Deployment

1. **Build Docker Images**

   Navigate to the `deploy/docker` directory and build the Docker images for the backend, frontend, and Nginx:

   ```bash
   docker build -t split-expenses-backend -f backend.Dockerfile .
   docker build -t split-expenses-frontend -f frontend.Dockerfile .
   docker build -t split-expenses-nginx -f nginx.Dockerfile .
   ```

2. **Run Docker Containers**

   You can run the containers using Docker Compose or manually. If using Docker Compose, create a `docker-compose.yml` file in the `deploy` directory and define the services.

## Kubernetes Deployment

1. **Deploy PostgreSQL**

   Apply the PostgreSQL deployment configuration:

   ```bash
   kubectl apply -f kubernetes/postgres-deployment.yaml
   ```

2. **Deploy Backend Service**

   Apply the backend deployment configuration:

   ```bash
   kubectl apply -f kubernetes/backend-deployment.yaml
   ```

3. **Deploy Frontend Application**

   Apply the frontend deployment configuration:

   ```bash
   kubectl apply -f kubernetes/frontend-deployment.yaml
   ```

4. **Deploy Nginx**

   Apply the Nginx deployment configuration:

   ```bash
   kubectl apply -f kubernetes/nginx-deployment.yaml
   ```

## Accessing the Application

Once all services are deployed, you can access the application through the Nginx service. If you're using a local Kubernetes cluster, you may need to set up port forwarding or use a LoadBalancer service type.

## Observability and Monitoring

Consider integrating observability tools such as Prometheus and Grafana for monitoring the application performance and health.

## Scaling

You can scale the deployments using the following command:

```bash
kubectl scale deployment <deployment-name> --replicas=<number>
```

Replace `<deployment-name>` with the name of the deployment (e.g., `split-expenses-backend`) and `<number>` with the desired number of replicas.

## Conclusion

This document outlines the steps to deploy the Split Expenses application using Docker and Kubernetes. For further customization and optimization, refer to the respective service documentation.