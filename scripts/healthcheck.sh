#!/bin/bash
set -e

echo "🔍 A verificar saúde da API..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)

if [ "$response" = "200" ]; then
  echo "✅ API está saudável"
  exit 0
else
  echo "❌ API não responde (HTTP $response)"
  exit 1
fi