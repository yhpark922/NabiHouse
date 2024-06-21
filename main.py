import streamlit as st
from PIL import Image
import exchange_rate

#사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input('아디디 입력', value = '', max_chars=15)
user_password = st.sidebar.text_input('페스워드 입력', value = "", type='password')

if user_id == "id" and user_password == "1234":
    st.sidebar.header("영훈의 포트폴리오")
    # sel_options = ["",'진주 귀걸이를 한 소녀','별이 빛나는 밤','절규','생명의 나무','월하정인']
    # user_opt = st.sidebar.selectbox("좋아하는 작품은", sel_options, index=0)
    # st.sidebar.write("**선택한 그림은", user_opt)
    
    menu = st.sidebar.radio('메뉴 선택',['환율 조회', '부동산 조회(EDA)', '인공지능 예측/분류'],index=None)

    if menu == '환율 조회':
        exchange_rate.exchange_main()
        st.sidebar.write('환율 조회')
        
    elif menu == '부동산 조회(EDA)':
        st.sidebar.write('부동산 조회(EDA)')
    elif menu == '인공지능 예측/분류':
        st.sidebar.write('인공지능 예측/분류')
    else:
        st.sidebar.write('메뉴를 선택해 주세요')



    #메인화면

    # st.subheader("나 만의 그림 목록")


    # image_files = ["welcome.jpg",'Vermeer.png','Gogh.png','Munch.png','Klimt.jpg','ShinYoonbok.png']
    # sel_index = sel_options.index(user_opt)
    # img_file = image_files[sel_index]
    # img_local = Image.open(f"img/{img_file}")
    # st.image(img_local, caption = user_opt)

    #pip list --format=freeze > requirements.txt