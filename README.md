# captha_scraper
script to get data from a website where the captcha protection is active


strategy :
run scripts\converter.bat data\captcha7.jpg 60 95
run scripts\converter.bat data\captcha7.jpg 80 95

load the longest string and try it


Going with Sphynx (the other choice is wit.ai)

1- https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
pip install pocketsphinx

model_dir = C:\Users\NJean\Miniconda3\envs\deeplearning\lib\site-packages\speech_recognition\pocketsphinx-data\en-US
2 - add italian
https://drive.google.com/open?id=0Bw_EqP-hnaFNSXUtMm8tRkdUejg

bash script
#!/usr/bin/env bash
SR_LIB=$(python -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))")
sudo apt-get install --yes wget unzip
sudo wget https://db.tt/tVNcZXao -O "$SR_LIB/fr-FR.zip"
sudo unzip -o "$SR_LIB/fr-FR.zip" -d "$SR_LIB"
sudo chmod --recursive a+r "$SR_LIB/fr-FR/"
sudo wget https://db.tt/2YQVXmEk -O "$SR_LIB/zh-CN.zip"
sudo unzip -o "$SR_LIB/zh-CN.zip" -d "$SR_LIB"
sudo chmod --recursive a+r "$SR_LIB/zh-CN/"



3 - get sox

4 - get pydub https://stackoverflow.com/questions/36458214/split-speech-audio-file-on-words-in-python





pip install SpeechRecognition

https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
