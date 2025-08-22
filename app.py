import streamlit as st

st.set_page_config(page_title="変電Webアプリ", layout="centered")

st.title("📱変電Webアプリ🛠️")
st.write("現場業務をサポートするための便利なWebアプリ集です。以下のリンクから各アプリにアクセスできます。")

# アプリ情報のリスト
apps = [
    {
        "title": "GPS情報取得アプリ",
        "description": "スマートフォンやタブレットの位置情報を取得し、現場の位置記録を簡単に行えるアプリです。",
        "url": "https://hepconw-henden-app1.streamlit.app/"
    },
    {
        "title": "巡視カード入力アプリ（テスト）",
        "description": "設備ごとの点検結果や異常の有無を簡単に入力でき、データはCSV形式で保存・管理が可能です。",
        "url": "https://hepconw-henden-app2.streamlit.app/"
    },
    {
        "title": "カメラ撮影＋ラベル合成アプリ【廃止】",
        "description": "スマートフォンやタブレットで写真を撮影し、ラベルを合成するアプリです。仕様上フォーカスやズームといった機能は使えません。",
        "url": "https://hepconw-henden-app3.streamlit.app/"
    },
    {
        "title": "ラベル付き画像生成アプリ",
        "description": "スマートフォンやタブレットで写真を撮影し、ラベルを合成するアプリです。カメラアプリで撮影した画像が使えます。",
        "url": "https://hepconw-henden-app4.streamlit.app/"
    },
    {
        "title": "ガス圧20℃換算アプリ",
        "description": "ガス圧を20℃換算するアプリ。MPa、kg/cm2対応。",
        "url": "https://hepconw-henden-app5.streamlit.app/"
    }
]

# 検索バー
search_query = st.text_input("🔍 アプリ名やキーワードで検索", "")

# 検索結果の表示
for app in apps:
    if search_query.lower() in app["title"].lower() or search_query.lower() in app["description"].lower():
        st.subheader(f"📌 {app['title']}")
        st.write(app["description"])
        st.markdown(f"[アプリを開く]({app['url']})")

# 検索結果がない場合のメッセージ
if search_query and not any(search_query.lower() in app["title"].lower() or search_query.lower() in app["description"].lower() for app in apps):
    st.warning("該当するアプリが見つかりませんでした。別のキーワードを試してください。")
