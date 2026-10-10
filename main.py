import qrcode
import tkinter as tk
from tkinter import ttk
from urllib.parse import quote

###ADD
#URL ENCODED EMOJIS?
#LETERS FROM THREEMA CODE ALWAYS BIG

#check active field
def update_input_fields():
    messenger = messenger_var.get()
    if messenger == "Threema":
        contact_id_entry.config(state=tk.NORMAL)
        phone_entry.config(state=tk.DISABLED)
    else:
        contact_id_entry.config(state=tk.DISABLED)
        phone_entry.config(state=tk.NORMAL)

#check max. characters
def update_char_count(event=None):
    char_count = len(Imessage_text.get("1.0", tk.END)) - 1  # -1 for newline
    if char_count > 500:
        Imessage_text.delete("500", tk.END)
        char_count = 500
    char_count_label.config(text=f"Characters: {char_count}/500")

# Create URL
def create_url():
    Messenger = messenger_var.get()
    ContactID = contact_id_entry.get()
    PhoneNumber = phone_entry.get()
    InputText = Imessage_text.get("1.0", tk.END).strip()
    
    # Percent-encode. 'safe' controls which characters are left unencoded.
    # By default, quote() encodes everything except letters, digits, '_.-~'.
    URLMessage = quote(InputText, safe="")
    #print("Percent-encoded:", OutputText)

    #create link according to messenger
    match Messenger:
        case "Threema":
            Link = f"https://threema.id/{ContactID}?text={URLMessage}"
        case "WhatsApp":
            Link =f"https://wa.me/{PhoneNumber}?text={URLMessage}"
        case "Signal":
            Link = f"https://signal.me/#p/{PhoneNumber}"

    # show the generated link in the output text widget
    Omessage_text.delete("1.0", tk.END)
    Omessage_text.insert(tk.END, Link)

#create QR Code
def create_qr():
    QRText = Omessage_text.get("1.0", tk.END).strip()
    if QRText == "":
        QRText = "Sorry, no URL generated yet!"

    img = qrcode.make(QRText)
    type(img)
    img.show("myQR.png")

# Create main window
root = tk.Tk()
root.title("Click Message")
root.geometry("500x800")

# Title
title_label = tk.Label(root, text="Click Message", font=("Arial", 14, "bold"))
title_label.pack(pady=3)

# Frame for form
form_frame = ttk.Frame(root, padding="20")
form_frame.pack(fill=tk.BOTH, expand=True)

# Messenger Selection (Radio Buttons)
messenger_label = tk.Label(form_frame, text="Choose Messenger:", font=("Arial", 11, "bold"))
messenger_label.pack(anchor=tk.W, pady=(10, 3))

messenger_var = tk.StringVar(value="Threema")
# show the radio buttons horizontally and ensure the values match create_url
messengers = [("Threema", "Threema"), ("WhatsApp", "WhatsApp"), ("Signal", "Signal")]

messenger_radio_frame = tk.Frame(form_frame)
messenger_radio_frame.pack(anchor=tk.W, pady=(0, 3), padx=20)

for label, value in messengers:
    radio_btn = tk.Radiobutton(messenger_radio_frame, text=label, variable=messenger_var, value=value, command=update_input_fields)
    radio_btn.pack(side=tk.LEFT, padx=10)


# Contact ID Input
contact_id_label = tk.Label(form_frame, text="Contact ID:", font=("Arial", 11, "bold"))
contact_id_label.pack(anchor=tk.W, pady=(12, 3))
contact_id_entry = tk.Entry(form_frame, width=40)
contact_id_entry.insert(0, "A1B2C3D4")
contact_id_entry.pack(anchor=tk.W, padx=20, pady=3)

# Phone Number Input
phone_label = tk.Label(form_frame, text="Phone Number:", font=("Arial", 11, "bold"))
phone_label.pack(anchor=tk.W, pady=(15, 3))
phone_entry = tk.Entry(form_frame, width=40)
phone_entry.insert(0,"12345678")
phone_entry.pack(anchor=tk.W, padx=20, pady=3)

# Check active input field
update_input_fields()

# Message Text Box for Input with character counter
Imessage_label = tk.Label(form_frame, text="Message (max. 500 characters):", font=("Arial", 11, "bold"))
Imessage_label.pack(anchor=tk.W, pady=(15, 5))

Imessage_frame = tk.Frame(form_frame)
Imessage_frame.pack(anchor=tk.W, padx=20, pady=5)

Imessage_text = tk.Text(Imessage_frame, width=50, height=8, wrap=tk.WORD)
Imessage_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Character counter
char_count_label = tk.Label(form_frame, text="Characters: 0/500", font=("Arial", 9))
char_count_label.pack(anchor=tk.W, padx=20, pady=5)

Imessage_text.bind("<KeyRelease>", update_char_count)

# Message Text Box for Output
Omessage_label = tk.Label(form_frame, text=f"Your URL:", font=("Arial", 11, "bold"))
Omessage_label.pack(anchor=tk.W, pady=(15, 5))

Omessage_frame = tk.Frame(form_frame)
Omessage_frame.pack(anchor=tk.W, padx=20, pady=5)

Omessage_text = tk.Text(Omessage_frame, width=50, height=8, wrap=tk.WORD)
Omessage_text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

#Buttons
submit_btnURL = tk.Button(form_frame, text="Generate URL", command=create_url, bg="#4CAF50", fg="white", font=("Arial", 11), padx=10, pady=10)
submit_btnURL.pack(side=tk.LEFT, pady = 0)

submit_btnQR = tk.Button(form_frame, text="Generate QR Code", command=create_qr, bg="#4CAF50", fg="white", font=("Arial", 11), padx=30, pady=10)
submit_btnQR.pack(side=tk.RIGHT, pady = 0)

# Start the GUI
root.mainloop()