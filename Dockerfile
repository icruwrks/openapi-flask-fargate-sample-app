FROM python:3.11-slim

WORKDIR /app

# flask-app の依存関係をインストール（gunicornも追加）
COPY flask-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir "gunicorn>=20.1.0"

# flask-app のコードをコピー（自動生成物はそのまま）
COPY flask-app/ .

# gunicorn 用 WSGIエントリーポイントをコピー
COPY wsgi.py .

# ポートの公開
EXPOSE 8080

# gunicorn で起動
# GUNICORN_WORKERS: ワーカー数（デフォルト: 4）
CMD ["sh", "-c", "gunicorn --workers=${GUNICORN_WORKERS:-4} --bind=0.0.0.0:8080 wsgi:application"]
