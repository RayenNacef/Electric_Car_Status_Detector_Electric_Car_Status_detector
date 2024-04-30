from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickled model
with open('regmodel.pkl', 'rb') as model_file:
    regression_model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get feature values from the form
        time = float(request.form['Time [s]'])
        battery_voltage = float(request.form['Battery Voltage [V]'])
        motor_torque = float(request.form['Motor Torque [Nm]'])
        battery_current = float(request.form['Battery Current [A]'])
        battery_temperature = float(request.form['Battery Temperature'])

        # Prepare the features for prediction
        input_features = [
            [time, battery_voltage, motor_torque, battery_current, battery_temperature]
        ]

        # Make a prediction using your trained model
        prediction = regression_model.predict(input_features)

        # Display the predicted status based on the prediction value
        status = "Car Status: " + ("High" if prediction > 0.75 else "Medium" if prediction > 0.25 else "Low")

        return render_template('results.html', prediction=status)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickled model
with open('regmodel.pkl', 'rb') as model_file:
    regression_model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get feature values from the form
        time = float(request.form['Time [s]'])
        battery_voltage = float(request.form['Battery Voltage [V]'])
        motor_torque = float(request.form['Motor Torque [Nm]'])
        battery_current = float(request.form['Battery Current [A]'])
        battery_temperature = float(request.form['Battery Temperature'])

        # Prepare the features for prediction
        input_features = [
            [time, battery_voltage, motor_torque, battery_current, battery_temperature]
        ]

        # Make a prediction using your trained model
        prediction = regression_model.predict(input_features)

        # Display the predicted status based on the prediction value
        status = "Car Status: " + ("High" if prediction > 0.75 else "Medium" if prediction > 0.25 else "Low")

        return render_template('results.html', prediction=status)

if __name__ == '__main__':
    app.run(debug=True)
