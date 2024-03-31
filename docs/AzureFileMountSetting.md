# Azure Files ボリュームを `open-interpreter-ssh-server` コンテナにマウントする手順

## ステップ 1: Storage Account の作成
1. Azure ポータルにログインします。
2. 「リソースの作成」をクリックし、「Storage account」を検索して選択します。
3. 必要な情報を入力し、「レビュー + 作成」をクリックします。
4. レビューが完了したら、「作成」をクリックして Storage Account を作成します。

## ステップ 2: ファイル共有の作成
1. 作成した Storage Account に移動します。
2. 左側のメニューから「ファイル共有」を選択します。
3. 「+ ファイル共有」をクリックして新しいファイル共有を作成します。
4. 名前とクォータを指定し、「作成」をクリックします。

## ステップ 3: コンテナーアプリ環境の設定
1. Azure CLI を使用して、コンテナーアプリ環境用のストレージを設定します。
   ```bash
   az containerapp env storage set --name <ENVIRONMENT_NAME> --resource-group <RESOURCE_GROUP_NAME> \
   --storage-name <STORAGE_NAME> \
   --azure-file-account-name <STORAGE_ACCOUNT_NAME> \
   --azure-file-account-key <STORAGE_ACCOUNT_KEY> \
   --azure-file-share-name <STORAGE_SHARE_NAME> \
   --access-mode ReadWrite
   ```

## ステップ 4: Azure Files ボリュームをマウントするためにコンテナーアプリを更新
1. コンテナーアプリの仕様を YAML ファイルにエクスポートします。
   ```bash
   az containerapp show -n <APP_NAME> -g <RESOURCE_GROUP_NAME> -o yaml > app.yaml
   ```
2. YAML ファイルを編集して、ボリュームとボリュームマウントを追加します。
   ```yaml
   volumes:
     - name: azure-files-volume
       storageType: AzureFile
       storageName: <STORAGE_NAME>
   containers:
     - name: open-interpreter-ssh-server
       volumeMounts:
         - volumeName: azure-files-volume
           mountPath: /mnt
   ```
3. 修正された YAML ファイルを使用してコンテナーアプリを更新します。
   ```bash
   az containerapp update --name <APP_NAME> --resource-group <RESOURCE_GROUP_NAME> --yaml app.yaml
   ```

## ステップ 5: ファイル共有マウントの確認
1. `open-interpreter-ssh-server` コンテナに接続し、Azure Files ボリュームが `/mnt` ディレクトリに正しくマウントされていることを確認します。