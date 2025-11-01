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