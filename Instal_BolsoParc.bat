@echo off
echo Baixando o instalador do Python...
curl -o python-installer.exe https://www.python.org/ftp/python/3.x.x/python-3.x.x-amd64.exe
echo Instalando o Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
echo Limpando arquivos temporários...
del python-installer.exe
echo Python instalado com sucesso!

@echo off
pip install streamlit
pause
