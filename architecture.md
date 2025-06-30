# Instant Dev Environment Generator – Architecture

## Core Concept
Spin up a containerized dev environment (Docker) from a GitHub repo or user prompt.

## Components

- 🧠 **API Server (FastAPI)**: Accepts prompt or repo URL → triggers container build
- 🐳 **Docker Interface**: Uses Docker SDK to spin up containers with `.devcontainer.json`
- 🌐 **Frontend (React)**: Form input, log viewer, job status
- 🔁 **Async Task Queue**: Handles long-running container jobs (Celery or asyncio)
- 📡 **WebSockets**: Stream logs live to frontend
- 🔐 **Sandboxing/Security**: Limit memory, runtime, filesystem access