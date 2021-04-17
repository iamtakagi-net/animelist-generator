# 📰 animelist-generator: Japanese animelist generator with web application.
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iamtakagi-net/animelist-generator)](https://github.com/iamtakagi-net/animelist-generator/releases)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/iamtakagi-net/animelist-generator/CI)](https://github.com/iamtakagi-net/animelist-generator/actions/workflows/ci.yml)
[![license](https://img.shields.io/github/license/iamtakagi-net/animelist-generator)](https://github.com/iamtakagi-net/animelist-generator/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/iamtakagi-net/animelist-generator)](https://github.com/iamtakagi-net/animelist-generator/issues)
[![pull requests](https://img.shields.io/github/issues-pr/iamtakagi-net/animelist-generator)](https://github.com/iamtakagi-net/animelist-generator/pulls)

Generate the image of season-animelist based on the data fetched from [animateTimes](https://www.animatetimes.com/) 

![chrome_5I4bimZ9Ak](https://user-images.githubusercontent.com/46530214/110240691-83e87580-7f90-11eb-8c99-3307aa0180a2.png)
![hmI1MPKwGI](https://user-images.githubusercontent.com/46530214/110240693-8519a280-7f90-11eb-9a86-7d50461700a2.png)

## API Endpoints
URL  | Description | Response Example 
---- | ---- | ----
/api/generate?url=https://www.animatetimes.com/tag/details.php?id=xxx | Return Base64 | {"title", xxx, "base64Str": xxx}
/api/data?url=https://www.animatetimes.com/tag/details.php?id=xxx | Return Data | [{"img": xxx, "原作": xxx, "キャスト": xxx, "制作元請": xxx, "放送スケジュール": xxx}]

## Installation
`:latest` for master branch\
`:dev` for dev branch\
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
