import pandas as pd
import numpy as np
class DataPrepKit:
    def __init__(self,data):
        self.data=data
    def reader(self,format,path):
        if format=="csv":
            self.data=pd.read_csv(path)
        elif format=="excel":
            self.data=pd.read_excel(path)
        elif format=="json":
            self.data=pd.read_json(path)
    def summarizer(self):
        summary = {
            'Average': self.data.mean(),
            'Most Frequent Values': self.data.mode().iloc[0]
        }
        return summary
    def HMV(self, strategy='remove'):
        if strategy == 'remove':
            self.data = self.data.dropna()
        elif strategy == 'impute':
            self.data = self.data.fillna(self.data.mean()) 
    def encoder(self):
        self.data = pd.get_dummies(self.data)
    def save_data(self,path):
        self.data.to_csv(path, index=False)
dataPrep = DataPrepKit(None)
dataPrep.reader('data.csv', 'csv')
summary = dataPrep.summarizer()
print(summary)