import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation Function", layout="centered")

st.title("ReLU Activation Function")
st.write("Rectified Linear Unit (ReLU): f(x) = max(0, x)")

# Slider for x range
x_min, x_max = st.slider(
    "Select range of x values",
    min_value=-20,
    max_value=20,
    value=(-10, 10)
)

x = np.linspace(x_min, x_max, 400)
relu = np.maximum(0, x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, relu)
ax.set_xlabel("x")
ax.set_ylabel("ReLU(x)")
ax.set_title("ReLU Activation Function")
ax.grid(True)

st.pyplot(fig)
