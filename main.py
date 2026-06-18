from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "めっちゃ大吉"
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(11)]

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>これはカウントサイトです</title>
        </head>
       <meta charset="utf-8">
       <script src="myStyle.js"></script>
       <div id="click_html"></div>
       <button onclick="a()">+1</button><br>
       <button onclick="b()">-1</button><br>
       <button onclick="c()">リセット</button>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
