import streamlit as st

color = st.text_input("Enter a color")
plural_noun = st.text_input("Enter a plural noun")
celebrity = st.text_input("Enter a celebrity's name")

if color and plural_noun and celebrity:
    st.write(f"Roses are {color}")
    st.write(f"{plural_noun} are blue")
    st.write(f"I love {celebrity}")
