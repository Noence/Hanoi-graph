import streamlit as st
from main import HanoiTower

st.write("""
# Towers of Hanoi Game""")

towers = st.slider("Number of towers", 3, 5)
print(towers)

test = HanoiTower(3, towers).create_tower(shortest_path=True, plot_diagram=True, start='111', end='333')
# st.write()
st.pyplot(test)






