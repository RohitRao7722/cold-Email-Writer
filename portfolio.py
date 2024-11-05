import pandas as pd
import faiss
import numpy as np
import uuid

class Portfolio:
    def __init__(self, file_path="E:\\imp_data\\codes\\cold email generator\\resources\\my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        
        # Metadata storage for links associated with each document ID
        self.metadata_store = {}
        
        # Initialize FAISS index and load portfolio data
        self.index = None
        self.load_portfolio()

    def load_portfolio(self):
        tech_stacks = self.data['Techstack'].tolist()
        self.embeddings = self.get_embeddings(tech_stacks)  # Generate embeddings for tech stacks
        
        # Initialize FAISS index for L2 similarity (euclidean distance)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])  # 128-dimensional vectors
        self.index.add(self.embeddings)
        
        # Store metadata (links) by document ID
        for i, row in self.data.iterrows():
            doc_id = i  # Use row index as document ID
            self.metadata_store[doc_id] = row["Links"]

    def get_embeddings(self, tech_stacks):
        # Here you would convert tech stack text to embeddings
        # Using dummy 128-dimensional random vectors for demonstration
        return np.random.rand(len(tech_stacks), 128).astype('float32')

    def query_links(self, skills, n_results=2):
        # Convert skills into a query embedding
        query_embedding = self.get_embeddings([skills])[0].reshape(1, -1)
        
        # Perform similarity search
        _, indices = self.index.search(query_embedding, n_results)
        
        # Retrieve corresponding links from metadata
        results = [self.metadata_store[idx] for idx in indices[0] if idx in self.metadata_store]
        return results
