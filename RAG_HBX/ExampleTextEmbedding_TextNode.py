import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 读取文档
with open(os.path.join('../data', 'Elon.txt'), 'r') as f:
    text = f.read()

# 2. 初始化解析器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=64, chunk_overlap=2, add_start_index=True
)

# 3. 将文档解析为文本节点
doc=text_splitter.create_documents([text])
all_splits = text_splitter.split_documents(doc)
print(len(all_splits))
print(all_splits[0])

# 4. 初始化ChromaDB客户端
client = chromadb.PersistentClient(path="./chromaDemo")
collection = client.get_collection(name="ExampleText")

# 5. 准备文本块和元数据
texts = [split.page_content for split in all_splits]
metadatas = [split.metadata for split in all_splits]
ids = [f"node_{i}" for i in range(len(all_splits))]
#
# 6. 添加文本块到ChromaDB
collection.add(
    documents=texts,
    metadatas=metadatas,
    ids=ids,
)

# 7. 查询文本块
results = collection.query(
    query_texts=["When did Musk establish xAI"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # 可选过滤器
    # where_document={"$contains":"search_string"}  # 可选过滤器
)

print(results)
