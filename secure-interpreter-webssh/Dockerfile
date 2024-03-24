FROM --platform=linux/x86_64 python:3.11.3

# poetryをインストール
RUN pip install poetry
RUN poetry config virtualenvs.create false

ADD . /code
WORKDIR /code

# 必要なファイルをコピー
COPY pyproject.toml poetry.lock ./

# 依存関係をインストールする
RUN poetry install

ENTRYPOINT [ "wssh" ] 