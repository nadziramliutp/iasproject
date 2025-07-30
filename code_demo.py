flask (python)

from flask import Flask, request

app = Flask(_name_)

@app.route('/submit', methods=['POST'])
def submit():
    # Handle Plaintext Submission
    if 'card' in request.form and 'cvv' in request.form:
        card = request.form['card']
        cvv = request.form['cvv']
        print("Received Card: {}, CVV: {}".format(card, cvv))
        return "Payment Received"

    # Handle E2EE Submission
    elif 'data' in request.form:
        encrypted_data = request.form['data']
        print("Encrypted Data Received: {}".format(encrypted_data))
        return "Encrypted Payment Received"

    # Handle Tokenization Submission
    elif 'token' in request.form:
        token = request.form['token']
        print("Received Token: {}".format(token))
        return "Tokenized Payment Processed"

    else:
        return "Invalid Submission"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)


    