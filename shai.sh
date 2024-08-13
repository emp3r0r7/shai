#!/bin/bash

# Verifica se jq è installato
if ! command -v jq &> /dev/null
then
    echo "jq could not be found. Please install jq to proceed."
    exit 1
fi

# Controlla se il prompt è stato fornito
if [ -z "$1" ]; then
    echo "Usage: $0 \"<prompt>\""
    exit 1
fi

PROMPT="$1"

# Invia la richiesta al server Flask e ottieni la risposta
RESPONSE=$(curl -s -X POST http://localhost:11435/api/generate -H "Content-Type: application/json" -d "{\"prompt\": \"$PROMPT\"}")

# Verifica se la risposta è vuota o contiene un errore
if [ -z "$RESPONSE" ]; then
    echo "Error: No response from server. Please ensure the server is running and reachable."
    exit 1
elif echo "$RESPONSE" | jq -e .error > /dev/null; then
    ERROR_MSG=$(echo $RESPONSE | jq -r '.error')
    echo "Error: $ERROR_MSG"
    exit 1
fi

# Estrai il comando dalla risposta usando jq
COMMAND=$(echo $RESPONSE | jq -r '.response')

# Stampa il comando
echo $COMMAND
