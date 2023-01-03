# MouseJiggler

Keeps Microsoft TEAMS active after system have been untouched for 4 min using python. Win32 only

## Clone MouseJiggler repo
```
git clone https://github.com/manmountain/MouseJiggler.git
```

## Install libraries
```
pip install -r requirements.txt
```

## Create a .bat file to autostart
Create .bat file `C:\Users\[your username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\mousejiggler.bat` and paste the code below. now every time when your pc will start this batch-file will execute and call your python script.

```
@echo off
cd path-to-repo\MouseJiggler\
python main.py
```

Exit application from systray by right-click'ing bell icon and select `Quit`
