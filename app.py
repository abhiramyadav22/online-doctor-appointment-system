from flask import Flask, render_template, request, jsonify
from datetime import datetime
app = Flask(__name__)
# Temporary storage for appointments
appointments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        date = data.get('date')
        doctor = data.get('doctor')

        # Validate input
        if not name or not email or not date or not doctor:
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400
        
        # Store appointment
        appointments.append({
            'name': name,
            'email': email,
            'date': date,
            'doctor': doctor,
            'booked_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        return jsonify({'status': 'success', 'message': 'Appointment booked successfully!'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify({'appointments': appointments})

if __name__== '__main__':
    app.run(debug=True)
