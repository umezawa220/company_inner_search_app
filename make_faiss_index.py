# make_faiss_index.py
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import constants as ct
from initialize import load_data_sources, adjust_string

load_dotenv()

# データ読み込み
docs_all = load_data_sources()

# Windows調整（省略可）
for doc in docs_all:
    doc.page_content = adjust_string(doc.page_content)
    for key in doc.metadata:
        doc.metadata[key] = adjust_string(doc.metadata[key])

# テキスト分割
splitter = CharacterTextSplitter(
    chunk_size=ct.CHUNK_SIZE,
    chunk_overlap=ct.CHUNK_OVERLAP,
    separator="\n"
)
split_docs = splitter.split_documents(docs_all)

# 埋め込み
embeddings = OpenAIEmbeddings()

# FAISS作成 & 保存
db = FAISS.from_documents(split_docs, embedding=embeddings)
db.save_local("faiss_index")  # ←保存先（git管理 or Cloudにアップ）
