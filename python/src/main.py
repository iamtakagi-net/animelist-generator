# Env
import os
Env = { 
    "HOST": os.environ["HOST"],
    "PORT": os.environ["PORT"],
}

# Flask
from flask import Flask, jsonify, request
app = Flask(__name__)

# CORS
from flask_cors import CORS
CORS(app)

# Generator
import generator

# 生成された画像(Base64)を返します
@app.route("/api/generate")
def generate():
     url = request.args.get('url')
     try:
          base64str = generator.generate(url).decode('utf-8')
          return jsonify({'base64str': base64str})
     except:
          return jsonify({'message': '無効なURL'}), 500

if __name__ == '__main__':
    app.run (
          host = Env["HOST"], 
          port = Env["PORT"], 
          debug = True
     )