import streamlit as st

st.set_page_config(page_title="変電Webアプリ", layout="centered")

st.title("変電Webアプリ")
st.write("現場業務をサポートするための便利なWebアプリ集です。以下のリンクから各アプリにアクセスできます。")

# GPS情報取得アプリ
st.subheader("📍 GPS情報取得アプリ")
st.write("""
スマートフォンやタブレットの位置情報を取得し、現場の位置記録を簡単に行えるアプリです。
点検や巡視の際に、正確な位置情報を記録することで、報告書作成や履歴管理がスムーズになります。
""")
st.markdown("[GPS情報取得アプリを開く](https://hepconw-henden-app1.streamlit.app/)")

# 巡視カード入力アプリ
st.subheader("📝 巡視カード入力アプリ")
st.write("""
巡視業務の記録を効率化するための入力フォームです。
設備ごとの点検結果や異常の有無を簡単に入力でき、データはCSV形式で保存・管理が可能です。
""")
st.markdown("[巡視カード入力アプリを開く](https://hepconw-henden-app2.streamlit.app/)")
