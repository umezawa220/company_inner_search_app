# make_faiss_index.py
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import constants as ct
from initialize import load_data_sources, adjust_string
import pandas as pd
from langchain.docstore.document import Document

load_dotenv()

# CSVデータの整形関数
def load_csv_as_documents(path):
    df = pd.read_csv(path, encoding="utf-8")
    docs = []

    for _, row in df.iterrows():
        content = f"""
        以下は社員情報です。
        社員ID: {row['社員ID']}
        氏名: {row['氏名（フルネーム）']}
        性別: {row['性別']}
        生年月日: {row['生年月日']}
        年齢: {row['年齢']}
        メールアドレス: {row['メールアドレス']}
        従業員区分: {row['従業員区分']}
        入社日: {row['入社日']}
        部署: {row['部署']}
        役職: {row['役職']}
        スキルセット: {row['スキルセット']}
        """
        doc = Document(page_content=content.strip(), metadata={"source": path})
        docs.append(doc)
    return docs

# CSV（社員名簿）の読み込み
docs_csv = load_csv_as_documents("data/社員について/社員名簿.csv")

# その他データ読み込み
docs_all = load_data_sources()
docs_all.extend(docs_csv)

# CSVをドキュメントとして読み込む
csv_docs = load_csv_as_documents("data/社員について/社員名簿.csv")
docs_all.extend(csv_docs)

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
db.save_local("faiss_index")