# AI Code Generator (DevOps Internship Task)

This project is an AI-powered Python code assistant that takes natural language prompts and generates Python code and a meaningful title based on the prompt. It is designed to run with a simple Flask web interface, and the backend is powered by a local LLM model (CodeLlama via Ollama).

---

## 💡 Features

- Prompt input via web interface
- Generates a Python code snippet and a descriptive title
- Returns both title and code formatted and displayed in the UI
- Uses `ollama` (CodeLlama) via `subprocess` for local LLM integration
- Containerized with Docker
- Deployable on Minikube (Kubernetes)

---

## ⚙️ Technologies Used

- Python (Flask)
- HTML + CSS (UI)
- Ollama (LLM engine)
- Docker
- Minikube / Kubernetes

---

## 🚀 How to Run

### 🔹 1. Install Ollama and Run CodeLlama

```bash
ollama run codellama
```

Make sure `ollama` is installed and CodeLlama is downloaded.

### 🔹 2. Start Flask App (Local)

```bash
flask run
```

---

## 🐳 Docker Build & Run

```bash
docker build -t ai-codegen .
docker run -p 5000:5000 ai-codegen
```

---

## ☸️ Kubernetes Deployment with Minikube

1. Start Minikube:

```bash
minikube start
```

2. Apply deployment config:

```bash
kubectl apply -f deployment.yaml
```

3. Access app in browser:

```bash
minikube service ai-codegen-service
```

---

## 📌 Note on LLM Integration

The LLM model (Ollama) is **not included inside the Docker container**. The application uses `subprocess.run(["ollama", "run", ...])` to call the model.

In production, it is recommended to:
- Containerize Ollama separately as a backend API service
- Connect Flask to it via HTTP request
- Avoid relying on `subprocess` for model execution

---

## 📁 Project Structure

```
ai-codegen/
├── app.py
├── llm_client.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── Dockerfile
├── requirements.txt
├── deployment.yaml
└── README.md
```

---

## 👤 Author

**Name:** Abdulkerim Akten  
**DockerHub:** [akerimakten](https://hub.docker.com/u/akerimakten)  
**GitHub Repo:** [https://github.com/abdulkerimakten/ai-codegen](https://github.com/abdulkerimakten/ai-codegen)
