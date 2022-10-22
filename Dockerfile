FROM python
RUN pip3 install --upgrade pip

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir -r /code/requirements.txt
COPY ./app /code/app
CMD ["python3", "app/main.py"]
