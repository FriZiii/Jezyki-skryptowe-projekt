@echo off
:begin
chcp 65001 > nul
echo ╔═╦════════════════════════╗
echo ║1║ INFORMACJE O PROJEKCIE ║
echo ╚═╩════════════════════════╝
echo ╔═╦════════════════════════╗
echo ║2║    URUCHOM PROGRAM     ║
echo ╚═╩════════════════════════╝
echo ╔═╦════════════════════════╗
echo ║3║     STWÓRZ BACKUP      ║
echo ╚═╩════════════════════════╝
echo ╔═╦════════════════════════╗
echo ║4║      WRÓC DO CMD       ║
echo ╚═╩════════════════════════╝
echo ╔═╦════════════════════════╗
echo ║5║        KONIEC          ║
echo ╚═╩════════════════════════╝ 

set /p option=
if %option%==1 goto option1
if %option%==2 goto option2
if %option%==3 goto option3
if %option%==4 goto option4
if %option%==5 exit
goto wrong

:option1
cls
echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                        INFORMACJE O PROJEKCIE                      ║
echo ╠════════════════════════════════════════════════════════════════════╣
echo ║                   Autor projektu: Mateusz Sawosz                   ║
echo ║          Zadanie 4 - "Liczby Pierwsze", Algorytmion 2012           ║
echo ║ Program wyznacza wszystkie sumy różnych liczb pierwszych równych n ║
echo ╚════════════════════════════════════════════════════════════════════╝ 
pause
cls
goto begin

:option2
cls
echo Uruchamiam skrypt PYTHON
python python.py
pause
cls
goto begin

:option3
cls
echo Robię BACKUP
pause
cls
goto begin

:wrong
cls
echo Wrong answer
pause
goto begin

:option4
cls
cd 