import chromadb
from sentence_transformers import SentenceTransformer

# Initialize the ChromaDB client
client = chromadb.HttpClient(host='localhost', port=8000)

# Test if the service is up and running
print(client.heartbeat())

# Check if the collection 'matrix' already exists or create it if it does not exist
collection_name = "matrix"
try:
    matrix_collection = client.get_collection(collection_name)
    print(f"Collection '{collection_name}' already exists.")
except Exception as e:
    if "does not exist" in str(e):
        try:
            # Create the collection if it does not exist
            matrix_collection = client.create_collection(name=collection_name)
            print(f"Collection '{collection_name}' created.")
        except Exception as create_e:
            print(f"Error creating collection: {create_e}")
            matrix_collection = None
    else:
        print(f"Error checking collection: {e}")
        matrix_collection = None

if matrix_collection:
    # Define documents, metadatas, and ids
    documents = [
        "Matrix es una película de ciencia ficción de 1999.",
        "Neo es el protagonista de Matrix.",
        "La película fue dirigida por las hermanas Wachowski.",
        "Matrix explora temas filosóficos y tecnológicos.",
        "Trinity es uno de los personajes principales.",
        "Matrix se desarrolla en un futuro distópico.",
        "La trilogía de Matrix incluye Matrix, Matrix Reloaded y Matrix Revolutions.",
        "El Agente Smith es el antagonista principal de la serie.",
        "La película es conocida por sus innovadores efectos visuales.",
        "Matrix ha tenido una gran influencia en la cultura popular."
    ]

    metadatas = [
        {"doc": "cine"},
        {"doc": "personajes"},
        {"doc": "directores"},
        {"doc": "temas"},
        {"doc": "personajes"},
        {"doc": "ambientación"},
        {"doc": "películas"},
        {"doc": "antagonistas"},
        {"doc": "efectos"},
        {"doc": "influencia"}
    ]

    ids = ["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9", "id10"]

    # Load a pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Create embeddings for the documents
    embeddings = model.encode(documents).tolist()

    # Add the documents with embeddings to the collection
    try:
        matrix_collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings
        )
    except Exception as add_e:
        print(f"Error adding documents: {add_e}")

    # Verify the addition by retrieving the documents
    for doc_id in ids:
        try:
            doc = matrix_collection.get(doc_id)
            print(f"Document {doc_id}: {doc}")
        except Exception as get_e:
            print(f"Error retrieving document {doc_id}: {get_e}")
else:
    print("No se pudo crear ni obtener la colección 'matrix'.")
