import os
import chromadb

client = chromadb.PersistentClient(path="./chromaDemo")
collection = client.get_collection(name="ExampleText")


with open(os.path.join('../data', 'Elon.txt'), 'r') as f:
    text = f.read()
with open(os.path.join('../data', 'Henry.txt'), 'r') as f:
    text2 = f.read()

collection.add(
    documents=[text, text2],
    metadatas=[{"source": "Elon"}, {"source": "Henry"}],
    ids=["Elon", "Henry"],
)

results = collection.query(
    query_texts=["When did Musk establish xAI"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # 可选过滤器
    # where_document={"$contains":"search_string"}  # 可选过滤器
)
print(results)

