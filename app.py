from flask import Flask, request, render_template
from pyspark.sql import SparkSession
from pyspark.sql.functions import split

app = Flask(__name__)
     
# Crear SparkSession global
spark = SparkSession.builder.appName("TitanicSearch").getOrCreate()

# Cargar y preparar el DataFrame UNA VEZ
df = spark.read.csv("titanic.csv", header=True, inferSchema=True)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        valor = request.form["lastname"]
        df_filtrado = df.filter(df["LastName"] == valor)
        # Convertimos a lista de diccionarios para enviar a la plantilla
        resultados = df_filtrado.select("PassengerId", "LastName", "RestOfName","Survived", "Pclass").collect()

    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
