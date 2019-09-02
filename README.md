# サーバレスハンズオン

## cloud9設定

``` bash
$ vi ~/.bashrc
  # [18行目を以下の通り変更して保存]
  # 変更前 alias python=python27
  # 変更後 alias python=python36

$ source ~/.bashrc

$ sudo update-alternatives --config python
  # 「2」を入力して、Enter
```

## 必要なライブラリのインストール

``` bash
$ cd ~/environment/serverless-handson01
$ sudo pip install -r requirements.txt
```

## 実行

``` bash
# ローカル実行
$ cd ~/environment/serverless-handson01/
$ chalice local --port 8080

# デプロイ
$ cd ~/environment/serverless-handson01/
$ chalice deploy
```
