FROM python:3

RUN pip install cffi

COPY . .

RUN python backend.py

RUN ls

RUN ldconfig

ENV LD_LIBRARY_PATH="./lang_protocol.so" 

RUN python client.py

CMD [ "python", "client.py" ]
