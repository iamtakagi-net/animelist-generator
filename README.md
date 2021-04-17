# 📰 animelist-generator: Japanese animelist generator with web application.

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/releases)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/releases)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/iamtakagi/animelist-generator/CI)](https://github.com/iamtakagi/animelist-generator/actions/workflows/ci.yml)
[![license](https://img.shields.io/github/license/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/issues)
[![pull requests](https://img.shields.io/github/issues-pr/iamtakagi/animelist-generator)](https://github.com/iamtakagi/animelist-generator/pulls)

[animateTimes](https://www.animatetimes.com/) のページからデータを取得し クールごとのアニメリスト画像を生成するウェブアプリケーションです。

![chrome_5I4bimZ9Ak](https://user-images.githubusercontent.com/46530214/110240691-83e87580-7f90-11eb-8c99-3307aa0180a2.png)
![hmI1MPKwGI](https://user-images.githubusercontent.com/46530214/110240693-8519a280-7f90-11eb-9a86-7d50461700a2.png)

- 例としてこのような画像を生成します
  - 参照画像が存在しない場合 サムネイルは空白となります。
<details>
<summary>クリックして画像を開く</summary>
  <img src="https://user-images.githubusercontent.com/46530214/109520497-a5101880-7aef-11eb-9c08-cb0f6dd8067a.png"/>
</details>

- ワンクリックでダウンロードできます
  - [0.0.4](https://github.com/iamtakagi/animelist-generator/releases/tag/0.0.4) より対応

![chrome_kZaefnhGgX](https://user-images.githubusercontent.com/46530214/113428672-2968fa80-9412-11eb-917e-1f63b32a21d5.png)
![chrome_cjY01mgHTI](https://user-images.githubusercontent.com/46530214/113428675-2a9a2780-9412-11eb-9ba6-44fbd7c9365c.png)

- API Endpoints
  - いくつかAPIを提供しています

URL  | Description | Response Example 
---- | ---- | ----
/api/generate?url=https://www.animatetimes.com/tag/details.php?id=xxx | アニメリスト画像を生成してBase64で返します | {"title", xxx, "base64Str": xxx}
/api/data?url=https://www.animatetimes.com/tag/details.php?id=xxx | データを配列で返します | [{"img": xxx, "原作": xxx, "キャスト": xxx, "制作元請": xxx, "放送スケジュール": xxx}]

## Installation

`:latest` for master branch
`:dev` for dev branch 
`:<tag>` for release tag

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
    restart: always
    ports:
      - 3000:3000
  nginx:
    container_name: animelist-generator_nginx
    image: iamtakagi/animelist-generator_nginx:latest
    ports:
      - 8086:80
    environment:
      TZ: Asia/Tokyo
    restart: always
```
