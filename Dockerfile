FROM python:3

RUN pip install cffi

COPY . .

RUN python ./backend.py

RUN ls

CMD [ "python", "./client.py" ]
