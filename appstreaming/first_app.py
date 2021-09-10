# streamlit import해서 웹 퍼브리싱이 되도록 한다.
import streamlit as st
import numpy as np
import pandas as pd

# 간단한 문자열을 출력
# st.title('안녕하세요. 유헌상입니다.')
# # 데이터프레임 출력하기
# st.write('데이터프레임 구성, 테이블을 만들어 보자.')
# st.write(pd.DataFrame({
#     'column1' : [1,2,3,4], 
#     'column2' : [10,20,30,40]
# }))

# use magic 마법을 부려보자
# """
# # 안녕하세요, 유헌상입니다.
# 데이터 프레임 구성, 테이블을 만들어 보자.
# """

# df = pd.DataFrame({
#     '학번' : [2001, 2002, 2003, 2004],
#     '성     명' : ['홍길동', '춘향이', '갑돌이', '갑순이']
# })
# df

# # Chart와 Map
# # line chart
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['A','B', 'C',]
# )

# st.line_chart(chart_data)

# plot map
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [150, 150] +[36.644361, 127.487274],
    columns = ['lat', 'lon']
)
st.map(map_data)