# Env
import os
env = { 
    "HOST": os.environ["HOST"],
    "PORT": os.environ["PORT"]
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
@app.route("/api/data")
def get_data():
     url = request.args.get('url')
     try:
          data = generator.get_data(url)
          return jsonify({'data': data})
     except:
          return jsonify({'message': '無効なURL'}), 500

# 生成された画像(Base64)を返します
@app.route("/api/generate")
def generate():
     url = request.args.get('url')
     try:
          title, base64Str = generator.generate(url)
          return jsonify({'title': title, 'base64Str': base64Str})
     except:
          return jsonify({'message': '無効なURL'}), 500

if __name__ == '__main__':
    app.run (
          threaded=True,
          host = env["HOST"], 
          port = env["PORT"], 
          debug = True
     )