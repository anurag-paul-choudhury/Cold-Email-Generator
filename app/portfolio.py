import pandas as pd
import chromadb
import uuid
from chromadb.utils import embedding_functions

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        # Initialize Chroma with a local persistent store
        self.chroma_client = chromadb.PersistentClient(path="vectorstore")

        # Use a simpler embedding function to avoid ONNX/tokenizer issues
        import sentence_transformers
        print("✅ sentence-transformers imported successfully!")

        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2",device="cpu"
        )

        # Create or load collection using that embedding function
        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio",
            embedding_function=self.embedding_function
        )

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        results = self.collection.query(
            query_texts=[skills],
            n_results=2
        )
        return results.get('metadatas', [])
