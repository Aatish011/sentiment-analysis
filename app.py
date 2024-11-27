from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment_category = 'Positive'
        color = 'green'
    elif polarity < 0:
        sentiment_category = 'Negative'
        color = 'red'
    else:
        sentiment_category = 'Neutral'
        color = 'yellow'
    
    return sentiment_category, color

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    color = None

    # Check for POST request (form submission)
    if request.method == 'POST':
        text = request.form.get('text', '')  # Get text input from form
        if text.strip():  # Only process non-empty input
            sentiment, color = analyze_sentiment(text)
    
    # Pass sentiment and color to the HTML template
    return render_template('index.html', sentiment=sentiment, color=color)

if __name__ == '__main__':
    app.run(debug=True)



