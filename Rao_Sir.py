from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Rao Maths Classes",page_icon=":book:",layout="wide")
def anime_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load assets
math_anime=anime_url("https://assets10.lottiefiles.com/packages/lf20_neoi7cp3.json")
img=Image.open("images/web.jpg")
#Header Section
with st.container():
    l_column,r_column = st.columns(2)
    with l_column:
        st.title("WELCOME to Rao Maths Classes.")
        st.subheader("Hi, I am Rakes Rao.")
        st.subheader("This website is for study purpose only.")
        st.image(img)
    with r_column:
        st_lottie(math_anime,height=200,key="maths")
        st.header("Follow me on:")
        st.subheader("[Youtube](https://www.youtube.com/@rakeshkumarrao8782)")
        st.subheader("[Instagram](https://www.instagram.com/rakeshkumarrao77/)")
        st.subheader("[Facebook](https://www.facebook.com/rakeshkumar.rao.50)")