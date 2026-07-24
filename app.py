from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/sqlprj.pkl")

# Load the LabelEncoder used for the target
le = joblib.load("model/performance_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    Query_Length = float(request.form["Query_Length"])
    Number_of_Joins = float(request.form["Number_of_Joins"])
    Number_of_Where = float(request.form["Number_of_Where"])
    Number_of_Subqueries = float(request.form["Number_of_Subqueries"])
    Has_GroupBy = int(request.form["Has_GroupBy"])
    Has_OrderBy = int(request.form["Has_OrderBy"])
    Has_Index = int(request.form["Has_Index"])
    Table_Size = int(request.form["Table_Size"])
    Estimated_Rows = float(request.form["Estimated_Rows"])
    Execution_Memory_MB = float(request.form["Execution_Memory_MB"])

    data = np.array([[
        Query_Length,
        Number_of_Joins,
        Number_of_Where,
        Number_of_Subqueries,
        Has_GroupBy,
        Has_OrderBy,
        Has_Index,
        Table_Size,
        Estimated_Rows,
        Execution_Memory_MB
    ]])

    prediction = model.predict(data)

    result = le.inverse_transform(prediction)[0]

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)