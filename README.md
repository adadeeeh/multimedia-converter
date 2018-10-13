# Multimedia Converter

## Index

- [Requirements](#requirements)
- [Installation](#installation)
- [API](#api)

## Requirements

- [Python 3+](https://www.python.org/downloads/)
- [FFMPEG](http://www.ffmpeg.org/download.html)

## Installation

### Create Virtual Environment

```sh
python -m venv venv
```

### Activate the Environment

- Unix

  ```sh
  . venv/bin/activate
  ```

- Windows

  ```sh
  venv\Scripts\activate
  ```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### FFMPEG

Download [FFMPEG](http://www.ffmpeg.org/download.html) and add the bin directory to the environment path.

### Run the Server

- Unix

  ```sh
  export FLASK_ENV=development
  flask run
  ```

- Windows

  ```sh
  set FLASK_ENV=development
  flask run
  ```

### Run Test

```sh
python -m unittest
```

## API

### Image

```text
/api/convert/image?json=true
```

- Query Parameter
  - `json` (optional): set only if you want the api to return a JSON instead of the file

- Parameter
  - `file` (mandatory)
  - `resolution` = target resolution (in `widthxheight` format)
  - `colors` = color depth
  - `conversion_rate` (not implemented)
  - `output` (mandatory) = output file extension

- Request

  ```json
  {
    "file": "",
    "resolution": "512x512",
    "colors": 16,
    "output": "png"
  }
  ```

- Response
  
  The converted file or if you set `json` to true:

  ```json
  {
    "status": "success",
    "file_url": "/files/filename.extension"
  }
  ```

### Audio

```text
/api/convert/audio?json=true
```

- Query Parameter
  - `json` (optional): set only if you want the api to return a JSON instead of the file

- Parameter
  - `file` (mandatory)
  - `time_off` = start time offset (format: "hh:mm:ss")
  - `time_off_s` `time_off_m` `time_off_s` = respective start time offset. Will only be considered if all three value is set. `time_off` will have higher priority
  - `time_stop` = stop time (format: "hh:mm:ss")
  - `time_stop_s` `time_stop_m` `time_stop_s` = respective stop time. Will only be considered if all three value is set. `time_stop` will have higher priority
  - `bitrate_audio` = audio bitrate (in B/s)
  - `sample_rate` = audio sampling rate (in Hz)
  - `channels` = number of audio channels
  - `disable_audio` = disable audio (boolean)
  - `volume` = volume (0-255)
  - `output` (mandatory) = output file extension

- Request

  ```json
  {
    "file": "",
    "time_off": "00:00:30",
    "time_off_h": "0",
    "time_off_m": "0",
    "time_off_s": "30",
    "time_stop": "00:01:30",
    "time_stop_h": "0",
    "time_stop_m": "1",
    "time_stop_s": "30",
    "bitrate_audio": 128,
    "sample_rate": 48000,
    "channels": 2,
    "disable_audio": true,
    "volume": 128,
    "output": "ogg"
  }
  ```

- Response
  
  The converted file or if you set `json` to true:

  ```json
  {
    "status": "success",
    "file_url": "/files/filename.extension"
  }
  ```

### Video

```text
/api/convert/video?json=true
```

- Query Parameter
  - `json` (optional): set only if you want the api to return a JSON instead of the file

- Parameter
  - `file` (mandatory)
  - `time_off` = start time offset (format: "hh:mm:ss")
  - `time_off_s` `time_off_m` `time_off_s` = respective start time offset. Will only be considered if all three value is set. `time_off` will have higher priority
  - `time_stop` = stop time (format: "hh:mm:ss")
  - `time_stop_s` `time_stop_m` `time_stop_s` = respective stop time. Will only be considered if all three value is set. `time_stop` will have higher priority
  - `rate` = frame rate (in fps)
  - `size` = frame size (in `wxh` format)
  - `aspect` = aspect ratio (4:3, 16:9, etc)
  - `disable_video` = disable_video (boolean)
  - `bitrate_video` = video bitrate (in B/s)
  - `bitrate_audio` = audio bitrate (in B/s)
  - `sample_rate` = audio sampling rate (in Hz)
  - `channels` = number of audio channels
  - `disable_audio` = disable audio (boolean)
  - `volume` = volume (0-255)
  - `output` (mandatory) = output file extension

- Request

  ```json
  {
    "file": "",
    "time_off": "00:00:30",
    "time_off_h": "0",
    "time_off_m": "0",
    "time_off_s": "30",
    "time_stop": "00:01:30",
    "time_stop_h": "0",
    "time_stop_m": "1",
    "time_stop_s": "30",
    "rate": 60,
    "size": "1280x720",
    "aspect": "16:9",
    "disable_video": true,
    "bitrate_video": 256,
    "bitrate_audio": 128,
    "sample_rate": 48000,
    "channels": 2,
    "disable_audio": true,
    "volume": 128,
    "output": "mkv"
  }
  ```

- Response
  
  The converted file or if you set `json` to true:

  ```json
  {
    "status": "success",
    "file_url": "/files/filename.extension"
  }
  ```
