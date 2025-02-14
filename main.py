#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QGridLayout, QPushButton, QCheckBox
import os
import yt_dlp
from configparser import ConfigParser
import pathlib

class Window(QWidget):
    def __init__(self):
        super().__init__()


        config = ConfigParser()
        filedir = pathlib.Path(__file__).parent.resolve()
        homepath = str(pathlib.Path.home())
        if os.name == 'nt':
            if not os.path.isfile(f'{filedir}\\ytdconfig.toml'):
                config['DEFAULT'] = {
                    'directory' : f'{homepath}\\Downloads',
                    'audio_mode': 'no'
                }
                with open(f'{filedir}\\ytdconfig.toml', 'w') as configfile:
                    config.write(configfile)
            
            config.read(f'{filedir}\\ytdconfig.toml')
        else:
            print('sup')
            if not os.path.isfile(f'{filedir}/ytdconfig.toml'):
                config['DEFAULT'] = {
                    'directory' : f'{homepath}/Downloads',
                    'audio_mode': 'no'
                }
                with open(f'{filedir}/ytdconfig.toml', 'w') as configfile:
                    config.write(configfile)
            
            config.read(f'{filedir}/ytdconfig.toml')

        self.default_path = config['DEFAULT']['directory']
        if config['DEFAULT']['audio_mode'] == 'yes':
            self.audio_mode = True
        else:
            self.audio_mode = False

        self.setWindowTitle("Niggesh YTD")
        self.url_box = QLineEdit()
        self.directory_box = QLineEdit(self.default_path)

        self.search_button = QPushButton("Download", self)
        self.search_button.clicked.connect(self.button_click)

        self.audioonly_checkbox = QCheckBox("Audio only", self)
        self.audioonly_checkbox.setChecked(self.audio_mode)
        self.audioonly_checkbox.stateChanged.connect(self.checkbox_changed)

        layout = QGridLayout()
        layout.addWidget(QLabel('Enter URL'), 0, 0)
        layout.addWidget(self.url_box, 0, 1)
        layout.addWidget(QLabel("Enter Path to download"),1, 0)
        layout.addWidget(self.directory_box, 1, 1)
        layout.addWidget(self.audioonly_checkbox, 2, 0)
        layout.addWidget(self.search_button, 3, 1)
        layout.addWidget(QLabel("Made with love by NotNiggesh"),4, 0)

        self.setLayout(layout)

    def button_click(self):
        path = self.directory_box.text()
        url = self.url_box.text()
        
        if not self.audio_mode:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  # Merge video and audio if FFmpeg is selected
                'outtmpl': f'{path}/%(title)s.%(ext)s',  
                'quiet': False,  
                'noprogress': True,  
                'merge_output_format': 'mp4',  # Allow merging into mp4 if FFmpeg is selected
            }


            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        else:
            ydl_opts = {
                'format':'bestaudio',
                'outtmpl': f'{path}/%(title)s.%(ext)s',
                'postprocessors' : [{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3'
                }]
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        print(url)





    def checkbox_changed(self, state):
        if state == 2:
            self.audio_mode = True
            print("Audio mode")
        else:
            self.audio_mode = False
            print("Video Mode")





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.resize(700, 200)

    window.show()

    sys.exit(app.exec_())