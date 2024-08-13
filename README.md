SHAI : (SHELL-AI) Offline AI helper to generate Linux command prompts when asked!

First, a lightweight ollama model is required to run the application.
You can download ollama here : https://ollama.com/download

After installing Ollama you need a model : https://ollama.com/library

I suggest you a light model if you're running on a low specs laptop, Google gemma2b is what im using now.
You can find it here : https://ollama.com/library/gemma2:2b

After the download of your model, you'll need :

JQ (json manipulation via bash)

python (to run flask)

sudo apt install jq

sudo apt install python3

and add to your .zshrc or .bashrc 

move shai.sh and flaskserver_shai.py in a folder of your choice

After that, run :
python flaskserver_shai.py

You can setup a service to start the flaskserver at boot!

Add SHAI path and alias to bashrc or zshrc

export SHAI="/your_desired_path_here/shai.sh"

alias shai="bash \$SHAI"

reload any opened shell
source /home/your_username/.bashrc or ./zshrc

If you have done everything correctly , just prompt :
shai "list all files in a directory" 
(remember to use double quotes!)

output should be : ls -la

The quality of the response depends on the AI model you're using, larger models are more precise and correct while smaller ones are faster but sometimes imprecise or incorrect.

If you want to test other models make sure to change the model variable in the flaskserver_shai.py file here and restart the server :

    llama3_data = {
        "model": "gemma2:2b",
        "prompt": combined_prompt
    }


Have fun!
