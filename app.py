from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickle file
model = pickle.load(open("Trinitt.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve the values of the input fields
    nitrogen_content = request.form["NITROGEN_CONTENT"]
    phosphorous_content = request.form["PHOSPHOROUS_CONTENT"]
    potassium_content = request.form["POTASSIUM_CONTENT"]
    temperature = request.form["TEMPERATURE"]
    humidity = request.form["HUMIDITY"]
    ph_soil = request.form["PH_SOIL"]
    rainfall = request.form["RAINFALL"]
    
    # Use the model to predict the crop recommendation
    prediction = model.predict([[nitrogen_content, phosphorous_content, potassium_content, temperature, humidity, ph_soil, rainfall]])
    prediction_text = "The recommended crop is: " + prediction
    
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)