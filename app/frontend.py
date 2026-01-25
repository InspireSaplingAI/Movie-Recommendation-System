"""Streamlit frontend (starter).

Run with: streamlit run app/frontend.py
"""

import streamlit as st

st.set_page_config(page_title="Movie Recommender Demo")
st.title("Movie Recommendation Demo")

user_id = st.number_input("User ID", min_value=0, value=1, step=1)
if st.button("Get Recommendations"):
    st.info("This is a demo: hook up to the API or local inference module.")
    st.write(["movie_1", "movie_2", "movie_3"]) 
