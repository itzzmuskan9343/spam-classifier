# 📩 SMS Spam Classifier

A machine learning web app that classifies SMS messages as **spam** or **not spam**.

🔗 **Live demo:** https://spam-classifier-muskan2.streamlit.app

## How it works

1. Messages are converted to numbers using **TF-IDF**.
2. A **Multinomial Naive Bayes** classifier predicts spam or ham (not spam).
3. The model is served through a **Streamlit** web app.

## Results

Trained on the UCI SMS Spam Collection (80/20 train-test split).

| Metric | Score |
|---|---|
| Accuracy | 98.65% |
| Spam precision | 99% |
| Spam recall | 91% |

Tuning the smoothing parameter (alpha) from 1.0 to 0.3 raised spam recall from 84% to 91% while keeping precision at 99%.

## Limitations

- Trained on older English SMS data, so it is weaker on **Hinglish spam** and modern phishing messages.
- Next step: add Hinglish and modern phishing examples to the training data.

## Tech stack

Python, scikit-learn, pandas, Streamlit

## Run locally

    pip install -r requirements.txt
    streamlit run app.py
