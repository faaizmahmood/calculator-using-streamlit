import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Streamlit Calculator", layout="centered")

st.title("🧮 Simple Calculator with Graph")

# --- Calculator Section ---
st.header("Calculator")

# Number inputs
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Operation select
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    result = num1 / num2 if num2 != 0 else "Infinity (Divide by 0)"


st.success(f"Result: {result}")


# --- Graph Section ---
st.header("📊 Graph Based on Number Input")

graph_number = st.slider("Pick a number for graph (1-20)", 1, 20, 5)



# Generate data (like showing property growth)
x = list(range(1, graph_number + 1))
y = [i ** 2 for i in x]  # Example: square growth

fig, ax = plt.subplots()
ax.plot(x, y, marker="o")
ax.set_title(f"Square Growth up to {graph_number}")
ax.set_xlabel("Number")
ax.set_ylabel("Value (n²)")

st.pyplot(fig)