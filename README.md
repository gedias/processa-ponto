# Processa ponto

by Geisler

## Objetivo

Este python tem como Objetivo converter o arquivo AFD de relógio de ponto para planilha xlsx por funcionários.

## Como utilizo?

Eu executo o mesmo utilizando a imagem docker geisler/streamlit-lite:0.1 mapeando um diretório dentro do docker com o app.py e um executa.sh.
o conteúdo do **executa.sh** conforme abaixo:

```bash

#!/bin/bash
streamlit run app.py
```

desta forma executamos o docker conforme abaixo:

```bash

docker run -ti --name streamlit --rm -v /home/geisler/streamlit-tst:/app -p 8500:8501 geisler.dias/streamlit-lite:0.4
```
