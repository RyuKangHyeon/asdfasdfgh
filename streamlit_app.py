import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)