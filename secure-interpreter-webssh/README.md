# secure-interpreter-websshの認可機能付き

1. MS entraIDでグループの作成
2. Azure app serviceで「設定」→「認証」で「IDプロバイダー」を設定
3. 「APIのアクセス許可」にて「User.Read.All」を有効にする
4. 「構成」→「アプリケーション設定」で以下の内容を設定する(SSH_HOSTNAME, SSH_USERNAME, SSH_PASSWORD, SSH_PORTに設定した値が接続画面に入力されます)

| 変数名 | 概要 | 
| -- | -- |
| ALLOW_GROUP_OBJECT_ID | 認可に使いたいentraIDのグループのオブジェクト ID |
| SSH_HOSTNAME | ssh接続に使うhostname |
| SSH_USERNAME | ssh接続に使うusername |
| SSH_PASSWORD | ssh接続に使うpassword | 
| SSH_PORT | ssh接続に使うport番号 |
