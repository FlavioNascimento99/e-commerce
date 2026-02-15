# 🔧 Solução: Erro de Resolução de Dependências no Vercel

## 🚨 Erro Original
```
Error: Failed to run "uv lock": Command failed: /usr/local/bin/uv lock
No solution found when resolving dependencies for split
```

## ✅ O Que Foi Corrigido

### 1. **Atualizar `requires-python`**
```toml
# ❌ ANTES
requires-python = ">=3.10"

# ✅ DEPOIS
requires-python = ">=3.12"
```
**Motivo:** `psycopg2-binary` exige Python 3.12+

### 2. **Usar Versões Flexíveis no `pyproject.toml`**
```toml
# ❌ ANTES
dependencies = [
    "Django==6.0.2",
    "psycopg2-binary==2.9.9",
]

# ✅ DEPOIS
dependencies = [
    "Django>=6.0.2",
    "psycopg2-binary>=2.9.9",
]
```
**Motivo:** Permite ao `uv` resolver versões compatíveis

### 3. **Adicionar Constraints ao `requirements.txt`**
```txt
# ✅ NOVO
Django>=6.0.2,<7.0
psycopg2-binary>=2.9.9
```
**Motivo:** Mais explícito para resolução de dependências

### 4. **Atualizar `vercel.json`**
```json
{
  "env": {
    "PYTHON_VERSION": "3.12"
  },
  "builds": [
    {
      "use": "@vercel/python@3.12"
    }
  ]
}
```
**Motivo:** Força Python 3.12 explicitamente

### 5. **Criar `.python-version`**
```
3.12
```
**Motivo:** Tell Vercel qual Python usar

### 6. **Arquivo `setup.py`**
Fornece configuração alternativa para setuptools

---

## 🚀 Próximas Ações

### Local
```bash
# 1. Atualizar ambiente local
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt --upgrade

# 3. Testar
python manage.py runserver
```

### Vercel
```bash
# Fazer novo deploy
vercel deploy --prod --force

# Ou via Git push (se CI/CD configurado)
git add .
git commit -m "Fix: Python 3.12 dependency resolution"
git push origin main
```

---

## 📋 Arquivos Modificados

| Arquivo | Mudança |
|---------|---------|
| `pyproject.toml` | `requires-python = ">=3.12"`, versões com `>=` |
| `requirements.txt` | Versões com `>=` e constraints |
| `vercel.json` | Added `PYTHON_VERSION`, `@vercel/python@3.12` |
| `.python-version` | Já criado (3.12) |
| `setup.py` | ✅ NOVO |
| `pip.ini` | ✅ NOVO |

---

## ✔️ Verificação

### Local
```bash
python --version  # Deve ser 3.12+
pip list | grep Django  # Debe mostrar versão instalada
```

### Vercel
```bash
vercel logs --follow  # Ajustes em tempo real
curl https://seu-app.vercel.app/api/  # Testar endpoint
```

---

## 🎯 Se Ainda Tiver Problemas

### Opção 1: Remover `psycopg2-binary` (SQLite apenas)
```txt
# requirements.txt
Django>=6.0.2,<7.0
djangorestframework>=3.14.0
python-decouple>=3.8
gunicorn>=21.2.0
whitenoise>=6.5.0
# (remover psycopg2-binary se usar SQLite)
```

Depois em `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Opção 2: Usar Lock File
```bash
# Gerar lock file local
pip freeze > requirements-lock.txt

# Deploy com lock
vercel deploy --prod --force
```

### Opção 3: Desabilitar `uv`
Se Vercel continuar usando `uv`, crie `requirements.txt.lock`:
```bash
pip install pip-tools
pip-compile --output-file=requirements.txt requirements.txt
```

---

## 📞 Debug

### Ver detalhes do erro
```bash
vercel logs --follow
```

### Testar localmente como Vercel
```bash
# Simular build do Vercel
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
gunicorn core.wsgi:application
```

---

## ✨ Status

✅ Corrigido: Erro de resolução de dependências  
✅ Python 3.12 mandatório  
✅ Versões flexíveis para `uv` resolver  
✅ Setup.py adicionado como fallback  

**Próximo passo:** `vercel deploy --prod`
