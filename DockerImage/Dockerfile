From python:2.7

RUN apt-get update
RUN apt-get upgrade -y

RUN pip install html2text
RUN pip install beautifulsoup4
RUN pip install langid
RUN pip install roman

COPY ./code/ /src/
WORKDIR /src
ENTRYPOINT ["/src/main.sh"]

