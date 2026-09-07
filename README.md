## API Serverless (Contacts API)

## 1. Sobre
### 1.1. Informações Gerais
- API Serverless é uma API rodando em uma única AWS Lambda, com roteamento interno através da biblioteca AWS Lambda Powertools;
- Os testes são locais via `API_GATEWAY_PAYLOAD.json` simulando um payload do API Gateway, sem necessidade de deploy;
- No diretório `/events` contém uma coletânea de payloads de eventos do API Gateway prontos para uso nos testes locais (diferentes métodos, rotas e cenários).

### 1.2. Pré-requisitos
- Python (>= 3.14.4)
- AWS Lambda
- AWS Lambda Powertools (Event Handler / `APIGatewayRestResolver`)
- AWS API Gateway (REST API: payload v1)
- AWS CLI
- IAM User válido
- Terraform
> __Importante__: O IAM User utilizado pela aplicação deve possuir as permissões necessárias para realizar as operações no `AWS Lambda.` Em ambientes de desenvolvimento, pode utilizar a política `AdministratorAccess`.

### 1.3. Configuração do AWS CLI
O projeto utiliza serviços da AWS durante o desenvolvimento local. Por isso, é necessário instalar o AWS CLI e configurar suas credenciais antes de iniciar a aplicação.

#### 1.3.1. Instale o AWS CLI
Siga a documentação oficial da AWS para instalar o AWS CLI:

- [Documentação oficial da AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cliv2-migration.html)

Após a instalação, confirme se o comando encontra-se disponível:

```bash 
aws --version
```   

#### 1.3.2. Configure as credenciais da AWS
Execute:

```bash 
aws configure
```   

O comando solicitará os seguintes preenchimentos:

```bash
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]:
Default output format [None]:
``` 

Preencha apenas:
- `AWS Access Key ID`: sua Access Key da AWS
- `AWS Secret Access Key`: sua Secret Access Key da AWS
- `Default output format`: json

Deixe os campos abaixo em branco:
- Default region name [None]: a região será definida pela aplicação.

> __Importante:__ não defina uma região padrão no AWS CLI, pois a aplicação é responsável por configurar a região utilizada pelos serviços da AWS.

As credenciais serão armazenadas, por padrão, em:

```bash
~/.aws/credentials
``` 

As configurações gerais do AWS CLI serão armazenadas em:

```bash
~/.aws/config
``` 