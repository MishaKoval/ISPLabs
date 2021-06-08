FROM python:3.8.5-alpine

WORKDIR /usr/src/finalblog

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -U -r requirements.txt
COPY ./entrypoint.sh .

COPY . .
RUN ./manage.py migrate
RUN chmod +x /usr/src/finalblog/entrypoint.sh
ENTRYPOINT ["/usr/src/finalblog/entrypoint.sh"]