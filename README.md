# Search Movie

## Overview

This project is a straightforward movie search API developed using the Django REST framework, designed to practice Docker Compose and Kubernetes concepts. Additionally, Docker Compose is utilized to integrate Kibana, Elasticsearch, and Redis into the project.

- `Kibana`: A data visualization and exploration tool used for log and time-series analytics, application monitoring, and operational intelligence. It is designed to work with Elasticsearch, providing a user-friendly interface for searching, viewing, and interacting with data stored in Elasticsearch indices.

- `Elasticsearch`: A highly scalable open-source search and analytics engine used for a variety of applications, including log and event data analysis, full-text search, and more. It stores and indexes data in near real-time, allowing for powerful and fast searches.

- `Redis`: An in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, and more, offering high performance and scalability for caching frequently accessed data.

Prerequisites
-------------
1. Kubernetes Cluster
2. kubectl
3. Docker and Docker Compose

How To Run
----------
1. **Clone the project**
2. **Set Up the Environment**
3. **Create project docker image**
    ```bash
    docker build . -t main_service
    ```
    `With docker-compose`
4. **Create docker network**
    ```bash
    docker network create musicnet 
    ```
5. **Start docker-compose.yml file**
    ```bash
    docker-compose up -d  
    ```
    `With h8s`
4. **Apply the Kubernetes manifest files to your cluster using kubectl**
    ```bash
    kubectl apply -f deployment/.
    ```
5. **Verify Deployment**
    ```bash
    kubectl get pods
    kubectl get services
    ```
    
   
