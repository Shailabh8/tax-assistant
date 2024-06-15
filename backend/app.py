from flask import Flask, jsonify, request
import spacy

app = Flask(__name__)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    return jsonify(message="Welcome to the Tax Assistant Backend")

@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    # Logic to handle profile creation (save to database)
    return jsonify(message="Profile created", data=data)

@app.route('/calculate-taxes', methods=['POST'])
def calculate_taxes():
    data = request.json
    # Logic to calculate taxes based on user profile and financial data
    taxes = calculate_tax_logic(data)
    return jsonify(taxes=taxes)

def calculate_tax_logic(data):
    # Example tax calculation logic
    income = data.get('income', 0)
    deductions = data.get('deductions', 0)
    taxable_income = income - deductions
    tax = taxable_income * 0.1  # Example tax rate
    return tax

@app.route('/upload-document', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify(error="No file part")
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file")
    if file:
        # Logic to process and analyze the uploaded document
        return jsonify(message="File uploaded successfully")

@app.route('/ask-question', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    doc = nlp(question)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Logic to provide tax advice based on extracted entities
    return jsonify(entities=entities)

if __name__ == '__main__':
    app.run(debug=True)
