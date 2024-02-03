from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/inquiryoption')
def inquiry_option():
    return render_template('inquiryoption.html')

@app.route('/inquiryform-a')
def inquiryform():
    return render_template('inquiryform-a.html')

@app.route('/inquiryform-t')
def inquiryform_t():
    return render_template('inquiryform-t.html')


@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    if request.method == 'POST':
        # Holen Sie sich die Formulardaten aus dem Request
        arrival = request.form['arrival']
        departure = request.form['departure']
        amount = request.form['amount']
        budget = request.form['budget']
        requests = request.form['requests']
        
        # Führen Sie hier die Verarbeitung der Formulardaten durch
        # Zum Beispiel: Speichern in einer Datenbank, Senden von E-Mails, usw.
        
        # Geben Sie eine Bestätigungsseite zurück oder leiten Sie die Benutzer weiter
        return "Vielen Dank für Ihre Anfrage! Wir werden uns in Kürze bei Ihnen melden."

if __name__ == '__main__':
    app.run(debug=True)










