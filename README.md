# YDownloader

This is a python based GUI app to download Youtube videos and audio

## Installation
Make sure you have Python and PIP installed in your system

Clone the repository using
` git clone https://www.github.com/InfernalSpark/YDownloader `
or just download and extract the ZIP file

Open the folder and install the requirements using
`pip install -r requirements.txt`

#### NOTE

If PIP doesnt let you install global packages, you can create a local environment with

``` bash
python3 -m venv yd_env
source yd_env/bin/activate
```

or on Windows

``` cmd
py -m venv yd_env
yd_env/bin/activate.bat
```

Then install [ffmpeg](https://www.ffmpeg.org/download.html) and place the executable in the same folder as `main.py` \
You can skip this step if you have ffmpeg already installed.

## Usage

### Linux/MacOS

Give the script executable permission using `chmod +x main.py` \
You can then run the app using `./main.py`

or just `python3 main.py`

### Windows

Run the script using `py main.py`

### Configuration

When the script is run for the first time, a config file named `ytdconfig.toml` will be created \
You can modify the default download directory and whether to default to audio only mode in this file

## Upcoming feaatures (hopefully)

- Error messages in GUI
- Installation Script that automates ffmpeg and pip dependency installation
- Change video and audio quality through GUI
- Loading Bar
  