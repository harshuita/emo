from flask import Flask, render_template,request
from transformers import pipeline
app = Flask(__name__)
sentiment_analysis = pipeline('sentiment-analysis')
@app.route('/')
def home():
   return render_template('index.html')
@app.route('/result', methods=['POST','GET'])
def result():
   if request.method == 'POST':
      text = request.form['inp']
      results = sentiment_analysis(text)
      sentiment = results[0]['label']
   return render_template('result.html')
if __name__ == '__main__':
   app.run()