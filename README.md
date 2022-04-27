# Projector Control
Small program to controll a Panasonic PT-MZ770 projector.

Controls:
- On/Off
- Shutter On/Off
- Lens shift up/down
- Zoom in/out
- Preset for screen and backwall positions

### Installation

- Clone repo
  ```
  git clone https://github.com/h-leth/projector_control.git
  cd projector_control
  ```

- Update and rename vars.py with projector ip-address and login details
  ```
  cd projector_control
  cp vars.sample vars.py
  ```

- Install dependencies using pipenv
  
  ```pipenv install && pipenv shell```

- Make executeable
  
  ```pyinstaller --noconsole --name ProjectorControl projector_control/main.py```
