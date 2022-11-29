from jina import Client
from docarray import Document
import streamlit as st
query = st.text_input("Paper's abstract")
if st.button(label="Search"):
    client = Client(host="0.0.0.0:57127")
    response = client.search(
        Document(text=query),
        parameters={"traversal_path": "@r"},
    )
    matches = response[0].matches
    for match in matches:
        st.header(match.tags["title"])
        st.caption(match.tags["abstract"])