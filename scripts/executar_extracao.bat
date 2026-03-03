@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo      EXTRATOR DE DADOS DE ESCOLAS - RPA ESCOLAR
echo ============================================================
echo.

:: Solicita o nome da pasta (dentro de data/input)
set /p folder="Digite o nome da pasta de PDFs (ex: 2026_01_13_relacao_escolas): "

:: Define o caminho completo para a pasta
set "input_path=data\input\%folder%"

:: Verifica se a pasta existe
if not exist "%input_path%" (
    echo.
    echo [ERRO] A pasta "%input_path%" nao foi encontrada.
    echo Verifique se ela esta dentro de 'data/input/'.
    echo.
    pause
    exit /b
)

:: Executa o script Python
echo.
echo Iniciando o processamento...
echo.
python -m src.main "%input_path%"

echo.
echo ============================================================
echo Processo Concluido! Verifique a pasta 'data/output/'.
echo ============================================================
echo.
pause
