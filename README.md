# openapi-flask-fargate-sample-app
openapiを使ったflaskアプリのサンプル

# コマンド

## 概要
- node.jsのインストールが必要（npm or npxを使える必要がある）
- latestのオプションをつける場合はnodeの最新の安定板（LTS）をインストールしておくのが良さそう
- https://redocly.com/docs/cli/installation
- openapi-generatorを使う場合はJavaのインストールが必要

### PowerShellでnpxが実行できない場合

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Javaのインストール（winget）

```powershell
winget install EclipseAdoptium.Temurin.17.JDK
```

インストール後は**新しいターミナルを開く**と `java` コマンドが使えるようになる。

## 結合（bundle）

```
npx @redocly/cli@latest bundle openapi/openapi.yaml -o openapi/openapi_bundle.yaml
```

## 構文チェック

```
npx @redocly/cli@latest lint openapi/openapi_bundle.yaml
```

## html作成

```
npx @redocly/cli@latest build-docs openapi/openapi_bundle.yaml -o openapi/openapi.html
```

## モックサーバ作成(Prism)

- 簡易的にAPIの確認をしたい場合

```
npx -y @stoplight/prism-cli@latest mock openapi/openapi_bundle.yaml
```

### Prismのモックサーバのcurl例

```
curl --verbose 'http://127.0.0.1:4010/healthcheck'
```

### openapi genelator

```
npx @openapitools/openapi-generator-cli generate -i openapi/openapi_bundle.yaml -g python-flask -o ./flask-app
```