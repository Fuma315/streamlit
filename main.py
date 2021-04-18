import streamlit as st
import time
st.title('Streamlit 超入門')

st.write('Progress_bar')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.02)

'Done!!!'




left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに保持を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# st.write('あなたの趣味：', text)

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# st.write('コンディション：', condition)

# if st.checkbox('Show Images'):
#     img = Image.open('/Users/fuma.moteki/Desktop/pose_reiwa_man.png')
#     st.image(img, caption='hoge', use_column_width=True)

