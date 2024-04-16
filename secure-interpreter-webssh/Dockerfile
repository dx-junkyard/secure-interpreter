FROM --platform=linux/x86_64 python:3.11.5

ADD . /code
WORKDIR /code

RUN git clone https://github.com/huashengdun/webssh.git

WORKDIR /code/webssh

COPY index.html ./webssh/templates
COPY page403.html ./webssh/templates
COPY handler.py ./webssh

RUN python ./setup.py build
RUN python ./setup.py install

ENTRYPOINT [ "wssh", "--port=80" ] 
