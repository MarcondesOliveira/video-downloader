import streamlit as st
import yt_dlp

st.title("Video Downloader by Troll Cat")

link = st.text_input("Enter the video link")
if st.button("Download"):
    if link:
        if "x.com" in link:
            # Separar a URL no ponto de interrogação e pegar a primeira parte
            link = link.split('?')[0]            
        
        st.write(f"Downloading video from: {link}")
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        st.write("Download completed!")        
    else:
        st.write("Please enter a valid link.")


