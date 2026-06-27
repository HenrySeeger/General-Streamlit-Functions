# app.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

if "rad1" not in st.session_state:
    st.session_state.rad1 = 1

if "rad2" not in st.session_state:
    st.session_state.rad2 = 2

if "rad3" not in st.session_state:
    st.session_state.rad3 = 3

cols = st.columns([1, 1, 1], border = True)

rad_options = ["1", 2, 3, 3.5, "giraffe"]

def rad_change(changed):
    index_sum = len(rad_options) * (len(rad_options) - 1) / 2 # -1 instead of +1 because of zero-indexing
    r1 = st.session_state.rad1
    r2 = st.session_state.rad2
    r3 = st.session_state.rad3
    
    if changed == 1:
        if r1 == r2:
            st.session_state.rad2 = rad_options[int(index_sum - rad_options.index(r1) - rad_options.index(r3))]
        elif r1 == r3:
            st.session_state.rad3 = rad_options[int(index_sum - rad_options.index(r1) - rad_options.index(r2))]
    if changed == 2:
        if r2 == r1:
            st.session_state.rad1 = rad_options[int(index_sum - rad_options.index(r3) - rad_options.index(r2))]
        elif r2 == r3:
            st.session_state.rad3 = rad_options[int(index_sum - rad_options.index(r1) - rad_options.index(r2))]
    if changed == 3:
        if r3 == r1:
            st.session_state.rad1 = rad_options[int(index_sum - rad_options.index(r3) - rad_options.index(r2))]
        elif r3 == r2:
            st.session_state.rad2 = rad_options[int(index_sum - rad_options.index(r3) - rad_options.index(r1))]

for i, col in enumerate(cols):
    with col:
        st.radio(label = f"rad{i + 1}", options = rad_options, key = f"rad{i + 1}", on_change = rad_change, args = (i + 1,))