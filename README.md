

---

````
# 📚 API Escola - FastAPI

Sistema de gerenciamento de alunos, cursos e matrículas desenvolvido com FastAPI + SQLAlchemy.

---

## 🚀 Objetivo

Esta API permite:

- Gerenciar alunos
- Gerenciar cursos
- Controlar matrículas
- Aplicar regras de negócio (validações reais)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

---

## ▶️ Como Executar o Projeto

### 1. Acesse a pasta do projeto

```bash
cd api_escola
````

---

### 2. Instale as dependências

```bash
pip install fastapi uvicorn sqlalchemy pydantic[email]
```

---

### 3. Execute o servidor

```bash
python -m uvicorn main:app --reload
```

---

### 4. A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## 🧪 Testando a API com Postman

Utilize o **Postman** para realizar requisições HTTP.

### Base URL:

```
http://127.0.0.1:8000
```

---

## 📌 Endpoints

---

### 👨‍🎓 ALUNOS

#### Criar aluno

POST `/alunos`

```json
{
  "nome": "Marcos",
  "email": "marcos@email.com"
}
```

---

#### Listar alunos

GET `/alunos?page=1&limit=10`

---

#### Buscar aluno por ID

GET `/alunos/{id}`

---

#### Atualizar aluno

PUT `/alunos/{id}`

```json
{
  "nome": "Novo Nome",
  "email": "novo@email.com"
}
```

---

#### Deletar aluno

DELETE `/alunos/{id}`

---

## 📖 CURSOS

#### Criar curso

POST `/cursos`

```json
{
  "nome": "Python",
  "descricao": "Curso completo de Python"
}
```

---

#### Listar cursos

GET `/cursos?page=1&limit=10`

---

#### Buscar curso por ID

GET `/cursos/{id}`

---

#### Atualizar curso

PUT `/cursos/{id}`

---

#### Deletar curso

DELETE `/cursos/{id}`

---

## 📝 MATRÍCULAS

#### Matricular aluno

POST `/matriculas`

```json
{
  "aluno_id": 1,
  "curso_id": 1
}
```

---

#### Listar cursos de um aluno

GET `/alunos/{id}/cursos`

---

#### Listar alunos de um curso

GET `/cursos/{id}/alunos`

---

#### Cancelar matrícula

PUT `/matriculas/{id}/cancelar`

---

#### Concluir curso

PUT `/matriculas/{id}/concluir`

---

## ⚙️ Regras de Negócio

### 📌 Matrículas

* ❌ Não permite matrícula duplicada
* ❌ Não permite aluno inexistente
* ❌ Não permite curso inexistente
* ⚠️ Máximo de 5 matrículas ativas por aluno

---

### 📌 Validação de Dados

* Email deve ser único
* Campos obrigatórios:

  * nome
  * email
  * nome do curso
* ❌ Não permite valores vazios ou inválidos

---

### 📌 Status da Matrícula

* ativa
* cancelada
* concluida

---

## ❗ Tratamento de Erros

Formato padrão:

```json
{
  "error": "Mensagem descritiva",
  "statusCode": 400
}
```

### Códigos:

* 400 → Requisição inválida
* 404 → Recurso não encontrado
* 422 → Erro de validação
* 500 → Erro interno

---

## 📂 Estrutura do Projeto

```
api_escola/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── crud_alunos.py
├── crud_cursos.py
├── crud_matriculas.py
│
└── README.md
```

---

## 💡 Melhorias Futuras

* 🔐 Autenticação com JWT
* 👤 Controle de usuários
* 📊 Dashboard
* 🐳 Docker
* ☁️ Deploy

---

## 👨‍💻 Autor

Marcos Vinicius Sousa Ferreira

Projeto desenvolvido para prática de backend com FastAPI.

```

---


```
