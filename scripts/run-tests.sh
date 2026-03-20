#!/bin/bash
set -e   # para imediatamente se qualquer comando falhar

echo "🧪 A correr testes..."
pytest tests/ -v --tb=short

echo "✅ Todos os testes passaram!"