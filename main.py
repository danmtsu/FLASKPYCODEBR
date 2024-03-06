from flask import Flask, make_response, jsonify, request
import mysql.connector

#Estabelece uma conexão com o banco de dados MySQL usando os parâmetros fornecidos (host, usuário, senha e nome do banco de dados),do docker-compose.yaml.
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='garagem',
)
#Cria uma instância da classe Flask, que será o aplicativo Flask.
app = Flask(__name__)
#Desativa a ordenação automática das chaves JSON, o que mantém a ordem original dos campos JSON nas respostas.
app.config['JSON_SORT_KEYS'] = False

carros = []
#@app.route('/carros', methods=['GET']): Define uma rota para a URL '/carros' que aceita apenas solicitações GET.
@app.route('/carros',methods=['GET'])
def get_cars(): #Esta função é chamada quando uma solicitação GET é feita para '/carros'. Ela busca todos os carros no banco de dados e os retorna como uma resposta JSON.
    myCursor = mydb.cursor() #Cria um cursor para interagir com o banco de dados.
    myCursor.execute('SELECT * FROM carros')#Executa uma consulta SQL no banco de dados.
    meus_carros = myCursor.fetchall()#Obtém todos os resultados de uma consulta SQL.
    for carro in meus_carros:
        carros.append({
            'marca':carro[1],
            'modelo':carro[2],
            'ano':carro[3]
        })
    return make_response(
        jsonify(
            message="Lista de carros"
            ,data=carros
            )
        )

@app.route('/carros', methods=['POST'])
def create_cars(): #Esta função é chamada quando uma solicitação POST é feita para '/carros'. Ela insere um novo carro no banco de dados com base nos dados fornecidos na solicitação JSON e retorna uma mensagem de sucesso ou erro.
    carro = request.json
    if not carro or 'marca' not in carro or 'modelo' not in carro or 'ano' not in carro:
        return make_response(jsonify(message="Dados incompletos"), 400)

    my_cursor = mydb.cursor()
    sql = "INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s)"
    val = (carro['marca'], carro['modelo'], carro['ano'])
    try:#O bloco try envolve a execução do código para inserir um novo carro no banco de dados.
        my_cursor.execute(sql, val)
        mydb.commit()#Confirma a transação no banco de dados.
        return make_response(jsonify(
            message="Carro cadastrado",
            data=carro
        ), 200)
    except mysql.connector.Error as err: # captura exceções que podem ocorrer durante a execução do código no bloco try
        # Lidar com erros de banco de dados
        return make_response(jsonify(message=f"Erro ao cadastrar carro: {err}"), 500)#Nesse caso, ele captura exceções do tipo mysql.connector.Error e lida com elas retornando uma mensagem de erro adequada.
    finally:#é usado para garantir que o cursor usado para executar a operação no banco de dados seja fechado após a conclusão, independentemente de ocorrer uma exceção ou não.
        my_cursor.close()# Fecha o cursor após a conclusão da transação.



app.run()

