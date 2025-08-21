import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.data.find("sentiment/vader_lexicon.zip")

class TextProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.sia = SentimentIntensityAnalyzer()
        self.weapons_list = []
        with open("data/weapons.txt") as f:
            self.weapons_list = [line.strip().lower() for line in f.readlines()]

    def rarest_word(self, text):
        words = text.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        return min(words, key=lambda x: freq[x])

    def detect_weapons(self, text):
        text_lower = text.lower()
        for weapon in self.weapons_list:
            if weapon in text_lower:
                return weapon
        return ""

    def sentiment_label(self, text):
        score = self.sia.polarity_scores(text)['compound']
        if score >= 0.5:
            return "positive"
        elif score <= -0.5:
            return "negative"
        else:
            return "neutral"

    def process(self):
        self.df["rarest_word"] = self.df["original_text"].apply(self.rarest_word)
        self.df["sentiment"] = self.df["original_text"].apply(self.sentiment_label)
        self.df["weapons_detected"] = self.df["original_text"].apply(self.detect_weapons)
        return self.df