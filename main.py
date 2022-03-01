#from curses import use_default_colors
import streamlit as st
import time
import pandas as pd
import numpy as np

st.title('streamlit超入門')

st.write('progress bar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)

df_map = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.7],
    columns=['lat','lon']
)
st.map(df_map)

# if st.checkbox('Show Image'):
#     st.image(img,caption='hanabi',use_column_width=True)

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option = st.selectbox(
#     'あなたが好きな数字を',
#     list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です'


# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は',text,'です'
# condition = st.slider('あなたの調子は',0,100,50)
# 'コンディション:',condition



#st.table staticな表
#st.dataframe(df, width = 100, height = 100)

# """
# markdown記法
# # 章
# ## 節
# ```python
# print(aaa)
# ```
# """

