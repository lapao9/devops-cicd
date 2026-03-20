# ⚙️ DevOps CI/CD Pipeline

![CI](https://github.com/lapao9/devops-cicd/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/lapao9/devops-cicd/actions/workflows/cd.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-GHCR-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)

> **Parte 2/5 do DevOps Portfolio** · Pipeline CI/CD completo com GitHub Actions — testes automáticos e publicação de imagem Docker em cada push.

## 🔄 Como funciona o Pipeline
```
git push origin main
        │
        ▼
┌─────────────────────────────────┐
│  CI — Tests (ci.yml)            │
│  ├── Instala Python 3.12        │
│  ├── Inicia PostgreSQL          │
│  ├── Instala dependências       │
│  └── Corre pytest (6 testes)   │
└─────────────┬───────────────────┘
              │ ✅ testes passam
              ▼
┌─────────────────────────────────┐
│  CD — Docker (cd.yml)           │
│  ├── Build da imagem            │
│  ├── Tag: latest + sha-abc123   │
│  └── Push para GHCR             │
└─────────────────────────────────┘
```

## 🚀 Início Rápido
```bash
git clone https://github.com/lapao9/devops-cicd.git
cd devops-cicd
cp .env.example .env
make up
```

## 🧪 Testes
```bash
make test
```

## 📦 Imagem Docker
```bash
docker pull ghcr.io/lapao9/devops-cicd:latest
```

## 📚 Projeto Anterior
**[← Projeto 01: Foundations](https://github.com/lapao9/devops-foundations)**

## 📚 Próximo Passo
**[→ Projeto 03: Containers](https://github.com/lapao9/devops-containers)**