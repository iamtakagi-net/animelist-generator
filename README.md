# animelist-generator: season animelist generator with web application.

[![Docker Compose](https://img.shields.io/badge/DockerCompose-3.8-blue)](https://kotlinlang.org)
[![Node.js](https://img.shields.io/badge/Node.js-14-blue)](https://nodejs.org)
[![React](https://img.shields.io/badge/React-17.0.1-blue)](https://https://reactjs.org)
[![Next.js](https://img.shields.io/badge/Next.js-10.0.7-blue)](https://nextjs.org)
[![Python](https://img.shields.io/badge/Python-3.9.2-blue)](https://kotlinlang.org)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/iam-takagi/animelist-generator)](https://github.com/iam-takagi/animelist-generator/releases)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/iam-takagi/animelist-generator/CI)](https://github.com/iamtakagi/animelist-generator/actions/workflows/ci.yml)
[![license](https://img.shields.io/github/license/iam-takagi/animelist-generator)](https://github.com/iam-takagi/animelist-generator/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/iam-takagi/animelist-generator)](https://github.com/iam-takagi/animelist-generator/issues)
[![pull requests](https://img.shields.io/github/issues-pr/iam-takagi/animelist-generator)](https://github.com/iam-takagi/animelist-generator/pulls)

## これはなに / What is this?

## 動作環境 / OS
Linux/macOS/Windows

## インストール / Installation

- Cloneします
```console
git clone https://github.com/iam-takagi/animelist-generator.git
cd animelist-generator
```

## Docker
`docker-compose.yml`
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

```console
# 起動 / Start
docker-compose up -d

# 停止 / Shutdown
docker-compose down

# ログ確認 / Logs
docker-compose logs -f
```

# 貢献 / Contribution

## Issues
バグの報告・改善点・提案等を行ってください。

## Pull Requests
開発には VSCode を使用しています。
各自で環境を準備してください。
