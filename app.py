import streamlit as st
import joblib

st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📩 SMS Spam Detector")
st.write("Koi bhi message paste karo, model batayega ki spam hai ya nahi.")

msg = st.text_area("Message likho:", height=150)

if st.button("Check karo"):
    if msg.strip() == "":
        st.warning("Pehle koi message likho.")
    else:
        X = vectorizer.transform([msg])
        pred = model.predict(X)[0]
        spam_prob = model.predict_proba(X)[0][1]

        if pred == 1:
            st.error(f"🚨 SPAM (confidence: {spam_prob*100:.1f}%)")
        else:
            st.success(f"✅ Not Spam (spam probability: {spam_prob*100:.1f}%)")

st.caption("Model: TF-IDF + Naive Bayes | Trained on English SMS data, isliye Hinglish spam pe kamzor hai.")
