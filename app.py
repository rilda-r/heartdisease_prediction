from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("heartdisease_rfmodel.pkl", "rb"))

REQUIRED_FIELDS = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "thalach", "exang", "oldpeak"
]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":

        # Check for missing or empty inputs
        for field in REQUIRED_FIELDS:
            if field not in request.form or request.form[field].strip() == "":
                error = "⚠️ Please fill in all the fields before predicting."
                return render_template("index.html", prediction=None, error=error)

        try:
            # Convert inputs to float
            age = float(request.form["age"])
            sex = float(request.form["sex"])
            cp = float(request.form["cp"])
            trestbps = float(request.form["trestbps"])
            chol = float(request.form["chol"])
            fbs = float(request.form["fbs"])
            thalach = float(request.form["thalach"])
            exang = float(request.form["exang"])
            oldpeak = float(request.form["oldpeak"])

            input_data = np.array(
                [[age, sex, cp, trestbps, chol, fbs, thalach, exang, oldpeak]]
            )

            prediction = model.predict(input_data)[0]

        except ValueError:
            error = "❌ Invalid input. Please enter numeric values only."

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True)
