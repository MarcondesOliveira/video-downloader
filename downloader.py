import streamlit as st
import yt_dlp
import os

def on_click():
    st.session_state.user_input = ""

st.title("Video Downloader by Troll Cat")

link = st.text_input("Enter the video link", key="user_input")
if st.button("Carregar"):
    if link:
        if "x.com" in link:
            # Separar a URL no ponto de interrogação e pegar a primeira parte
            link = link.split('?')[0]            
        
        st.write(f"Downloading video from: {link}")
        ydl_opts = {
            'outtmpl': '/tmp/%(title)s.%(ext)s',  # Salva o arquivo no diretório /tmp
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_title = info_dict.get('title', None)
            video_ext = info_dict.get('ext', None)
            video_filename = f"/tmp/{video_title}.{video_ext}"
                
        with open(video_filename, "rb") as file:
            btn = st.download_button(
                label="Download Video",
                data=file,
                file_name=f"{video_title}.{video_ext}",
                mime="video/mp4",
                on_click=on_click
            )
                        
        os.remove(video_filename)
    else:
        st.write("Please enter a valid link.")