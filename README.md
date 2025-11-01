<div align="center">

# 🍔 FOOD-DELIVERY_PREDICTION-JENKINS_CICD-PIPELINE  
*Accelerate Delivery, Predict Success, Power Innovation*

![last-commit](https://img.shields.io/github/last-commit/dhanush-raja-a/Food-delivery_prediction-jenkins_CICD-pipline?style=flat&logo=git&logoColor=white&color=0080ff)
![repo-top-language](https://img.shields.io/github/languages/top/dhanush-raja-a/Food-delivery_prediction-jenkins_CICD-pipline?style=flat&color=0080ff)
![repo-language-count](https://img.shields.io/github/languages/count/dhanush-raja-a/Food-delivery_prediction-jenkins_CICD-pipline?style=flat&color=0080ff)

### Built With:
![Markdown](https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939.svg?style=flat&logo=Jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white)

</div>

---

## 📘 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [CI/CD Workflow](#cicd-workflow)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview
This project predicts **food delivery times** based on real-world features like distance, weather, and traffic using a **Machine Learning model**.  
The ML model is deployed via **FastAPI**, and the entire CI/CD process is automated with **Jenkins** and **Docker**, hosted on an **AWS EC2 instance**.

**Objective:**  
Automate ML deployment → Build → Test → Deploy → Update on every commit 🚀

---

## 🏗️ Architecture

```mermaid
graph TD
A[GitHub Push] --> B[Jenkins Pipeline]
B --> C[Docker Build]
C --> D[FastAPI Container Deployment]
D --> E[EC2 / Cloud Hosting]
E --> F[User Access via API Endpoint]


---

## ⚙️ Docker & Jenkins CI/CD

### 🔁 Workflow Explained

**GitHub Webhook Trigger:**  
Whenever new code is pushed to the repository, GitHub automatically sends a POST request to Jenkins via a webhook. This trigger eliminates manual builds — making the pipeline fully automated.

**Jenkins Pipeline Execution:**  
Jenkins pulls the latest code from GitHub. It builds a Docker image using the Dockerfile present in the project. The image contains all dependencies (FastAPI, scikit-learn, Pandas, etc.). Jenkins then runs a container from that image.

**Docker Build Stage:**  
Docker packages the ML FastAPI app and model into an isolated container, ensuring consistent behavior across all environments.

Example:
docker build -t food_delivery_app .
docker run -d -p 5000:5000 food_delivery_app


docker build -t food_delivery_app .
docker run -d -p 5000:5000 food_delivery_app

sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
 Jenkins setup via Docker:
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

text

- Deploy FastAPI Container:
docker run -d -p 5000:5000 food_delivery_app

 Jenkins setup via Docker:
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

text

- Deploy FastAPI Container:
docker run -d -p 5000:5000 food_delivery_app


---

## 🧰 Linux Hands-on Experience

Throughout deployment, several Linux concepts were practiced:

- File permissions and ownership (`chmod`, `chown`)  
- Service management (`systemctl start/enable docker`)  
- Network configuration and port binding  
- Process monitoring (`ps`, `top`, `docker ps`)  
- Handling Jenkins logs and Docker logs  
- Secure SSH connection setup to EC2 using .pem key

This gave real-world DevOps + Cloud + Linux hands-on exposure.

---

## 🧱 Project Structure

── Dockerfile
├── requirements.txt
├── app/
│ ├── main.py
│ ├── model.joblib
│ ├── utils/
│ └── templates/
├── jenkinsfile
├── data/
│ └── dataset.csv
└── README.md


---

## 📊 Results

- Achieved automated deployment from GitHub → Jenkins → Docker → EC2.  
- Model provides real-time prediction APIs.  
- Demonstrated strong understanding of ML + DevOps integration.

---

## 🚀 Future Enhancements

- Integrate Grafana + Prometheus for container monitoring.  
- Add automated testing and SonarQube code quality checks.  
- Extend FastAPI endpoints for dataset retraining and analytics dashboard.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository  
2. Create your feature branch  
3. Commit your changes  
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

Developed by [Dhanush Raja A](https://github.com/dhanush-raja-a) 🚀

---

✅ **You can copy-paste this directly into your GitHub README.md.**  
It’s professional, descriptive, and shows **hands-on ML + CI/CD + DevOps** understanding — perfect for internships or showcasing on your profile.

<!-- Tags for GitHub repo -->
[//]: # (ci/cd docker jenkins ec2 fastapi machine-learning devops)
