# openapi-flask-fargate-sample-app
openapiを使ったflaskアプリのサンプル

# コマンド

## 概要
- node.jsのインストールが必要（npm or npxを使える必要がある）
- latestのオプションをつける場合はnodeの最新の安定板（LTS）をインストールしておくのが良さそう
- https://redocly.com/docs/cli/installation

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