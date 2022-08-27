import mysql.connector as connection
from flask import Flask, request, jsonify

app = Flask(__name__)


def createTable():
    try:
        mydb = connection.connect(host="localhost", database="ineuron", user="root", passwd="yash", use_pure=True)
        print(mydb.is_connected())

        query = "create table if not exists user_data(name VARCHAR(30), age int(5), dob DATE)"

        cur = mydb.cursor()
        cur.execute(query)
        print("table created")


    except Exception as e:
        mydb.close()
        print(str(e))

@app.route('/insert', methods = ['GET','POST'])
def insertData():
    createTable()
    if (request.method == 'POST'):
        name = request.json['name']
        age = request.json['age']
        dob = request.json['dob']

        try:
            mydb = connection.connect(host="localhost", database="ineuron", user="root", passwd="yash", use_pure=True)
            print(mydb.is_connected())

            cur = mydb.cursor()
            cur.execute("insert into ineuron.user_data values(%s, %s, %s)",(name,age,dob))
            mydb.commit()
            print("data inserted")
            mydb.close()
            return jsonify(str('successfully inserted'))

        except Exception as e:
            mydb.close()
            print(str(e))


@app.route('/update', methods=['GET', 'POST'])
def updateData():
    createTable()
    if (request.method == 'POST'):
        name = request.json['name']
        age = request.json['age']
        dob = request.json['dob']

        try:
            mydb = connection.connect(host="localhost", database="ineuron", user="root", passwd="yash", use_pure=True)
            print(mydb.is_connected())

            queryUpdate = 'Update user_data set age = %s, dob = %s where name = %s'
            val = (age,dob,name)
            cur = mydb.cursor()
            cur.execute(queryUpdate,val)
            mydb.commit()
            mydb.close()
            return jsonify(str('successfully updated'))

        except Exception as e:
            mydb.close()
            print(str(e))


@app.route('/delete', methods=['GET', 'POST'])
def deleteData():
    createTable()
    if request.method == 'POST':
        name = request.json['name']

        try:
            mydb = connection.connect(host="localhost", database="ineuron", user="root", passwd="yash", use_pure=True)
            print(mydb.is_connected())

            queryDelete = 'delete from user_data where name = %s'
            val = (name)
            cur = mydb.cursor()
            cur.execute(queryDelete,val)
            mydb.commit()
            mydb.close()
            return jsonify(str('successfully deleted'))

        except Exception as e:
            mydb.close()
            print(str(e))


@app.route('/fetch', methods=['GET', 'POST'])
def fetchData():
        try:
            mydb = connection.connect(host="localhost", database="ineuron", user="root", passwd="yash", use_pure=True)
            print(mydb.is_connected())

            queryFetch = 'select * from user_data'
            cur = mydb.cursor()
            cur.execute(queryFetch)
            l = []
            for i in cur.fetchall():
                l.append(i)
            return jsonify(str(l))

        except Exception as e:
            mydb.close()
            print(str(e))

if __name__ == '__main__':
    app.run()
