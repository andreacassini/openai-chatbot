# openai-chatbot

Un semplice chatbot da riga di comando (CLI) scritto in Python, che usa l'API di OpenAI per generare risposte.

Progetto realizzato come primo esercizio pratico per imparare le basi dello sviluppo Python e dell'integrazione con le API di intelligenza artificiale.

## Come funziona

Lo script legge un messaggio da tastiera, lo invia al modello OpenAI, e stampa a schermo la risposta. Il ciclo continua finché non si scrive `exit`.

## Requisiti

- Python 3
- Una API key OpenAI valida ([platform.openai.com](https://platform.openai.com))

## Setup

1. Clona il repository e spostati nella cartella del progetto.

2. Crea un ambiente virtuale e attivalo:

   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Installa le dipendenze:

   ```
   pip install openai python-dotenv
   ```

4. Crea un file `.env` nella cartella principale del progetto con la tua API key:

   ```
   OPENAI_API_KEY=la-tua-chiave-qui
   ```

   Il file `.env` è escluso da Git (vedi `.gitignore`) e non va mai condiviso o caricato online.

## Uso

Avvia il chatbot con:

```
python main.py
```

Scrivi i tuoi messaggi quando compare il prompt `Tu: `. Scrivi `exit` per terminare il programma.

## Struttura del progetto

- `main.py` — script principale del chatbot
- `.env` — contiene la API key (non tracciato da Git)
- `.gitignore` — esclude `.env`, l'ambiente virtuale e i file di sistema dal repository
