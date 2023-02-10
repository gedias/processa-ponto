import streamlit as st
from rembg import remove
from PIL import Image


st.title('Removedor de fundo')
arquivo = st.file_uploader('imagem a enviar',type=["png", "jpg", "jpeg"],accept_multiple_files=False)
if arquivo is not None:
    open('imagem.jpeg','wb').write(arquivo.read())
    col1, col2 = st.columns([1,1])
    col1.image(open('imagem.jpeg','rb').read())
    open('imagem.png','wb').write(remove(open('imagem.jpeg','rb').read()))
    col2.image('imagem.png')
    col2.download_button('Baixar imagem',open('imagem.png','rb').read(),arquivo.name.replace("jpeg","png").replace("jpg","png"))
