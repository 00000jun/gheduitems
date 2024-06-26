import streamlit as st
import pandas as pd

st.header("물품조사 페이지", divider='rainbow')

# 데이터프레임 처리
df = pd.read_excel('items_test.xlsx')


# 이미지 url 처리
url_df = pd.read_table('result_imges_url.txt', header=None) # 이미지 url txt 파일 불러오기
url_df = url_df[0]

code_list = [] # 물품목록번호 리스트
img_url_list = [] # 이미지주소 리스트

for line in url_df:
    code, url = line.split(' : ') # 물품목록번호와 이미지주소 분리
    code_list.append(code)
    img_url_list.append(url)

pre_url_df = pd.DataFrame({'물품목록번호': code_list, '이미지주소': img_url_list}) # (물품목록번호, 이미지주소) 데이터프레임 생성


# 데이터프레임 병합 : 물품목록번호를 기준으로 이미지주소를 병합
merged_df = pd.merge(df, pre_url_df, on='물품목록번호', how='left')


# 데이터프레임 후처리 (컬럼 인덱싱)
merged_df = merged_df[['순','운용부서','이미지주소', '물품목록번호', '물품분류명', '품명규격', '등록수량', '검수수량']]


# 처리 후 데이터프레임
with st.expander('검수용 데이터프레임', expanded=True):
    # 데이터프레임 출력
    result = st.data_editor(
        merged_df,
        column_config={
            "이미지주소": st.column_config.ImageColumn(
                "미리보기", help="클릭시 확대"
            )
        },
        num_rows='dynamic',
        width=3000,
        height=400,
        )


# 저장 버튼
if st.button('저장', help='검수수량 입력 후 저장 버튼을 누르면 데이터 저장'):
    result.to_excel('items_test.xlsx', index=False)
    st.success('저장 완료')
