import chromadb
# 设置Chroma为内存模式，方便原型设计。可以轻松添加持久化功能！
client = chromadb.PersistentClient(path="./chromaDemo")


# 创建集合。还可以使用 get_collection、get_or_create_collection、delete_collection 方法！
collection = client.create_collection("all-my-documents")

# 向集合中添加文档。还可以更新和删除文档。基于行的API即将推出！
collection.add(
    documents=["This is document1", "This is document2"], # 我们自动处理分词、嵌入和索引。您也可以跳过这些步骤，直接添加自己的嵌入
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # 可以根据这些元数据进行过滤！
    ids=["doc1", "doc2"], # 每个文档的唯一标识
)

# 查询/搜索最相似的两个结果。您也可以通过id使用 .get 方法获取
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # 可选过滤器
    # where_document={"$contains":"search_string"}  # 可选过滤器
)
print(results)