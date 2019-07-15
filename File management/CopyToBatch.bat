@ECHO OFF

:startscript
echo.
echo.
ECHO	Welcome! This is a simple batch for copying/moving video to a flash drive:
ECHO	1. Copy to USB and then move files to a "Watched" folder
ECHO	2. Only copy to USB
ECHO	3. Exit
echo.
echo.
SET /P ACTION="Choose an option: "

2>NUL CALL :CASE_%ACTION%
IF ERRORLEVEL 1 CALL :DEFAULT_CASE

ECHO Done.
EXIT /B

:CASE_1
  COLOR 9F
  ECHO Copying and moving...
  echo.
  python .\renameScript.py
  COPY *.mkv G:\#Video\Seasonals
  MOVE *.mkv .\Watched
  ECHO Task 1 is done!
  PAUSE
  GOTO END_CASE
:CASE_2 
  COLOR CF
  ECHO Copying...
  echo.
  python .\renameScript.py
  COPY *.mkv G:\#Video
  ECHO Task 2 is done!
  GOTO END_CASE
:CASE_3
  GOTO END_CASE
:DEFAULT_CASE
  ECHO Try again, unknown option: "%ACTION%"
  GOTO startscript
:END_CASE
  VER > NUL 
  GOTO :EOF