from textblob import TextBlob

def analyze_sentiment(text):
    if not text.strip():  # Check if the text is empty or contains only spaces
        return "Invalid input. Please enter meaningful text."

    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Analyze the sentiment
    sentiment = blob.sentiment
    polarity = sentiment.polarity  # ranges from -1 (negative) to 1 (positive)
    subjectivity = sentiment.subjectivity  # ranges from 0 (objective) to 1 (subjective)
    
    # Determine sentiment category
    if polarity > 0:
        sentiment_category = 'Positive'
    elif polarity < 0:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'
    
    # Display results
    return f"Sentiment: {sentiment_category}\nPolarity: {polarity:.2f}\nSubjectivity: {subjectivity:.2f}"

# Example usage
text = input("Enter your text: ")
result = analyze_sentiment(text)
print(result)
