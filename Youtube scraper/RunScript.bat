@ECHO OFF
echo.
echo.
ECHO This tool is meant to scrape the yogsLive channel and tell me if any new Chilluminati/Dark Souls streams are available.
ECHO Currently a WIP
echo.
echo.
python .\ytScraper.py
echo.
python .\videoCheck.py
echo.
pause