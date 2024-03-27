from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder="template")
app.config['SECRET_KEY']="lksfgnhajkfsngjkgfksnfbgfjskgbafnbkjf"

# Имитация состояния умного дома
smart_home = {
    'lights': False,
    'thermostat': 22  # температура в градусах Цельсия
}

@app.route('/')
def index():
    return render_template('index.html', lights=smart_home['lights'], thermostat=smart_home['thermostat'])

@app.route('/toggle_lights', methods=['POST'])
def toggle_lights():
    smart_home['lights'] = not smart_home['lights']
    return "Lights Toggled"

@app.route('/set_thermostat', methods=['POST'])
def set_thermostat():
    temperature = request.form.get('temperature')
    if temperature is not None and temperature.isdigit():
        smart_home['thermostat'] = int(temperature)
        return "Thermostat set to {}°C".format(temperature)
    else:
        return "Invalid temperature value"

if __name__ == '__main__':
    app.run(debug=True)
