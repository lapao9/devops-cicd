FROM python:3.12-slim

# Metadata profissional
LABEL org.opencontainers.image.source="https://github.com/lapao9/devops-cicd"
LABEL org.opencontainers.image.description="DevOps Task Manager API"

WORKDIR /app

# Instala dependências (camada separada para cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the application code
COPY . .

#Non root user for security
RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

EXPOSE 8000

#Without --reload for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
