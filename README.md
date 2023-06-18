# db-e-commerce-system

db-e-commerce-system for 2023 NCCU DBMS

- front-end : Vue 3
- back-end : Flask
- database : MySQL

## Contributors

|  系級  |  組員  |    學號    |   工作分配  |  貢獻百分比  |
|-------|--------|------------|------------|------------ |
| 資碩一 | 許軒祥 | 111753122  | Flask、Vue |     14%     |
| 資碩一 | 陳筱詩 | 111753201  | Flask      |     14%     |
| 資碩二 | 巫謹任 | 111753124  | Vue        |     14%     |
| 資碩二 | 彭怡靜 | 111753106  | Flask      |     14%     |
| 資碩一 | 吳家瑋 | 111753141  | Vue        |     14%     |
| 資科三 | 楊皓丞 | 109703008  | Vue        |     14%     |
| 資科三 | 許軒祥 | 109703013  | Flask      |     14%     |


## Prerequisites

- python 3.8.8
- node v18.16.0
- MySQL
- docker (optional)

## MySQL

- 建立 database: ecommerce
- 在 *./flask-back-end/app.py*下修改 `'mysql+pymysql://<user>:<password>@localhost:3306/ecommerce'`
- 有提供 MySQL docker-compose 可以使用 `docker-compose up -d`

## Flask

- 進到 _./flask-back-end_ 下 `cd flask-back-end`
- 建議使用 virtualenv 建立虛擬環境
- 安裝套件 `pip install -r requirements.txt`
- 啟動 `flask run`
- http://localhost:5000/api/

## Vue 3

- 進到 _./vue3-front-end_ 下 `cd vue3-front-end`
- 安裝套件 `npm install`
- 啟動 `npm run dev`
- http://localhost:5173/

# Flask

## 主要的套件

- pymsql -> connect to MySQL
- flask-restful -> restful api
- flask-SQLAlchemy -> ORM
- flask-marshmallow -> serialization

## Model

- User <使用者>
- Product <商品>
- OrderTable <訂單>
- CartItem <購物車>
- Market <賣場>

## RESTful API

- /api/login
- /api/signup
- /api/users/...
- /api/markets/...
- /api/products/...
- /api/cart/...
- /api/order/...

# Vue 3

## UI 套件

- Vuetify

## 主要套件

- axios -> call api

- vue-router -> manage route

## Pages

- /home
- /sign-in
- /sign-up
- /profile
- /carts
- /order
- /market
- /manage/product
- /manage/order

# ER-Model

![](./images/er-model.png)

# Relational Schema

![](./images/relational-schema.jpg)
