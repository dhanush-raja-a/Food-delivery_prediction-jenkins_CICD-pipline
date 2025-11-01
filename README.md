Perfect 💪 — you already have a very solid base.
Here’s your complete README (single copy-paste version) — with everything neatly integrated: Docker, Jenkins, EC2, ML explanation, Webhook automation, and Linux/DevOps hands-on parts — all merged into your current format.

⸻


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
- [Docker & Jenkins CI/CD](#docker--jenkins-cicd)
- [EC2 Deployment & Cloud Setup](#ec2-deployment--cloud-setup)
- [Linux Hands-on Experience](#linux-hands-on-experience)
- [Project Structure](#project-structure)
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
A[GitHub Push] --> B[Jenkins Pipeline Triggered via Webhook]
B --> C[Docker Build & Image Creation]
C --> D[FastAPI ML App Container Deployment]
D --> E[AWS EC2 Instance]
E --> F[User Access API Endpoint]
F --> G[Continuous Monitoring & Updates]


⸻

⚙️ Docker & Jenkins CI/CD

🔁 Workflow Explained
	1.	GitHub Webhook Trigger:
	•	Whenever new code is pushed to the repository, GitHub automatically sends a POST request to Jenkins via a webhook.
	•	This trigger eliminates manual builds — making the pipeline fully automated.
	2.	Jenkins Pipeline Execution:
	•	Jenkins pulls the latest code from GitHub.
	•	It builds a Docker image using the Dockerfile present in the project.
	•	The image contains all dependencies (FastAPI, scikit-learn, Pandas, etc.).
	•	Jenkins then runs a container from that image.
	3.	Docker Build Stage:
	•	Docker packages the ML FastAPI app and model into an isolated container.
	•	Ensures consistent behavior across all environments.
	•	Example:

docker build -t food_delivery_app .
docker run -d -p 5000:5000 food_delivery_app


	4.	Automated Deployment:
	•	Jenkins uses Post-Build Actions or a scripted pipeline to deploy the container.
	•	It ensures every new commit is tested, built, and deployed automatically — forming a true CI/CD pipeline.
	5.	Why CI/CD with Jenkins + Docker?
	•	Reduces manual intervention.
	•	Detects code issues early through automation.
	•	Seamless delivery from development → deployment.

⸻

☁️ EC2 Deployment & Cloud Setup

🧩 Steps to Set Up
	1.	Launch EC2 Instance (Ubuntu):
	•	Choose t2.micro (Free Tier)
	•	Enable Auto-assign Public IP
	•	Add inbound rules for ports 22, 8080, 5000.
	2.	Create and Configure VPC:
	•	Define IPv4 CIDR (e.g., 172.31.0.0/16)
	•	Create subnets and enable public access.
	•	Attach Internet Gateway and Route Table to allow external traffic.
	3.	Security Group:
	•	Allows access to:
	•	22 → SSH
	•	8080 → Jenkins
	•	5000 → FastAPI app
	4.	Install Required Tools:

sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

# Jenkins setup via Docker
docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts


	5.	Deploy FastAPI Container:

docker run -d -p 5000:5000 food_delivery_app


	6.	Access:
	•	Jenkins UI → http://<EC2_Public_IP>:8080
	•	FastAPI App → http://<EC2_Public_IP>:5000/docs

⸻

🧮 Machine Learning Model Overview

The ML model predicts estimated delivery time using:
	•	Distance between restaurant and customer
	•	Weather conditions
	•	Traffic density
	•	Order volume and time of day

ML Workflow:
	1.	Data preprocessing with Pandas & NumPy
	2.	Model training with Scikit-learn (Linear Regression / RandomForest)
	3.	Model serialized via Joblib
	4.	Integrated with FastAPI for live predictions

@app.post("/predict")
def predict_delivery_time(data: DeliveryInput):
    features = np.array([[data.distance, data.weather, data.traffic]])
    prediction = model.predict(features)
    return {"estimated_time": prediction[0]}


⸻

🧰 Linux Hands-on Experience

Throughout deployment, several Linux concepts were practiced:
	•	File permissions and ownership (chmod, chown)
	•	Service management (systemctl start/enable docker)
	•	Network configuration and port binding
	•	Process monitoring (ps, top, docker ps)
	•	Handling Jenkins logs and Docker logs
	•	Secure SSH connection setup to EC2 using .pem key

This gave real-world DevOps + Cloud + Linux hands-on exposure.

⸻

🧱 Project Structure

├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   ├── model.joblib
│   ├── utils/
│   └── templates/
├── jenkinsfile
├── data/
│   └── dataset.csv
└── README.md


⸻

📊 Results
	•	Achieved automated deployment from GitHub → Jenkins → Docker → EC2.
	•	Model provides real-time prediction APIs.
	•	Demonstrated strong understanding of ML + DevOps integration.

⸻

🚀 Future Enhancements
	•	Integrate Grafana + Prometheus for container monitoring.
	•	Add automated testing and SonarQube code quality checks.
	•	Extend FastAPI endpoints for dataset retraining and analytics dashboard.

⸻

🤝 Contributing

Contributions are welcome!
	1.	Fork this repository
	2.	Create your feature branch
	3.	Commit your changes
	4.	Push and open a Pull Request

⸻

📜 License

This project is licensed under the MIT License￼.

⸻

Developed by Dhanush Raja A￼ 🚀

---

✅ **You can copy-paste this directly into your GitHub README.md.**  
It’s professional, descriptive, and shows **hands-on ML + CI/CD + DevOps** understanding — perfect for internships or showcasing on your profile.
