import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation Function", layout="centered")

st.title("Sigmoid Activation Function")
st.write("Sigmoid Function: f(x) = 1 / (1 + e⁻ˣ)")

# Slider for x range
x_min, x_max = st.slider(
    "Select range of x values",
    min_value=-20,
    max_value=20,
    value=(-10, 10)
)

x = np.linspace(x_min, x_max, 400)
sigmoid = 1 / (1 + np.exp(-x))

# Plot
fig, ax = plt.subplots()
ax.plot(x, sigmoid)
ax.set_xlabel("x")
ax.set_ylabel("Sigmoid(x)")
ax.set_title("Sigmoid Activation Function")
ax.grid(True)

st.pyplot(fig)
