FROM valian/docker-python-opencv-ffmpeg:py3
EXPOSE 5000
RUN git clone https://github.com/adadeeeh/multimedia-converter app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_ENV production
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
