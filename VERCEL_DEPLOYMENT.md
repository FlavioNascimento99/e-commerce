# 🚀 Guia Completo: Deploy no Vercel

## 📌 Índice
1. [Pré-requisitos](#pré-requisitos)
2. [O Que Foi Feito](#o-que-foi-feito)
3. [Configuração Local](#configuração-local)
4. [Configuração no Vercel](#configuração-no-vercel)
5. [Executar Deploy](#executar-deploy)
6. [Troubleshooting](#troubleshooting)
7. [Estrutura do Projeto](#estrutura-do-projeto)

---

## 📋 Pré-requisitos

### Sistema
- ✅ Python 3.10+ (testado em 3.12)
- ✅ pip (gerenciador de pacotes)
- ✅ Git para versionamento
- ✅ Conta no [Vercel](https://vercel.com)

### Instalações Requeridas
```bash
# Instalar Node.js (para Vercel CLI)
# Download: https://nodejs.org/

# Instalar Vercel CLI globalmente
npm install -g vercel

# Verificar instalações
python --version
node --version
vercel --version
```

---

## 🔨 O Que Foi Feito

### 1. **Configuração Python**

#### ✅ `.python-version`
```
3.12
```
**Propósito:** Especifica a versão do Python para o Vercel usar (Python 3.12)

#### ✅ `runtime.txt`
```
python-3.12.0
```
**Propósito:** Compatibilidade com diferentes plataformas de deploy

#### ✅ `pyproject.toml`
- Criado com tabela `[project]` para especificar dependências
- Tabela `[build-system]` para build tools
- Compatível com `uv lock` do Vercel
- **Conteúdo:**
  - Nome: shopxpress-ecommerce
  - Versão: 1.0.0
  - Python: >=3.10

#### ✅ `requirements.txt`
Dependências instaladas:
```
Django==6.0.2              # Framework web
djangorestframework==3.14   # API REST
python-decouple==3.8       # Variáveis de ambiente
gunicorn==21.2.0           # Servidor WSGI
whitenoise==6.5.0          # Serve static files
psycopg2-binary==2.9.9     # PostgreSQL driver
```

---

### 2. **Configuração Django para Produção**

#### ✅ `core/settings.py` - Alterações

**1. WhiteNoise Middleware adicionado:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← NOVO
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... resto dos middlewares
]
```
**Por quê?** WhiteNoise serve arquivos estáticos eficientemente em produção

**2. Static Files Configurados:**
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
**Por quê?** Garante que CSS, JS e imagens sejam servidos corretamente

**3. ALLOWED_HOSTS:**
```python
ALLOWED_HOSTS = [
    ".vercel.app",
    "e-commerce-eight-chi-37.vercel.app"
]
```
**Por quê?** Django rejeita requisições de hosts não permitidos

**4. DEBUG em Produção:**
```python
DEBUG = False  # NUNCA True em produção!
```

#### ✅ `core/urls.py` - Correção
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),           # Página inicial
    path('api/', views.home_api)    # ← Adicionado endpoint separado
]
```
**Por quê?** Evita conflito de rotas (ambas no mesmo path)

#### ✅ `core/views.py` - Correção
```python
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def home_api(request):
    return JsonResponse({"message": "Django is ON! 🚀", "status": "success"})
```
**Por quê?** JsonResponse é seguro e estruturado para APIs

#### ✅ `core/wsgi.py` - Intacto
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()
```
**Propósito:** Entrypoint para Gunicorn executar a aplicação

---

### 3. **Arquivos de Deploy**

#### ✅ `vercel.json`
```json
{
  "builds": [
    {
      "src": "core/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "core/wsgi.py"
    }
  ]
}
```
**Propósito:**
- Define `core/wsgi.py` como aplicação Python
- Roteia todas as requisições para o WSGI

#### ✅ `Procfile`
```
web: gunicorn core.wsgi:application
```
**Propósito:** Tell Vercel como iniciar a aplicação com Gunicorn

#### ✅ `build.sh`
```bash
#!/bin/bash
python manage.py collectstatic --no-input
python manage.py migrate --no-input
```
**Propósito:**
- Coleta arquivos estáticos (CSS, JS, imagens)
- Aplica migrações do banco de dados

---

### 4. **Arquivos de Configuração**

#### ✅ `.python-version`
Define Python 3.12 como versão padrão

#### ✅ `.vercelignore`
```
venv/
.git/
db.sqlite3
*.pyc
__pycache__/
```
**Propósito:** Não faz upload desses arquivos para Vercel

#### ✅ `.env.example`
Template de variáveis de ambiente:
```env
DEBUG=False
SECRET_KEY=sua-chave-secreta
ALLOWED_HOSTS=localhost,127.0.0.1,seu-dominio.vercel.app
```

#### ✅ `DEPLOY.md`
Documentação básica de deploy

---

## 🔧 Configuração Local

### Passo 1: Preparar Ambiente
```bash
# Navegar para o projeto
cd /home/nascimento/Desktop/python_apps/ecommerce

# Ativar ambiente virtual
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

### Passo 2: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Variáveis de Ambiente
```bash
# Copiar template
cp .env.example .env

# Editar .env com seus valores
nano .env  # ou seu editor favorito
```

**Valores mínimos necessários:**
```env
DEBUG=True          # True para desenvolvimento
SECRET_KEY=dev-key  # Qualquer coisa para dev
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Passo 4: Executar Localmente
```bash
# Coletar static files
python manage.py collectstatic --no-input

# Aplicar migrações
python manage.py migrate

# Rodar servidor
python manage.py runserver

# Acessar em http://localhost:8000
```

### Passo 5: Testar com Gunicorn (como será em produção)
```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

---

## 🌐 Configuração no Vercel

### Método 1: Via CLI (Recomendado)

#### Passo 1: Fazer Login
```bash
vercel login
# Escolher método de autenticação (GitHub recomendado)
```

#### Passo 2: Fazer Deploy
```bash
# Na raiz do projeto
vercel deploy

# Ou com ambiente de produção
vercel deploy --prod
```

#### Passo 3: Confirmar Deployment
```
✅ Vercel CLI will guide you through the setup
✅ Link seu repositório Git
✅ Escolha a organização
✅ Configure projeto
```

### Método 2: Via Dashboard Web

1. Acesse [Vercel Dashboard](https://vercel.com/dashboard)
2. Clique em "New Project"
3. Selecione seu repositório Git
4. Configure conforme abaixo

---

## 📊 Variáveis de Ambiente no Vercel

### Adicionar no Dashboard

1. Vá para: **Settings → Environment Variables**
2. Adicione:

| Variável | Valor | Propósito |
|----------|-------|----------|
| `DEBUG` | `False` | Segurança em produção |
| `SECRET_KEY` | `seu-valor-aleatorio-longo` | Criptografia Django |
| `ALLOWED_HOSTS` | `seu-app.vercel.app` | Domínios permitidos |
| `DATABASE_URL` | (se usar PostgreSQL) | Conexão BD |

### Gerar SECRET_KEY Segura
```python
# Terminal Python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 🚀 Executar Deploy

### Deploy Inicial
```bash
vercel deploy --prod
```

### Deploy de Atualizações
```bash
# Commitar mudanças
git add .
git commit -m "Atualizações"
git push origin main

# Vercel faz deploy automático se configurado
# Ou manual:
vercel deploy --prod
```

### Verificar Status
```bash
vercel inspect
vercel logs
```

### Ver URL Live
```bash
vercel url
# Abre em: https://seu-app.vercel.app
```

---

## 📋 Checklist de Deploy

- [ ] Python 3.12 especificado (`.python-version`, `runtime.txt`)
- [ ] `pyproject.toml` com `[project]` table
- [ ] `requirements.txt` com todas as dependências
- [ ] `vercel.json` configurado corretamente
- [ ] `Procfile` com gunicorn
- [ ] `build.sh` executável
- [ ] `core/settings.py` em modo produção (`DEBUG=False`)
- [ ] `ALLOWED_HOSTS` configurado
- [ ] WhiteNoise middleware adicionado
- [ ] `.vercelignore` criado
- [ ] Variáveis de ambiente definidas no Vercel
- [ ] `core/urls.py` sem conflitos de rotas
- [ ] `core/views.py` usando JsonResponse
- [ ] `.gitignore` atualizado
- [ ] Repositório Git sincronizado

---

## 🔍 Troubleshooting

### Erro: "No `project` table found in pyproject.toml"
**Solução:** Certifique-se que `pyproject.toml` tem `[project]` table
```toml
[project]
name = "shopxpress-ecommerce"
# ...
```

### Erro: "Static files not found"
**Solução:** Execute build script
```bash
python manage.py collectstatic --no-input
```

### Erro: "Module not found"
**Solução:** Verifique `requirements.txt`
```bash
pip install -r requirements.txt
```

### Erro: "ALLOWED_HOSTS doesn't allow connections"
**Solução:** Adicione domínio ao settings.py
```python
ALLOWED_HOSTS = ["seu-app.vercel.app"]
```

### Erro: "502 Bad Gateway"
**Solução:**
1. Verifique logs: `vercel logs`
2. Cheque variáveis de ambiente
3. Confirme que `vercel.json` está correto

### Debug Ativo
```bash
# Ver logs em tempo real
vercel logs --follow

# Ver logs de um deployment específico
vercel logs [deployment-id]
```

---

## 📁 Estrutura Final do Projeto

```
ecommerce/
├── core/
│   ├── models/
│   ├── services/
│   ├── settings.py          ✅ Configurado
│   ├── urls.py              ✅ Corrigido
│   ├── views.py             ✅ Corrigido
│   ├── wsgi.py              ✅ Intacto
│   └── asgi.py
├── template/
│   └── home.html
├── static/
│   └── (arquivos estáticos)
├── .python-version          ✅ NOVO
├── .env.example             ✅ NOVO
├── .vercelignore            ✅ NOVO
├── .gitignore
├── build.sh                 ✅ NOVO
├── Procfile                 ✅ NOVO
├── pyproject.toml           ✅ NOVO/ATUALIZADO
├── requirements.txt         ✅ ATUALIZADO
├── runtime.txt              ✅ NOVO
├── vercel.json              ✅ Existente
├── README.md
├── DEPLOY.md                ✅ NOVO
└── db.sqlite3

✅ = Arquivo novo ou modificado para deployment
```

---

## 🎯 Endpoints Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial com Material Design |
| `/api/` | GET | Status da API |
| `/admin/` | GET/POST | Django Admin Panel |

---

## 📞 Suporte

### Recursos Úteis
- [Vercel Django Documentation](https://vercel.com/docs/frameworks/django)
- [Django Deployment Guide](https://docs.djangoproject.com/en/6.0/howto/deployment/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)
- [Gunicorn Documentation](https://gunicorn.org/)

### Verificar Status
```bash
# Status da aplicação
curl https://seu-app.vercel.app/api/

# Resposta esperada
{"message": "Django is ON! 🚀", "status": "success"}
```

---

## ✨ Resumo

Seu projeto foi configurado completamente para production-ready deployment! 

**Arquivos críticos:**
1. ✅ `pyproject.toml` - Resolve erro `uv lock`
2. ✅ `requirements.txt` - Todas as dependências
3. ✅ `settings.py` - Production settings
4. ✅ `vercel.json` - Configuração Vercel
5. ✅ `Procfile` - Startup command

**Próximo passo:** Execute `vercel deploy --prod` 🚀

---

**Data de Atualização:** Fevereiro 14, 2026  
**Versão:** 1.0.0  
**Status:** ✅ Production Ready
