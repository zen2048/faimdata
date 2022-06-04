from flask import Flask, jsonify, request
from db.query import * 
import html


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/clinic/', methods=['GET'])
def clinic():
    return getClinicName()

@app.route('/provider/search/<string:pattern>', methods=['GET'])
def search(pattern):
    providers = searchProviders(html.unescape(pattern))
    return jsonify(providers)

@app.route('/provider/availability/<string:provider_first_name>/<string:provider_last_name>/<string:start_time>/<string:end_time>', methods=['GET'])
def availability(provider_first_name, provider_last_name, start_time, end_time):
    providers = checkProviderAvailability(html.unescape(provider_first_name),html.unescape(provider_last_name),html.unescape(start_time),html.unescape(end_time))
    return jsonify(providers)

@app.route('/book/', methods=['POST'])
def book():
    provider_first_name = request.form.get('provider_first_name')
    provider_last_name = request.form.get('provider_last_name')
    start_time = request.form.get('start_time')
    patient_first_name = request.form.get('patient_first_name')
    patient_last_name = request.form.get('patient_last_name')
    update_time = request.form.get('update_time')
    rowcount = bookAppointment(html.unescape(provider_first_name), html.unescape(provider_last_name), html.unescape(start_time), html.unescape(patient_first_name), html.unescape(patient_last_name), html.unescape(update_time))
    return str(rowcount)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)