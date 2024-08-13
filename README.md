Sure! Here's a more polished and structured version of your README, suitable for GitHub:

---

# SHAI (SHELL-AI) - Offline AI Helper for Generating Linux Commands

SHAI is an offline AI-powered tool designed to help you generate Linux command prompts on the fly. This lightweight application leverages an Ollama model to deliver quick and accurate command suggestions based on your input.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Ollama**: A lightweight model runner.
   - Download Ollama here: [Ollama Download](https://ollama.com/download)
   - Choose a model from the Ollama library: [Ollama Library](https://ollama.com/library)
     - Recommended model: [Google Gemma2b](https://ollama.com/library/gemma2:2b) for low-spec laptops.

2. **JQ**: For JSON manipulation via Bash.
   - Install JQ: `sudo apt install jq`

3. **Python**: Required to run the Flask server.
   - Install Python: `sudo apt install python3`

## Installation

1. **Set up the Environment**:
   - Add the following lines to your `.bashrc` or `.zshrc`:
     ```bash
     export SHAI="/your_desired_path_here/shai.sh"
     alias shai="bash \$SHAI"
     ```

   - Reload your shell configuration:
     ```bash
     source /home/your_username/.bashrc
     # or
     source /home/your_username/.zshrc
     ```

2. **Move the Files**:
   - Place `shai.sh` and `flaskserver_shai.py` in a folder of your choice.

3. **Run the Flask Server**:
   - Start the Flask server by running:
     ```bash
     python flaskserver_shai.py
     ```

4. (Optional) **Set Up as a Service**:
   - You can configure the Flask server to start automatically at boot.

## Usage

Once everything is set up, you can start using SHAI by typing commands in the following format:

```bash
shai "list all files in a directory"
```

The output should be:

```bash
ls -la
```

> **Note**: The quality of the response depends on the AI model you are using. Larger models are generally more accurate but may be slower, while smaller models are faster but may occasionally provide imprecise or incorrect results.

### Switching Models

If you want to try different AI models, you can change the model variable in the `flaskserver_shai.py` file. Modify the `model` variable, then restart the server:

```python
    model_data = {
        "model": model,
        "prompt": combined_prompt
    }
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

---

## Have Fun!

Enjoy using SHAI to simplify your Linux command generation tasks!

---
