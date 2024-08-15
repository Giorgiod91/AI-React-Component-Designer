import os
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow requests from all origins

@app.route('/component', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    preDefinedComponents = data.get('componentCode')
    
    modified_prompt = f"Please generate the code for a component based on the following prompt. Only include the code with no extra explanation or description.\n\nPrompt: {prompt}\n\nCode:"


   

    
    try:
       
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "user", "content":  modified_prompt}
            ],
           
        )
        
        component_code = response.choices[0].message['content'].strip()
        return jsonify({"component_code": component_code})
    
    except Exception as e:
      
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
