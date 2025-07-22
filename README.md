# 社内情報特化型 生成AI検索アプリ

本アプリは、Python／Streamlitの基本理解と、生成AIの業務活用方法の習得を目的に作成したものです。  
DMM生成AI CAMPの教材をベースにしつつ、独自にカスタマイズを加えています。

「エンジニアとしての実装力」よりも、
「**業務改善・情報活用をリードするPM的な立場**」としての知見向上を目的としています。
将来的には、社内に点在するナレッジやドキュメントの再利用性を高める仕組みへの応用を見据えています。

---

## 🔍 概要

このアプリは、以下の2機能を備えています：

- **社内文書検索**：社内の議事録や資料データなどから、質問に応じて関連情報を抽出・回答  
- **社員情報検索**：CSV形式で管理されている社員名簿をもとに、社員に関する問い合わせに自動応答

✅ デモ例：
- 「営業部に所属している社員を一覧化して」→ 社員CSVから抽出
- 「2023年3月のMTGで話された内容を表示して」→ 議事録データから回答

---

<details>
<summary>📁 主な構成</summary>

- `Streamlit` によるチャット型UI
- `OpenAI API` を使った文書ベクトル検索（RAG）
- `FAISS` による社内文書ベクトルDB構築
- CSVデータ（社員名簿）読み込み対応

</details>

---

<details>
<summary>🧠 使用技術・ライブラリ</summary>

- `LangChain`：テキスト分割・ベクトルDB連携
- `OpenAI Embeddings`：テキストのベクトル化
- `FAISS`：社内データ検索用ベクトルDB
- `Streamlit`：UI構築用フレームワーク
- `Python`：アプリ全体のベース言語

</details>

---

<details>
<summary>📂 ディレクトリ構成</summary>
├── company_inner_search_app/
│ ├── main.py # Streamlitアプリのメイン
│ ├── initialize.py # データ読み込み・整形
│ ├── constants.py # 各種設定値
│ ├── components.py # Streamlit用UI部品
├── data/
│ ├── 社員について/
│ │ └── 社員名簿.csv # 社員情報CSV
│ └── MTG議事録/ # 複数の社内文書
├── make_faiss_index.py # ベクトルDB作成スクリプト
├── requirements.txt # 必要ライブラリ一覧
</details>

---

<details>
<summary>🚀 使い方</summary>
1. 必要なライブラリをインストール  
   ```bash
   pip install -r requirements.txt
2. 環境変数 .env を作成し、OpenAIのAPIキーを設定
   OPENAI_API_KEY=your-api-key
3. ベクトルDB（FAISS）を作成
   python make_faiss_index.py
4. アプリを起動
   streamlit run company_inner_search_app/main.py
</details>

💡 今後の展望
- 社内議事録や業務マニュアルなど実データでの応用
- Google Workspace や外部ストレージとの連携
- GPTs／Zapierなど他ツールと連動した自動化プロトタイプ展開

👤 作者情報
- GitHub: umezawa220
- 使用目的：業務改善／AI×ナレッジ活用の実践的理解と提案力向上
