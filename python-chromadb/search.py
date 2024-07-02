import warnings
warnings.filterwarnings("ignore", message="Found Intel OpenMP.*")

import chromadb
from sentence_transformers import SentenceTransformer
import argparse

# Configurar argparse para manejar los argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Buscar en la colección de Matrix.')
parser.add_argument('query', type=str, help='La consulta de búsqueda')
parser.add_argument('--n_results', type=int, default=5, help='Número de resultados a devolver')

args = parser.parse_args()

# Initialize the ChromaDB client
client = chromadb.HttpClient(host='localhost', port=8000)

# Test if the service is up and running
print(client.heartbeat())

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create an embedding for the query
query_embedding = model.encode([args.query]).tolist()

# Perform the search
try:
    matrix_collection = client.get_collection("matrix")
    results = matrix_collection.query(
        query_embeddings=query_embedding,
        n_results=args.n_results
    )
    print("Search Results:")
    for i in range(len(results['documents'])):
        print(f"Document ID: {results['ids'][i]}")
        print(f"Document: {results['documents'][i]}")
        print(f"Metadata: {results['metadatas'][i]}")
        print(f"Distance: {results['distances'][i]}")
        print()
except Exception as e:
    print(f"Error performing search: {e}")
