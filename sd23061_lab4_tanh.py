import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function", layout="centered")

st.title("Hyperbolic Tangent (Tanh) Activation Function")
st.write("Tanh Function: f(x) = tanh(x)")

# Slider for x range
x_min, x_max = st.slider(
    "Select range of x values",
    min_value=-20,
    max_value=20,
    value=(-10, 10)
)

x = np.linspace(x_min, x_max, 400)
tanh = np.tanh(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, tanh)
ax.set_xlabel("x")
ax.set_ylabel("tanh(x)")
ax.set_title("Tanh Activation Function")
ax.grid(True)

st.pyplot(fig)
