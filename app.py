from flask import Flask, render_template, request
import pickle
import streamlit as st
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__, template_folder='View')

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Define a function to preprocess the text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []

    for i in text:
        if i.isalnum():
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(ps.stem(i))
    return " ".join(y)


# Load the TF-IDF vectorizer and the model
tfidf = pickle.load(open('Model/vectorizer.pkl', 'rb'))
model = pickle.load(open('Model/model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def spamDetect():
    if request.method == 'POST':
        try:
            input_sms = request.form['text'] 
            # Preprocess the input message
            transformed_sms = transform_text(input_sms)

            # Use the vectorizer to transform the input
            processed_text = tfidf.transform([transformed_sms])

            # Use the trained model to make a prediction
            spam_status = model.predict(processed_text)[0]

            # Display the prediction result
            if spam_status == 1:
                result = "Spam"
            else:
                result = "Not Spam"

            return render_template('index.html', spam_status=result)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)