# Pyweek 34

<div align="center">

[![Python Check](https://github.com/MrTanoshii/PyWeek-34/actions/workflows/python_lint_check.yml/badge.svg)](https://github.com/MrTanoshii/PyWeek-34/actions/workflows/python_lint_check.yml)

</div>

## Python Modules

<div align="center">

[![Python v3.9](https://img.shields.io/badge/Python-v3.9-blue)](https://docs.python.org/3.9/)
[![Arcade v2.6.15](https://img.shields.io/badge/Arcade-v2.6.15-blue)](https://api.arcade.academy/en/2.6.15/)

</div>

## Other Dependencies

<div align="center">

[![FFmpeg](https://img.shields.io/badge/FFmpeg-required-blue)](https://www.ffmpeg.org/download.html)

</div>

## Python venv setup

<details>
  <summary>[SHOW/HIDE] Python venv setup</summary>
    <details>
      <summary>[SHOW/HIDE] Windows Instructions</summary>

### Windows

#### Create the venv

```shell
cd GITHUB_REPO_ROOT_DIR
python -m venv venv
```

#### Activate the venv

```shell
cd GITHUB_REPO_ROOT_DIR
.\venv\Scripts\activate
```

Note: Your terminal will have `(venv)` prefixed to your current path.

#### Deactivate the venv

```shell
deactivate
```

</details><details>
    <summary>[SHOW/HIDE] Linux Instructions</summary>

### Linux

```
shell
cd GITHUB_REPO_ROOT_DIR
python3 -m venv venv
```

#### Activate the venv

```shell
cd GITHUB_REPO_ROOT_DIR
source venv\bin\activate
```

Note: Your terminal will have `(venv)` prefixed to your current path.

#### Deactivate the venv

```shell
deactivate
```

</details>

### Install Dependencies

With venv activated, Windows `pip install -r requirements.txt` Linux `pip3 install -r requirements.txt`

### Running Instructions

Run game with `python3 run_game.py`

</details>
