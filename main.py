import streamlit as st
import pandas as pd

st.header("물품조사 페이지", divider='rainbow')

# 데이터프레임 처리
df = pd.read_excel('items_test.xlsx')

with st.expander('expn_1', expanded=False):
    st.dataframe(df, width=3000, height=500)

# 에디트 테이블
with st.expander('expn_2', expanded=True):
    result = st.data_editor(df, num_rows='dynamic')

# 저장 버튼
if st.button('저장'):
    result.to_excel('items_test.xlsx', index=False)
    st.success('저장 완료')