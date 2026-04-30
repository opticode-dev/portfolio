import streamlit as st

#タイトル表示
st.title("My portfolio")

#プロフィール
st.header("About Me")
st.write("情報系学生")
st.write("PythonとStreamlitを用いたWebアプリ開発に取り組んでいる")
st.write("実際に使ってもらった意見をもとに改善を重ねる開発スタイル")
st.write("物事を整理しながら着実に進めるタイプ")

#強み
st.header("Strengths")
st.write("継続的に改善を重ねる")
st.write("実際に人に使ってもらいフィードバックを反映できる")
st.write("目的から逆算して行動できる")
st.write("新しいことにも抵抗なく取り組める")
st.write("集中力が高い")

#取得済み資格
st.header("Certifications")
st.write("ITパスポート")
st.write("基本情報技術者")
st.write("英検２級")

#興味
st.header("Interests")
st.write("Webアプリ開発を中心に、UI/UX改善・業務効率化・幅広い技術分野に興味がある")

#制作物紹介とGithubリンクとStreamlitで作ったアプリのリンク
st.header("Projects")

st.subheader("Project１")
st.write("履修優先度表示アプリ")
st.write("大学の履修登録時に優先度を分析し、グラフと表を表示")
st.link_button("Githubを見る","https://github.com/opticode-dev/risyutekisei")
st.link_button("アプリを見る","https://risyutekisei-iue8jkluryyopnwd4pnh2s.streamlit.app/")

st.subheader("Project２")
st.write("バスの時刻表検索アプリ")
st.write("日にちと出発地点を選択すれば時刻表の一覧を表示")
st.link_button("Githubを見る","https://github.com/opticode-dev/bus-app")
st.link_button("アプリを見る","https://bus-app-xnyjutwhlx3sjxdwbrpe8u.streamlit.app/")

#開発・改善ログ
st.header("Development Log")
st.write("2026/03 履修優先度アプリ作成")
st.write("2026/03 バスの時刻表検索アプリ作成")
st.write("2026/04 履修優先度アプリ改善")
st.write("2026/04 ポートフォリオ公開")
st.write("2026/04 韓国語学習本格始動")

st.write("2026/05 HTML/CSS学習開始予定")
st.write("2026/05 お金管理アプリ公開予定")
st.write("2026/05 TOEIC学習開始予定")

st.write("2026/11 応用情報技術者試験受験予定")
st.write("2026/12 MOS Excel/Word受験予定")

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
