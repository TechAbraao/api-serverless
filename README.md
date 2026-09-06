## API Serverless 

## 1. Sobre
### 1.1. Informações Gerais
- API Serverless é uma API rodando em uma única AWS Lambda, com roteamento interno através da biblioteca AWS Lambda Powertools;
- Os testes são locais via `API_GATEWAY_PAYLOAD.json` simulando um payload do API Gateway, sem necessidade de deploy;
- No diretório `/eventos` contém uma coletânea de payloads de eventos do API Gateway prontos para uso nos testes locais (diferentes métodos, rotas e cenários).

### 1.2. Tecnologias
- Python
- AWS Lambda
- AWS Lambda Powertools (Event Handler / `APIGatewayRestResolver`)
- AWS API Gateway (REST API: payload v1)

## 2. Rotas disponíveis
### 2.1. Contatos

| Método | Rota | Descrição |
|---|---|---|
| GET | `/api/contacts` | Lista contatos |
| POST | `/api/contacts` | Cria contato |
