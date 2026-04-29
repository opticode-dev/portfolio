import streamlit as st

#タイトル表示
st.title("My portfolio")

#プロフィール
st.header("About Me")
st.write("情報系学生/Webアプリいくつか自作")

#取得済み□
st.header("Certifications")
st.write("ITパスポート")
st.write("基本情報技術者")
st.write("英検２級")

st.header("Interests")
st.write("Webアプリ開発を中心に取り組みつつ、今後は幅広い分野に挑戦し、自分の得意領域を深めていきたいと考えています。")

st.header("Background")
st.write("情報系学生として学習を進めながら、PythonとStreamlitを用いたWebアプリ開発に取り組んでいます。")
st.write("制作したアプリは実際に友人へ使ってもらい、改善を重ねています。")

st.header("Strengths")
st.write("継続的に改善を重ねる")
st.write("実際に人に使ってもらいフィードバックを反映できる")
st.write("目的から逆算して行動できる")
st.write("新しいことにも抵抗なく取り組める")
st.write("集中力が高い")

st.header("Parsonality")
st.write("物事を整理しながら、着実に進めるタイプです。")


#制作物紹介とGithubリンクとStreamlitで作ったアプリのリンク
st.header("Projects")

st.subheader("Project１")
st.write("履修優先度表示アプリ")
st.write("大学の履修登録時に優先度を整理できるアプリです。")
st.link_button("Githubを見る","https://github.com/opticode-dev/risyutekisei")
st.link_button("アプリを見る","https://risyutekisei-iue8jkluryyopnwd4pnh2s.streamlit.app/")

st.subheader("Project２")
st.write("バスの時刻表検索アプリ")
st.write("日にちと出発地点を選択すれば時刻表の一覧が表示されるアプリです。")
st.link_button("Githubを見る","https://github.com/opticode-dev/bus-app")
st.link_button("アプリを見る","https://bus-app-xnyjutwhlx3sjxdwbrpe8u.streamlit.app/")

#学習中
st.header("Learning Now")

st.subheader("Development/IT Skills")
st.write("上記アプリのUI/UX改善")
st.write("HTML/CSSの学習")
st.write("応用情報技術者試験の学習")

st.subheader("Languages")
st.write("韓国語能力試験の学習")
st.write("TOEIC600~")

st.subheader("Business Skills")
st.write("MOSのWord/Excelの学習")

st.subheader("Others")
st.write("随時ポートフォリオ更新中・・・")
st.link_button("Githubを見る","https://github.com/opticode-dev/portfolio")
