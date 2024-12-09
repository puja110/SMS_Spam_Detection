# SMS Spam Detection

This project aims to develop an SMS Spam Detection System using machine learning, categorising messages as "spam" or "ham" This system checks the textual content of the message to filter unwanted spam messages from legitimate messages. This implements Naive Bayes (MultinomialNB), TF-IDF vectorization, RandomForestClassifier, and GridSearchCV to achieve high accuracy in detecting spam SMS.

- Research Paper: https://ieeexplore.ieee.org/document/10533895
- Dataset Source: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

# Steps <br/>

1. Data cleaning: Handled missing values, dropped irrelevant columns, and performed basic preprocessing.
2. Exploratory data analysis (EDA): Visualize and analyze data distributions, target classes, and basic statistics.
3. Text Preprocessing:

- Lower case
- Tokenization
- Removing special characters
- Removing stop words and punctuation
- Stemming

5. Model building: Build a classification model using Multinomial Naive Bayes with TF-IDF features
6. Model Evaluation: Evaluated the model using metrics like accuracy and precision.
7. Mobel Performance Improvement: Used feature selection and stacking to improve the model.
8. Hyperparameter Tuning: Used GridSearchCV to search over a hyperparameter grid, tuning the alpha parameter for Multinomial Naive Bayes.
9. Model Testing: Tested the model on existing and new data
10. User Interface: Created a simple webpage to test SMS
11. Deploy on the local server: Deployed the model on a local web server using Flask

# Installation

1. Clone the repository:
   https://github.com/puja110/SMS_Spam_Detection.git

2. Go inside the project folder:
   cd SMS_Spam_Detection

3. Install the required dependencies:
   pip install -r requirements.txt

# Usage

1. Start the Flask server:

- Open your terminal and navigate to the directory where your app.py is located.
- Run the following command to start the server:
  python app.py

2. Access the web interface in your browser:

- Once the server starts, open your web browser and go to the following URL:
  http://127.0.0.1:5000

3. Enter your SMS:

- Sample: Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed 1000 cash or 5000 prize!

After submitting the message, the result will be displayed on the page, showing whether the message is classified as Spam or Not Spam.

# Result

Existing Model Metrics:
Accuracy: 98.74% <br/>
Precision: 97.0%

Hyperparameter Tuned Model Metrics:
Accuracy: 98.64% <br/>
Precision: 98.44%

# Contribution

1. We tried to explore hyperparameter Tuning using GridSearchCV to improve the existing Model Performance.
   
   <img width="669" alt="hyperparameterGridSearch" src="https://github.com/user-attachments/assets/99f8d3be-daf8-4380-bf97-7d14bc57e033">


3. Additionally, we also added a function to test the spam SMS
   
   <img width="1456" alt="testpredict" src="https://github.com/user-attachments/assets/2505bfb6-bfdf-473b-8570-98eb5724a723">

   
5. Created a web interface using HTML
   
   <img width="910" alt="webpage" src="https://github.com/user-attachments/assets/dc717b77-a9aa-49ee-85bd-8ed360ca64a9">


   
7. Deploy the local server using Flask

   <img width="1502" alt="spamtest" src="https://github.com/user-attachments/assets/ff3c642a-cd89-4318-adab-76ca7e848014">

   <img width="1497" alt="notspamtest" src="https://github.com/user-attachments/assets/e1cf905a-0ad4-4096-aec3-ba582f2d4755">



# Future Extension

1. Test the model on larger and more diverse datasets.
2. Experiment with advanced deep learning architecture like Bi-LSTM to improve the detection accuracy.
3. Extend the model to detect spam in voice messages by integrating speech-to-text.

# References

1. https://www.geeksforgeeks.org/multinomial-naive-bayes/
2. https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=spam+detection+machine+learning&btnG=&oq=spam+detection
3. https://scikit-learn.org/1.5/modules/grid_search.html
4. https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
