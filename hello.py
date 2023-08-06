import streamlit as st
import time

st.set_page_config(
        page_title="My App",
        page_icon=":shark")

"""
# This is a doc title

This is some _markdown_
"""

st.latex(r'''
         \displaystyle{\int_{0}^{5}} f(x) \cdot dx
         ''')


@st.cache_data
def expensive_computation(a, b):
    time.sleep(2)  # 👈 This makes the function take 2s to run
    return a * b

a = 3
b = 21
res = expensive_computation(a, b)

st.write("Results:", res)
