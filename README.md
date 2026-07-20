# Amazon Reviews - Sentiment Analysis

A sentiment analysis project that classifies Amazon customer reviews as **Positive**, **Negative**, or **Neutral** using Python and TextBlob, then visualizes the results.

## Contents
- `Amazon_Reviews_Sentiment_Analysis.ipynb` — the analysis notebook, with a markdown explanation before every step
- `Amazon_Reviews.csv` — the dataset (must stay in the same folder as the notebook)

## What's inside
- Loading messy real-world CSV data (handling encoding issues and bad rows)
- Building a simple polarity-based sentiment classifier with TextBlob
- Applying it across every review in the dataset
- Visualizing sentiment distribution with a bar chart and a pie chart

## Key result
- ~50% of reviews are Positive
- ~39.3% of reviews are Negative
- ~10.6% of reviews are Neutral

## How to run
1. Clone this repo
2. Make sure `Amazon_Reviews.csv` is in the same folder as the notebook
3. Install dependencies (see below)
4. Open `Amazon_Reviews_Sentiment_Analysis.ipynb` in Jupyter Notebook / JupyterLab / VS Code
5. Run all cells top to bottom

## Requirements
```
pandas
textblob
matplotlib
```
Install with:
```
pip install pandas textblob matplotlib
python -m textblob.download_corpora
```
