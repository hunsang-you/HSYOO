## 차트에 상호작용이 가능하도록 함
# streamlit import해서 웹 퍼브리싱이 되도록 한다.
import streamlit as st
import numpy as np
import pandas as pd
import time
# checkbox 이용, show/hide data
if st.checkbox('Show Data Frame'):
    chart_data = pd.DataFrame(
        np.random.rand(20, 3),
        columns = ['A', 'B', 'C']
    )

    chart_data

st.write('interactivity with widget...')

df = pd.DataFrame({
    'number' : [1, 2, 3, 4, 5],

})


# # 옵션 선택을 위한 selectbox
# option = st.selectbox(
#     '좋아하는 숫자는? ', 
#     df['number']
# )

# '선택 결과 : ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['number'])

'You selected:', option

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'