FROM --platform=linux/x86_64 python:3.11.3

# 必要なツールをインストール
RUN apt-get update &&  \
    apt-get install -y nkf &&  \
    apt-get install -y default-jdk

# poetryをインストール
RUN pip install poetry
RUN poetry config virtualenvs.create false

# 必要なファイルをコピー
COPY pyproject.toml poetry.lock entrypoint.sh app.py /code/
WORKDIR /code/

# 依存関係をインストールする
RUN poetry install

# Start and enable SSH
RUN apt-get update \
    && apt-get install -y gunicorn \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd \
    && chmod u+x ./entrypoint.sh
COPY sshd_config /etc/ssh/

EXPOSE 8000 2222

ENTRYPOINT [ "./entrypoint.sh" ] 