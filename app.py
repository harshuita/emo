from flask import Flask, render_template,request
from emo_detect import detect_emotion
import pandas as pd
import sqlite3
df=pd.read_csv('main.csv')
conn=sqlite3.connect('lyric_emotion.db')
#df.to_sql('main',conn,if_exists='replace',index=False) 
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')
@app.route('/result', methods=['POST','GET'])
def result():
   if request.method == 'POST':
      text = request.form['inp']
      emotion=detect_emotion(text);
      print(emotion)
   return render_template('result.html',emotion=emotion)
if __name__ == '__main__':
   app.run()

"""
   1) hugging face api - detect emotion 
   2) spotify api calls- playing the song,pause , play n stop (js)
   3) db part - spotify database labelled w emotions sqlite

   1.1) detect emotion of the text
   1.2) detect emotion of song from lyrics- text preprocessing, cleaning of dataset


"""