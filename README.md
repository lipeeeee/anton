<div align="center">
	
# anton
	
</div>
Anton is a league of legends hack focused around QOL(Quality of life) improvements.

# League Client Hook
...

# Remove Challenges
...

# Start as Offline
...


# HACKING LEAGUE Client
```bash
WMIC PROCESS WHERE name='LeagueClientUx.exe' GET commandline
```

# BUILDING .EXE

WHITHOUT CUSOTOM FONT JSON(USING ONE THAT CUSTOMTKINTER ALREADY PROVIDES)
```bash
pyinstaller.exe -F main.py --collect-all customtkinter
```

# PS
CTK DOES NOT ALLOW `HIDE_TO_TRAY` SO WE ALWAYS HIDE TO TASKBAR

VERY SMALL RAM/MEMORY OPTIMIZATION CAN BE DONE IN OUTFRAME MAKE() BUT NOT WORTH
THE EFFORT TO CONCEPTUALIZE RN

# TODO
- BUILDING OF CONFIG PACKAGE!!!! IMPORTANT 👍

- MIGRATE TO CUSTOMTKINTER AND REFACTOR WHOLE GUI PROGRAMMIGN 👍

- MAKE UTILITY FUNCT TO CREATE GUI WITHOUT BOILERPLATE Code 
IDEA: MAKE A STATIC FUNCTION INSIDE EACH FRAME THAT RETURNS A NEW INSTANCE OF FRAME
OR: MAKE A HELPER FUNCTION INSIDE EACH FRAMES FILE THAT RETURNS AN INSTANCE OF FRAME

- INCLUDE EMPTY JSON FIX IN `Config.fix_files`

- IMPLEMENT STOP KEYBIND/FLAG ON BACKGROUND_THREAD.PY

- SMALL OPTIMIZATION WITH REGEX PROCESSING IN LEAUGE CONNECTION

- IMPLEMENT ZOOMED INITIALIZATION AS AN OPTION

- OFFLINE STATUS

- CLEAR CHALENGES MANIPULATION

- ICON/PROFILE BANNER/PROFILE RANK MANIPULATION WITH HTTP REQUESTS

- INGAME DLL INJECTED SKIN CHANGER? | IF NOT OUTGAME SKINCHANGER *BUT RAM OFFSTETS ARE ANNOYING*, MAYBE NO SKINCHANGER

- DRAWINGS? (CHECK RIOT TOS)

- EXTERNAL SPACEGLIDER (CHECK RIOT TOS) ALSO *RAM OFFSETS ARE ANNOYING*

- EXPLORE LOCALHOST INGAMGE API

# BEFORE COMMIT CHECKLIST
- GOOGLE DOCING
- LOGGING PROCESSES?????
