# secure-interpreter

## 概要
secure-interpreterは、クローズドな環境から安全に利用できるOpenInterpreter環境を提供するOSSです。  
このプロジェクトは2つのDockerイメージを提供しており、ユーザーはお好みのホスティングプラットフォームにこれらをデプロイすることで環境を構築できます。

## Dockerイメージについて
- open-interpreter-ssh-server : open-interpreterを搭載したssh接続可能なコンテナ
- secure-interpreter-webssh : WebSSHを搭載し、open-interpreter-ssh-serverに安全にSSH接続できるコンテナ

## インストール方法
- **open-interpreter-ssh-server**: 
  - `./open-interpreter-ssh-server/.env.sample` ファイルを参考に環境変数をホスティングサービスに設定してください。
  - Dockerイメージ `ghcr.io/dx-junkyard/secure-interpreter/open-interpreter-ssh-server:latest` をpullして起動します。
- **secure-interpreter-webssh**: 
  - 特別な設定は不要です。Dockerイメージ `ghcr.io/dx-junkyard/secure-interpreter/secure-interpreter-webssh:latest` をpullして起動します。

## 使用方法
### open-interpreter-ssh-server
```
docker run -v -it --env-file=.env --rm --name open-interpreter-ssh-server -p 8000:80 open-interpreter-ssh-server
```

### secure-interpreter-webssh
```
docker run -it --rm --name secure-interpreter-webssh -p 80:80 secure-interpreter-webssh
```

## 設定とカスタマイズ
ホスティングサービスは自由に選択できます。少なくともAzureでは起動確認ができています。  
例: Azureでの構成例
![AzureHostingExample.jpg](https://raw.githubusercontent.com/dx-junkyard/secure-interpreter/main/docs/AzureHostingExample.jpg)

## ライセンス
このプロジェクトは [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.html) のもとで公開されています。

## 利用しているOSS
- [OpenInterpreter](https://github.com/OpenInterpreter/open-interpreter)
- [WebSSH](https://github.com/huashengdun/webssh)

## コントリビューション
コントリビューションガイドラインは現在作成中です。
