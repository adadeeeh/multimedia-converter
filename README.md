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
    "colors": 64,
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
  - `bitrate` = target bitrate (in B/s)
  - `sample_rate` = audio sample rate (in kHz)
  - `channel` (not implemented)
  - `output` (mandatory) = output file extension

- Request

  ```json
  {
    "file": "",
    "bitrate": 128,
    "sample_rate": 48000,
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
  - `frame_size` = target frame_size (in `widthxheight` format)
  - `frame_rate` = target frame rate (in fps)
  - `bitrate` = target bitrate (in B/s)
  - `sample_rate` = audio sample rate (in kHz)
  - `channel` (not implemented)
  - `output` (mandatory) = output file extension

- Request

  ```json
  {
    "file": "",
    "frame_size": "1366x768",
    "frame_rate": 60,
    "bitrate": 128,
    "sample_rate": 48000,
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
