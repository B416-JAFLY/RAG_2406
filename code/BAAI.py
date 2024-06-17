from sentence_transformers import SentenceTransformer

# 下载模型
model = SentenceTransformer('BAAI/bge-small-en-v1.5')
# 保存模型到指定路径
model.save('../BAAI/bge-small-en-v1.5')
