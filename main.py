from flask import Flask, make_response, jsonify, request
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='garagem',
)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

carros = []
@app.route('/carros',methods=['GET'])
def get_cars():
    myCursor = mydb.cursor()
    myCursor.execute('SELECT * FROM carros')
    meus_carros = myCursor.fetchall()
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
def create_cars():
    carro = request.json
    if not carro or 'marca' not in carro or 'modelo' not in carro or 'ano' not in carro:
        return make_response(jsonify(message="Dados incompletos"), 400)

    my_cursor = mydb.cursor()
    sql = "INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s)"
    val = (carro['marca'], carro['modelo'], carro['ano'])
    try:
        my_cursor.execute(sql, val)
        mydb.commit()
        return make_response(jsonify(
            message="Carro cadastrado",
            data=carro
        ), 200)
    except mysql.connector.Error as err:
        # Lidar com erros de banco de dados
        return make_response(jsonify(message=f"Erro ao cadastrar carro: {err}"), 500)
    finally:
        my_cursor.close()



app.run()

