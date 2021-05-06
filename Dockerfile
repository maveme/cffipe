FROM python:3.8-buster

# RUN pip install cffi
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python backend.py

RUN ls

RUN ldconfig

ENV LD_LIBRARY_PATH="./lang_protocol.so" 

RUN python client.py

CMD [ "python", "client.py" ]
