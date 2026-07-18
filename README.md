# 🌍 Offline Language Detector

## Description

This project is an offline machine learning application that detects the language of input text.

## Supported Languages

- English 🇬🇧
- Hindi 🇮🇳
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
- No internet required (After setup)

## Run

```bash
pip install -r requirements.txt
python app.py
```
## If it doesn't run then try to download this repository and follow these steps.
- ###Open app.py and edit line "6". 
- ###Now select and edit __*<ins>model = joblib.load("language_detector.pkl")</ins>*__ with __*<ins>model = joblib.load(r"path of language_detector.pkl")</ins>*__.

## Author

__Rudresh Mishra__
