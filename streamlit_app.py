import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


rand = np.random.cormal(1, 2, size=20)
fig, ax = plt.subpots()
ax.hist(rand, bins=15)
st.pyplot(fig)