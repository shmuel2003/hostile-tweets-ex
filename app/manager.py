from fetcher import MongoFetcher
from processor import TextProcessor

class AppManager:
    def __init__(self):
        self.fetcher = MongoFetcher()
        self.processor = None

    def run_pipeline(self):
        df = self.fetcher.fetch_all()
        self.processor = TextProcessor(df)
        processed_df = self.processor.process()
        return processed_df.to_dict(orient="records")