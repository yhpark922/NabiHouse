import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

#데이타 크롤링함수
def get_exchange_rate_data(currency_code, last_page_num):
    # base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.naver"

    df = pd.DataFrame()
    
    for page_num in range(1, last_page_num+1):
        url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{currency_code}KRW&page={page_num}"
        
        dfs = pd.read_html(url, header=1,encoding='cp949')
        
        # 통화 코드가 잘못 지정됐거나 마지막 페이지의 경우 for 문을 빠져나옴
        if dfs[0].empty:
            if (page_num==1):
                print(f"통화 코드({currency_code})가 잘못 지정됐습니다.")
            else:
                print(f"{page_num}가 마지막 페이지입니다.")
            break
            
        # page별로 가져온 DataFrame 데이터 연결
        df = pd.concat([df, dfs[0]], ignore_index=True)
        time.sleep(0.1) # 0.1초간 멈춤
        
    return df
# -----------------------------------------------------------------------------

def exchange_main():

    st.subheader("환율정보를 가져오는 웹 앱")
    # 딕셔널리 통화정보
    currency_name_dict={"미국 달러":"USD","유럽연합 유로":"EUR", "일본 엔화":"JPY", "영국 파운드":"GBP"}

    #콤보상자 작성
    currency_name = st.selectbox("통화선택", currency_name_dict.keys())
    clicked = st.button("환율 데이터 가져오기")

    select_currency_code = currency_name_dict[currency_name]
    last_page = 10

    if clicked:

        #환율 크롤링
        df_exchange = get_exchange_rate_data(select_currency_code, last_page)

        #원하는 열만 선택
        df_exchange_rate = df_exchange[['날짜','매매기준율','사실 때','파실 때','보내실 때','받으실 때']]
        df_exchange_rate=df_exchange_rate.set_index(['날짜'])

        #환율데이터 표시
        st.dataframe(df_exchange_rate)

        #챠트그리기(선그래프, 판다스이용)
        df_exchange_rate_2= df_exchange_rate.copy()
        df_exchange_rate_2.index = pd.to_datetime(df_exchange_rate_2.index)

        ax = df_exchange_rate_2['매매기준율'].plot(figsize=(15,5))
        ax.set_title("Exchange Rate Graph", fontsize = 15)
        ax.set_ylabel(f'Won/{select_currency_code}')
        fig = ax.get_figure() #챠트객체로 변환
        st.pyplot(fig)

        st.subheader("== 환율 데이터 다운로드 ==")
        csv_data = df_exchange_rate.to_csv()
        #엑셀 데이터로 변환
        excel_data = BytesIO() #메모리 버퍼에 바이너리 객체 생성
        df_exchange.to_excel(excel_data)

        col = st.columns(2)
        with col[0]:
            st.download_button("csv 파일 다운로드",csv_data, file_name = 'exchange_rate_data..csv')
        with col[1]:
            st.download_button("엑셀 파일 다운로드",excel_data,file_name = 'exchange_rate_data.xlsx')

if __name__ == "__main__":
    exchange_main()

