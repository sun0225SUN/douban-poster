# 声明

本项目基于该开源项目 https://github.com/sadjjk/DoubanPoster 开发，使用 Flask 框架构建

# 使用

```markdown

![](https://douban.sunguoqi.com?url=XXX)

```

```html
<img src="https://douban.sunguoqi.com?url=XXX">

```

注意：XXX为豆瓣图书/电影URL

# 示例

```markdown

![](https://douban.sunguoqi.com?url=https://movie.douban.com/subject/1291843/)

```

![](https://douban.sunguoqi.com?url=https://movie.douban.com/subject/1291843/)

# 开发

## 安装依赖

```
pip install -r requirements.txt
```

## 配置

```bash
export FLASK_APP=main
```

## 运行

```py
flask --app ./main.py run
```

