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
    im = Image.open('imagem.png')
    larg, altura = im.size
    ajustex = 0
    ajustey = 0
    if larg > altura:
        proporcao = larg / 600
        ajustey = int((525 - int(altura/proporcao) ) /2 )
    else:
        proporcao = altura / 525
        ajustex = int((525 - int(larg/proporcao) ) /2 )
    im = im.resize((int(larg/proporcao), int(altura/proporcao)))
    imnew = Image.new('RGBA', (600, 525))
    imnew.paste(im, (ajustex,ajustey) )
    imnew.save('imagem.png', )
    col2.image('imagem.png')
    col2.download_button('Baixar imagem',open('imagem.png','rb').read(),arquivo.name.replace("jpeg","png").replace("jpg","png"))
