# Flask MySQL API para Gerenciamento de Carros

Esta é uma API simples construída em Python usando Flask para gerenciar informações sobre carros em um banco de dados MySQL.

## Funcionalidades

- `GET /carros`: Retorna uma lista de todos os carros armazenados no banco de dados.
- `POST /carros`: Adiciona um novo carro ao banco de dados com base nos dados fornecidos.

## Pré-requisitos

- Python 3.x instalado
- Flask e mysql-connector-python bibliotecas Python instaladas
- MySQL Server instalado e em execução
- Docker e docker-compose

## Instalação e Uso

1. Clone este repositório:
   ```
   https://github.com/danmtsu/FLASKPYCODEBR.git
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure a conexão com o banco de dados editando o arquivo `main.py` e ajustando os parâmetros de conexão com o MySQL.

4. Inicie o servidor Flask:
   ```
   python main.py
   ```

5. Acesse a API através de um cliente HTTP, como o Postman:
   - `GET /carros`: `http://localhost:5000/carros`
   - `POST /carros`: `http://localhost:5000/carros`

## Observações

- Certifique-se de ter configurado corretamente a conexão com o banco de dados MySQL antes de iniciar o servidor Flask.
- Esta é uma aplicação de demonstração e pode ser estendida com mais funcionalidades conforme necessário.

Sinta-se à vontade para explorar e modificar o código-fonte de acordo com suas necessidades!

Se você tiver alguma dúvida ou encontrar problemas, não hesite em entrar em contato.
