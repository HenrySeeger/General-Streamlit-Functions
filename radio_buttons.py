# app.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

rad_options = [1, "2", 3, "giraffe", 3.14, 6, 7, 8]

num_cols = 4
num_cols = min(num_cols, len(rad_options))

for i, default_val in enumerate(rad_options):
  key = f"rad{i}"
  if key not in st.session_state:
    st.session_state[key] = rad_options[i]

cols = st.columns(num_cols, border = True)

def rad_change(changed):
  for i in [i for i in range(len(cols[:])) if i != changed]:
    if st.session_state[f"rad{changed}"] == st.session_state[f"rad{i}"]:
      available_indices = list(set(range(len(rad_options))) ^ {rad_options.index(st.session_state[f"rad{j}"]) for j in range(len(cols)) if j != i})
      st.session_state[f"rad{i}"] = rad_options[available_indices[0]]
      break

for i, col in enumerate(cols):
  with col:
    st.radio(label = f"rad{i}", options = rad_options, horizontal = False, key = f"rad{i}", on_change = rad_change, args = (i,))