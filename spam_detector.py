import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data():
    data = {
        'text': [
            'Get a free gift card now!', 'Hey, are we still meeting for lunch?',
            'WINNER! You have won a prize, claim now.', 'Can you send me the files?',
            'Urgent: Your account has been compromised.', 'Hope you are doing well.',
            'CONGRATULATIONS! You won $1000.', 'Let me know when you are free.',
            'Free entry into the contest.', 'I will call you back later.'
        ],
        'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def train_model():
    df = load_data()
    X = df['text']
    y = df['label']

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    joblib.dump(model, 'spam_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    
    return model, vectorizer

def predict_message(message):
    model = joblib.load('spam_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    
    message_vec = vectorizer.transform([message])
    prediction = model.predict(message_vec)
    
    return "SPAM" if prediction[0] == 1 else "HAM (Legit)"

if __name__ == "__main__":
    train_model()
    test_msg = "Claim your free prize now by clicking here!"
    print(f"Testing Message: '{test_msg}'")
    print(f"Prediction: {predict_message(test_msg)}")