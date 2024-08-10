import os
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/Component', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt', "")
    try:
        response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=150
    )
        component_code = response.choices[0].text.strip()
        return jsonify({"component_code": component_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run()

