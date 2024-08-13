from flask import Flask, request, jsonify, Response
import requests
import json

app = Flask(__name__)

model = "gemma2:2b"

preprompt = "From now on you will be SHAI. Here is what you need to do: The user provides a description of a task they want to perform on Linux. You need to respond only with the corresponding Linux command, without any description or explanation. Do not add any additional text. Example interaction: User: How can I list all the files in a directory? SHAI: ls -la. Here is the prompt you need to respond to: "

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400
    
    user_prompt = data['prompt']
    combined_prompt = f"{preprompt}\nUtente: {user_prompt}"
    
    model_data = {
        "model": model,
        "prompt": combined_prompt
    }
    
    try:
        with requests.post("http://localhost:11434/api/generate", json=model_data, stream=True) as response:
            response.raise_for_status()
            response_text = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_object = json.loads(line.decode('utf-8'))
                        response_text += json_object.get('response', '')
                        if json_object.get('done', False):
                            break
                    except ValueError as e:
                        continue
            return jsonify({'response': response_text})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=11435)
