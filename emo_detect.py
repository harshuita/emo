from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
def detect_emotion(text):
    model_name= 'bhadresh-savani/distilbert-base-uncased-emotion'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    emotion_detection = pipeline(
        'text-classification',
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        truncation=True
    )
    emotion = emotion_detection(text)[0]['label']
    return emotion
