from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained best model
model = pickle.load(open("heartdisease_best_model.pkl", "rb"))

REQUIRED_FIELDS = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "thalach", "exang", "oldpeak"
]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":

<<<<<<< HEAD
        # Check for empty fields FIRST
        for field in REQUIRED_FIELDS:
            if field not in request.form or request.form[field].strip() == "":
                error = "! Please fill in all fields before predicting."
                return render_template("index.html", prediction=None, error=error)

        try:
            # Convert inputs ONLY after validation
=======
        # 1️) Check for empty fields FIRST
        for field in REQUIRED_FIELDS:
            if field not in request.form or request.form[field].strip() == "":
                error = "!! Please fill in all fields before predicting."
                return render_template("index.html", prediction=None, error=error)

        try:
            # 2️) Convert inputs ONLY after validation
>>>>>>> cf38985775289485c788c3034f89b7c9dbc83199
            input_data = np.array([[
                float(request.form["age"]),
                float(request.form["sex"]),
                float(request.form["cp"]),
                float(request.form["trestbps"]),
                float(request.form["chol"]),
                float(request.form["fbs"]),
                float(request.form["thalach"]),
                float(request.form["exang"]),
                float(request.form["oldpeak"])
            ]])

            prediction = model.predict(input_data)[0]

        except ValueError:
<<<<<<< HEAD
            #  Only catches non-numeric inputs
            error = "! Please enter valid numeric values."
=======
            # 3️) Only catches non-numeric inputs
            error = !! Please enter valid numeric values."
>>>>>>> cf38985775289485c788c3034f89b7c9dbc83199

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
