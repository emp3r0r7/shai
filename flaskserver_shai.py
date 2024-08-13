from flask import Flask, request, jsonify, Response
import requests
import json

app = Flask(__name__)

# Definisci il preprompt
preprompt = "Da ora in poi tu sarai ShellGpt. Ecco cosa dovrai fare: L’utente fornisce una descrizione di un’attività che vuole eseguire su Linux. Tu devi rispondere solo ed esclusivamente con il comando Linux corrispondente, senza alcuna descrizione o spiegazione. Non aggiungere alcun testo aggiuntivo. Esempio di interazione: Utente: Come posso elencare tutti i file in una directory? ChatGPT: ls -la Ecco il prompt a cui devi rispondere: "

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400
    
    user_prompt = data['prompt']
    combined_prompt = f"{preprompt}\nUtente: {user_prompt}"
    
    llama3_data = {
        "model": "llama3",
        "prompt": combined_prompt
    }
    
    try:
        with requests.post("http://localhost:11434/api/generate", json=llama3_data, stream=True) as response:
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
