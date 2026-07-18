import tkinter as tk
from tkinter import ttk
import joblib

# Load model
model = joblib.load("language_detector.pkl")

def detect_language():
    text = text_box.get("1.0", tk.END).strip()

    if text == "":
        result_label.config(text="Please enter some text.")
        confidence_label.config(text="")
        return

    probs = model.predict_proba([text])[0]

    idx = probs.argmax()

    language = model.classes_[idx]

    confidence = probs[idx] * 100

    result_label.config(
        text=f"Detected Language: {language}"
    )

    confidence_label.config(
        text=f"Confidence: {confidence:.2f}%"
    )


def clear():
    text_box.delete("1.0", tk.END)
    result_label.config(text="")
    confidence_label.config(text="")


root = tk.Tk()

root.title("Offline Language Detector")

root.geometry("600x450")

root.resizable(False, False)

title = tk.Label(
    root,
    text="🌍 Offline Language Detector",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)

text_box = tk.Text(
    root,
    height=7,
    width=55,
    font=("Arial", 12)
)

text_box.pack()

btn = ttk.Button(
    root,
    text="Detect Language",
    command=detect_language
)

btn.pack(pady=15)

clear_btn = ttk.Button(
    root,
    text="Clear",
    command=clear
)

clear_btn.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=20)

confidence_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)

confidence_label.pack()

root.mainloop()