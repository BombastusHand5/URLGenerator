# Author
#Created by BombastusHand5
#Copyright © 2026 BombastusHand5

from io import BytesIO
from urllib.parse import quote

import qrcode
import streamlit as st


st.set_page_config(page_title="Click Message")
st.title("Click Message")
st.write("Create a link that opens a messenger chat with your message.")
st.write("Created by BombastusHand5")

messenger = st.radio(
    "Choose messenger",
    ("Threema", "WhatsApp", "Signal"),
    horizontal=True,
)

if messenger == "Threema":
    contact_id = st.text_input("Threema ID", value="A1B2C3D4").strip().upper()
    phone_number = ""
else:
    phone_number = st.text_input("Phone number with country code", value="12345678")
    contact_id = ""

message = st.text_area("Message", max_chars=500, height=150)
st.caption(f"{len(message)}/500 characters")

if st.button("Generate URL", type="primary"):
    encoded_message = quote(message.strip(), safe="")
    if messenger == "Threema":
        generated_url = f"https://threema.id/{contact_id}?text={encoded_message}"
    elif messenger == "WhatsApp":
        generated_url = f"https://wa.me/{phone_number}?text={encoded_message}"
    else:
        generated_url = f"https://signal.me/#p/{phone_number}"
    st.session_state["generated_url"] = generated_url

if generated_url := st.session_state.get("generated_url"):
    st.subheader("Your URL")
    st.code(generated_url, language=None)

    qr_image = qrcode.make(generated_url)
    image_buffer = BytesIO()
    qr_image.save(image_buffer, format="PNG")
    st.image(image_buffer.getvalue(), caption="QR code", width=220)
