@echo off
:begin
chcp 65001 > nul
echo ╔═══╦═════════════════════════════════════════════════════════════════╗
echo ║ 1 ║                     INFORMACJE O PROJEKCIE                      ║
echo ╠═══╬═════════════════════════════════════════════════════════════════╣
echo ║ 2 ║                         URUCHOM PROGRAM                         ║
echo ╠═══╬═════════════════════════════════════════════════════════════════╣
echo ║ 3 ║                         STWÓRZ BACKUP                           ║
echo ╠═══╬═════════════════════════════════════════════════════════════════╣
echo ║ 4 ║                          WRÓC DO CMD                            ║
echo ╠═══╬═════════════════════════════════════════════════════════════════╣
echo ║ 5 ║                             KONIEC                              ║
echo ╚═══╩═════════════════════════════════════════════════════════════════╝ 

set /p option=
if %option%==1 goto option1
if %option%==2 goto option2
if %option%==3 goto option3
if %option%==4 goto option4
if %option%==5 exit
goto wrong

:option1
cls
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║                        INFORMACJE O PROJEKCIE                       ║
echo ╠═════════════════════════════════════════════════════════════════════╣
echo ║                     Autor projektu: Mateusz Sawosz                  ║
echo ╠═════════════════════════════════════════════════════════════════════╣
echo ║          Zadanie 4 - "Liczby Pierwsze", Algorytmion 2012            ║
echo ║ Program wyznacza wszystkie sumy różnych liczb pierwszych równych n  ║
echo ╚═════════════════════════════════════════════════════════════════════╝
pause
cls
goto begin

:option2
cls
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║                        URUCHAMIAM SKRYPT PYTHON                     ║
echo ╚═════════════════════════════════════════════════════════════════════╝ 
python Scripts/raport.py
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║                       RAPORT ZOSTAŁ WYGENEROWANY                    ║
echo ╚═════════════════════════════════════════════════════════════════════╝ 
pause
cls
goto begin

:option3
cls
echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                       TWORZE BACKUP RAPORTU                        ║
echo ╚════════════════════════════════════════════════════════════════════╝ 
echo ...
echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                   BACKUP RAPORT ZOSTAŁ WYKONANY                    ║
echo ╚════════════════════════════════════════════════════════════════════╝ 
pause
cls
goto begin

:wrong
cls
echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                       PODAŁEŚ BŁĘDNĄ WARTOŚĆ                       ║
echo ╠════════════════════════════════════════════════════════════════════╣
echo ║          WCIŚNIJ DOWOLNY KLAWISZ BY WROCIĆ DO OKNA WYBORU          ║
echo ╚════════════════════════════════════════════════════════════════════╝ 
pause
goto begin

:option4
cls
cd 