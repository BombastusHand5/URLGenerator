# URLGenerator
Create clickable messenger links with a predefined message and a QR code.

## Run locally

Install the dependencies and start the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run main.py
```

## Publish with Streamlit Community Cloud

Push this repository to GitHub, then create an app in Streamlit Community Cloud. Select this repository and branch, and set `main.py` as the app's main file. Streamlit installs the packages listed in `requirements.txt` during deployment.

Threema and WhatsApp links include the message text. Signal links open the chat but do not prefill the message.
