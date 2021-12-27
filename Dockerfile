FROM python:3-buster

LABEL org.opencontainers.image.source https://github.com/SENERGY-Platform/mgw-kasa-dc


WORKDIR /usr/src/app

COPY . .
RUN pip install --extra-index-url https://www.piwheels.org/simple --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./dc.py"]
