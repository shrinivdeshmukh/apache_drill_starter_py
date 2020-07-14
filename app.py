import findspark
import os
findspark.init(os.environ.get("SPARK_HOME"))
import pandas as pd
from pyspark.sql import SparkSession
from flask import Flask, render_template, url_for, json,request,redirect,url_for
import pyspark
# from google.cloud import storage
# storage_client = storage.Client.from_service_account_json('/root/gcskey.json')
# buckets = storage_client.lookup_bucket('prometheus-master')

import mysql.connector
import pyodbc 
conn = pyodbc.connect("DSN=drill64", autocommit=True)
cursor = conn.cursor()


spark = SparkSession.builder.appName("Python Spark SQL basic example").master("yarn").getOrCreate()

app = Flask(__name__)

cnx = mysql.connector.connect(user='root', password='example',host='0.0.0.0',database=os.environ.get("DB_NAME"))

# @app.route("/")
# def login():
#     return render_template('log.html')

@app.route('/Authenticate', methods=['GET','POST'])
def Authenticate():
    username = request.form['uname']
    password = request.form['pwd']
    cursor = cnx.cursor()
    cursor.execute("SELECT * from user where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return render_template('log.html')
    else:
        return redirect(url_for('inde'))

# @app.route('/inde')
# def inde():
#     return render_template('inde.html')

@app.route('/in', methods=['GET','POST'])
def conn():
    foreman = request.form['drill_host']
    query = request.form['query']
    schema = request.form['schema']
    global dataframe_mysql
    dataframe_mysql = pd.read_sql('select * from %s.dummy."%s"' % (schema,query),conn)
    #pandas_df = dataframe_mysql.toPandas()
    pandas_html = dataframe_mysql.to_html(classes=["example table table-striped table-bordered table-hover"])
    return render_template('query.html', pandas_html = pandas_html)


@app.route('/write_to_mysql', methods=['POST','GET'])
def write_to_mysql():
    write_to_table = request.form['write_to_mysql']
    #df_pyspark = spark.createDataFrame(to_mysql_df)
    dataframe_mysql.write.format("jdbc").options(
    url="jdbc:mysql://172.29.79.73:3306/dummy",
    driver = "com.mysql.jdbc.Driver",
    dbtable = "%s" % (write_to_table),
    user="root",
    password="").option("inferSchema","True").save()
    return render_template('query.html')

# @app.route('/write_to_gs', methods=['POST','GET'])
# def write_to_gs():
#     write_to_bucket = request.form['write_to_gs']
#     blob = buckets.get_blob('shree_project_n/')
#     if not blob:
#         dataframe_mysql.write.option('path','gs://prometheus-master/%s' % (write_to_bucket)).format("csv").save()
#     else:
#         dataframe_mysql.write.option('path','gs://prometheus-master/%s' % (write_to_bucket)).   mode('append').format("csv").save()
        
#     return render_template('query.html')

# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')


# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
