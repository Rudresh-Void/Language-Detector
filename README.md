# 🌍 Offline Language Detector

## Description

This project is an offline machine learning application that detects the language of input text.

## Supported Languages

- English 🇬🇧
- Hindi 🇮🇳
- French 🇫🇷
- Japanese 🇯🇵

## Technologies

- Python
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Tkinter

## Features

- Offline language detection
- Confidence score
- Simple graphical interface
- No internet required

## Run

```bash
pip install -r requirements.txt
python app.py
```
## If it doesn't run then try to download this repository and follow these steps.
***Step 1 :*** Open app.py and edit line "6", 
***Step 2 :*** Now select and edit **model = joblib.load("language_detector.pkl")** with **model = joblib.load(r"path of language_detector.pkl")**

## Author

Rudresh Mishra
