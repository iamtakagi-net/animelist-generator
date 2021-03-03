# 📰 animelist-generator: Japanese season animelist generator with web application.

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/releases)
[![Docker Compose](https://img.shields.io/badge/DockerCompose-3.8-blue)](https://kotlinlang.org)
[![Nginx](https://img.shields.io/badge/Nginx-1.19.7-blue)](https://reactjs.org)
[![Node.js](https://img.shields.io/badge/Node.js-14-blue)](https://nodejs.org)
[![React](https://img.shields.io/badge/React-17.0.1-blue)](https://reactjs.org)
[![Next.js](https://img.shields.io/badge/Next.js-10.0.7-blue)](https://nextjs.org)
[![Python](https://img.shields.io/badge/Python-3.9.2-blue)](https://kotlinlang.org)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/releases)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/iamtakagi/animelist-generator/CI)](https://github.com/iamtakagi/animelist-generator/actions/workflows/ci.yml)
[![license](https://img.shields.io/github/license/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/issues)
[![pull requests](https://img.shields.io/github/issues-pr/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/pulls)

[animateTimes](https://www.animatetimes.com/) のページからデータを取得し クールごとのアニメリスト画像を生成するウェブアプリケーションです。\
開発中のため 一部不具合があります。ご了承ください。

[Cartelet0423/animeListGen](https://github.com/Cartelet0423/animeListGen) を元にウェブアプリケーションとして開発しています。

![キャプチャ1](https://user-images.githubusercontent.com/46530214/109392676-d0b0c880-7960-11eb-8dfb-4b39c92ca90c.PNG)
![キャプチャ2](https://user-images.githubusercontent.com/46530214/109520311-6ed29900-7aef-11eb-9a23-658ac320c4db.PNG)

### 例としてこのような画像を生成します
参照画像が存在しない場合 サムネイルは空白となります。
<details>
<summary>クリックして画像を開く</summary>
  <img src="https://user-images.githubusercontent.com/46530214/109520497-a5101880-7aef-11eb-9c08-cb0f6dd8067a.png"/>
</details>

## 動作環境 / OS
Linux/macOS/Windows

## インストール / Installation
イメージは DockerHub にpushされています。

`:latest` master ブランチへのプッシュの際にビルドされます。安定しています。\
`:dev` dev ブランチへのプッシュの際にビルドされます。開発版のため, 不安定である可能性があります。\
`:<tag>` GitHub 上のリリースに対応します。

### Docker Compose を使用してインストール / Install with Docker Compose

```console
touch docker-compose.dev.yml
```

`docker-compose.yml`
```yml
version: '3.8'

services:
  python:
    container_name: animelist-generator_python
    image: iamtakagi/animelist-generator_python:latest
    environment:
      TZ: Asia/Tokyo
      HOST: 0.0.0.0
      PORT: 8000
    restart: always
    ports:
      - 8000:8000
  next:
    container_name: animelist-generator_next
    image: iamtakagi/animelist-generator_next:latest
    environment:
      TZ: Asia/Tokyo
      HOST: 0.0.0.0
      PORT: 3000
    ports:
      - 3000:3000
    restart: always
  nginx:
    container_name: animelist-generator_nginx
    image: iamtakagi/animelist-generator_nginx:latest
    ports:
      - 8086:80
    environment:
      TZ: Asia/Tokyo
    restart: always
```

```console
# 起動 / Start
docker-compose up -d

# 停止 / Shutdown
docker-compose down

# ログ確認 / Logs
docker-compose logs -f

# 更新
docker pull iamtakagi/animelist-generator_python:latest
docker pull iamtakagi/animelist-generator_next:latest
docker pull iamtakagi/animelist-generator_nginx:latest
```

起動すると http://localhost:8086 にウェブページが立っています。

## 開発を行う場合 / Development mode
```console
git clone https://github.com/iamtakagi/animelist-generator (もしくはフォーク)
touch docker-compose.dev.yml
```

`docker-compose.dev.yml`
```yml
version: '3.8'

services:
  python:
    build: python
    environment:
      TZ: Asia/Tokyo
      HOST: 0.0.0.0
      PORT: 8000
    restart: always
    ports:
      - 8000:8000
  next:
    build: next
    environment:
      TZ: Asia/Tokyo
      HOST: 0.0.0.0
      PORT: 3000
      GENERATOR_HOST: python
    ports:
      - 3000:3000
    restart: always
  nginx:
    build: nginx
    ports:
      - 8086:80
    environment:
      TZ: Asia/Tokyo
    restart: always
```

## 貢献 / Contribution

### Issues
バグの報告・改善点・提案等を行ってください。

### Pull Requests
開発には VSCode を使用しています。
各自で環境を準備してください。

## 当アプリケーションをウェブ上に公開する場合
公開は自己責任で行ってください。開発者は一切の責任を負いかねます。
