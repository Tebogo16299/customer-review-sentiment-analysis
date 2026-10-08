import pandas as pd
from textblob import TextBlob

# Load the customer review dataset
df = pd.read_csv("ecommerce_customer_reviews_raw (1).csv")

# Display the first 5 rows
print(df.head())

# Display dataset shape
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Function to determine sentiment
def get_sentiment(review):
    polarity = TextBlob(str(review)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Customer_Review"].apply(get_sentiment)

# Display reviews with their sentiment
print("\nCustomer Reviews with Sentiment:")
print(df[["Customer_Review", "Sentiment"]].head(10))

# Count each sentiment
print("\nSentiment Summary:")
print(df["Sentiment"].value_counts())

# Sentiment by product category
print("\nSentiment by Product Category:")
category_sentiment = pd.crosstab(
    df["Product_Category"],
    df["Sentiment"]
)

print(category_sentiment)

# Sentiment by customer rating
print("\nSentiment by Customer Rating:")

rating_sentiment = pd.crosstab(
    df["Rating"],
    df["Sentiment"]
)

print(rating_sentiment)

# Save the analyzed data for Power BI
df.to_csv("customer_reviews_powerbi.csv", index=False)

print("\nPower BI file created successfully!")
print("File name: customer_reviews_powerbi.csv")