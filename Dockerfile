FROM python:2-slim
RUN mkdir /wepi
WORKDIR /wepi
COPY requirements.txt /wepi
RUN pip install –no-cache-dir -r requirements.txt
COPY wepi.py /wepi
ENTRYPOINT [ “python”, “-u”, “./wepi.py”]
