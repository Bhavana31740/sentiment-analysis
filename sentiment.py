import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv(
    "Amazon_Reviews.csv",
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)

# Sentiment Function
def get_sentiment(text):

    score = TextBlob(str(text)).sentiment.polarity

    if score > 0:
        return "Positive"

    elif score < 0:
        return "Negative"

    else:
        return "Neutral"

# Apply Sentiment Analysis
df["Sentiment"] = df["Review Text"].apply(get_sentiment)

# Display Results
print(df[["Review Text", "Sentiment"]].head())

print("\nSentiment Counts:")
print(df["Sentiment"].value_counts())

import matplotlib.pyplot as plt

df["Sentiment"].value_counts().plot(kind="bar")

plt.title("Amazon Review Sentiments")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()

df["Sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sentiment Distribution")
plt.ylabel("")

plt.show()