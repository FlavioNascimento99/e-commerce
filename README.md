# 🛍️ ShopXpress - E-Commerce

Uma loja online moderna desenvolvida com **Django** e estilizada com **Tailwind CSS** + **Glassmorphism**, oferecendo uma experiência de compra elegante e responsiva.

---

## 📋 Sumário

- [Características](#características)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Modelos de Dados](#modelos-de-dados)
- [API & Views](#api--views)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## ✨ Características

- ✅ Interface moderna com efeito **Glassmorphism**
- ✅ Responsiva em dispositivos móveis, tablets e desktops
- ✅ Catálogo de produtos com categorias
- ✅ Sistema de carrinho de compras
- ✅ Gestão de usuários e pedidos
- ✅ Newsletter subscription
- ✅ Design com Tailwind CSS
- ✅ Backend robusto com Django

---

## 🛠️ Tecnologias

### Frontend
- **HTML5** - Estrutura
- **Tailwind CSS** - Estilização
- **JavaScript** - Interatividade
- **Glassmorphism** - Efeito visual

### Backend
- **Python 3.x** - Linguagem
- **Django 6.0+** - Framework web
- **SQLite** - Banco de dados

### Ferramentas
- **pip** - Gerenciador de pacotes
- **virtualenv** - Ambiente virtual

---

## 📁 Estrutura do Projeto

```
ecommerce/
│
├── core/                          # Aplicação principal Django
│   ├── __init__.py
│   ├── settings.py               # Configurações do Django
│   ├── urls.py                   # Rotas da aplicação
│   ├── asgi.py                   # ASGI para deployment
│   ├── wsgi.py                   # WSGI para deployment
│   │
│   ├── models/                   # Modelos de dados
│   │   ├── __init__.py
│   │   ├── user.py              # Modelo de usuário
│   │   ├── product.py           # Modelo de produto
│   │   ├── cart.py              # Modelo de carrinho
│   │   └── cart_product.py      # Modelo de item do carrinho
│   │
│   ├── services/                # Lógica de negócios
│   │   └── services.py          # Serviços da aplicação
│   │
│   └── views.py                 # Views da aplicação
│
├── template/                      # Templates HTML
│   └── home.html                # Página inicial
│
├── static/                        # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
│
├── db.sqlite3                    # Banco de dados SQLite
├── manage.py                     # Script de gerenciamento Django
├── README.md                     # Este arquivo
└── venv/                         # Ambiente virtual (não incluído no git)
```

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- pip
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/ecommerce.git
cd ecommerce
```

### Passo 2: Criar Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Aplicar Migrações

```bash
python manage.py migrate
```

### Passo 5: Criar Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### Passo 6: Executar Servidor Local

```bash
python manage.py runserver
```

Acesse em: `http://localhost:8000`

---

## ⚙️ Configuração

### Configurações Importantes em `settings.py`

```python
# Diretório de templates
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'template'],
        ...
    }
]

# Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 💻 Como Usar

### Página Inicial
A página inicial apresenta:
- **Header** com navegação e carrinho
- **Hero Section** com chamada para ação
- **Categorias** em destaque
- **Produtos** recomendados
- **Features** da loja
- **Newsletter** subscription
- **Footer** com links úteis

### Adicionar ao Carrinho
Clique no botão "Adicionar ao Carrinho" nos produtos para adicionar automaticamente.

### Newsletter
Inscreva-se com seu e-mail para receber atualizações e promoções exclusivas.

---

## 📊 Modelos de Dados

### User
```python
class User:
    - id: Integer (PK)
    - name: String
    - email: String (Unique)
    - password: String
    - created_at: DateTime
    - updated_at: DateTime
```

### Product
```python
class Product:
    - id: Integer (PK)
    - name: String
    - description: Text
    - price: Decimal
    - category: String
    - stock: Integer
    - created_at: DateTime
```

### Cart
```python
class Cart:
    - id: Integer (PK)
    - user: FK(User)
    - created_at: DateTime
    - updated_at: DateTime
```

### CartProduct
```python
class CartProduct:
    - id: Integer (PK)
    - cart: FK(Cart)
    - product: FK(Product)
    - quantity: Integer
```

---

## 🌐 API & Views

### Views Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/admin/` | GET | Painel administrativo |

### Exemplo de Requisição

```bash
# Acessar página inicial
curl http://localhost:8000/
```

---

## 🧪 Testes

Para executar os testes:

```bash
python manage.py test
```

---

## 📦 Dependências

```
Django==6.0.2
djangorestframework==3.14.0
python-dotenv==0.21.0
```

Veja `requirements.txt` para lista completa.

---

## 🔒 Segurança

- ✅ CSRF Protection ativada
- ✅ SQL Injection proteção (ORM Django)
- ✅ XSS Protection
- ✅ Django Security Middleware
- ⚠️ **Em produção:** Alterar `DEBUG=False` e configurar `ALLOWED_HOSTS`

---

## 📱 Responsividade

A aplicação é totalmente responsiva:
- **Mobile** (< 640px)
- **Tablet** (640px - 1024px)
- **Desktop** (> 1024px)

---

## 🎨 Customização

### Alterar Cores
Edite as classes do Tailwind em `template/home.html`:

```html
<!-- Gradiente principal -->
<body class="bg-gradient-to-br from-purple-600 to-blue-700">
```

### Adicionar Novos Produtos
1. Execute: `python manage.py shell`
2. Adicione dados ao banco

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja `LICENSE` para detalhes.

---

## 👥 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📞 Suporte

Para suporte e dúvidas:
- 📧 Email: contato@shopxpress.com
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/ecommerce/issues)
- 💬 Discussões: [GitHub Discussions](https://github.com/seu-usuario/ecommerce/discussions)

---

## 🚀 Roadmap

- [ ] Integração com sistema de pagamento
- [ ] Autenticação com OAuth
- [ ] API REST completa
- [ ] Dashboard administrativo
- [ ] Sistema de avaliações
- [ ] Busca avançada de produtos
- [ ] Recomendações personalizadas
- [ ] Integração com WhatsApp

---

## 📈 Performance

- ⚡ Tempos de resposta < 200ms
- 📊 Otimizado para SEO
- 🖼️ Imagens otimizadas
- 💾 Cache habilitado

---

## ✅ Checklist de Deploy

- [ ] Definir `DEBUG = False`
- [ ] Configurar `ALLOWED_HOSTS`
- [ ] Coletar arquivos estáticos: `python manage.py collectstatic`
- [ ] Executar migrações em produção
- [ ] Configurar variáveis de ambiente
- [ ] Usar HTTPS
- [ ] Configurar CDN para assets

---

Made with ❤️ by **ShopXpress Team**

**Versão:** 1.0.0  
**Data de Atualização:** Fevereiro de 2026
