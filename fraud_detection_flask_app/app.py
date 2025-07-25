from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("xgboost_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    probability = None
    if request.method == "POST":
        try:
            features = [float(request.form[f"V{i}"]) for i in range(1, 29)]
            amount = float(request.form["amount"])
            features.append(amount)
            input_array = np.array(features).reshape(1, -1)
            prediction = model.predict(input_array)[0]
            proba = model.predict_proba(input_array)[0][1]
            result = "Fraudulent Transaction ⚠️" if prediction == 1 else "Legitimate Transaction ✅"
            probability = round(proba, 4)
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
