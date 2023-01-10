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
echo ║ 4 ║                             KONIEC                              ║
echo ╚═══╩═════════════════════════════════════════════════════════════════╝ 

set /p option=
if %option%==1 goto option1
if %option%==2 goto option2
if %option%==3 goto option3
if %option%==4 exit
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
echo ╠═════════════════════════════════════════════════════════════════════╣
set /p input=║ Jaką liczbę chcesz otrzymać poprzez sumowanie liczb pierwszych: 
if not exist "Scripts\INPUT" MD Scripts\INPUT
echo %input% > Scripts/Input/input.txt
python Scripts/raport.py
echo ╠═════════════════════════════════════════════════════════════════════╣
echo ║                       RAPORT ZOSTAŁ WYGENEROWANY                    ║
echo ╚═════════════════════════════════════════════════════════════════════╝ 
pause
cls
goto begin

:option3
cls
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║     PODAJ LOKALIZACJE GDZIE MA ZOSTAĆ STWORZONA KOPIA RAPORTU       ║
echo ╚═════════════════════════════════════════════════════════════════════╝ 
set /p location=
set /p name=< Raport\date.txt
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║                       TWORZE BACKUP RAPORTU...                      ║
echo ╚═════════════════════════════════════════════════════════════════════╝ 
robocopy Raport %location%/%name% /E
echo ╔═════════════════════════════════════════════════════════════════════╗
echo ║             BACKUP RAPORT ZOSTAŁ WYKONANY POD LOKALIZACJĄ           ║
echo ╠═════════════════════════════════════════════════════════════════════╣
echo ║                        %location%/%name%
echo ╚═════════════════════════════════════════════════════════════════════╝ 
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
cls
goto begin
