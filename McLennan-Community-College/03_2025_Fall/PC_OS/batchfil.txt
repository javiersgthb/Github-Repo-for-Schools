@echo off

rem Purpose: This program demonstrates basic batch file commands and copies batch files.
rem Filename: BATCHFIL.BAT
rem Author: Your Name
rem Date: 2025-10-23

cls

rem Display three blank lines
echo.
echo.
echo.

rem Display the main message
echo *** Insert your data files USB***

rem Display three more blank lines
echo.
echo.
echo.

pause

rem Clear the screen after the user presses a key
cls

rem Copy all files with a .bat extension from the USB root (F:\) to the F:\batch directory
copy F:\*.bat F:\batch