from script.moviespider import MovieInfo
from script.bookspider import  BookInfo
from script.poster import DouBanPoster
from io import BytesIO
import  logging
import  re
import flask
from flask import send_file

app = flask.Flask(__name__)

def main(url):

    if re.search(r"https://movie.douban.com/subject/.+?",url):

        doubaninfo = MovieInfo(url)
    elif re.search(r"https://book.douban.com/subject/.+?",url):
        doubaninfo = BookInfo(url,show_detail_error=True)

    else:
        logging.error("网址不符合要求 请输入如下样式:\n"
                      "电影:https://movie.douban.com/subject/xxxxx\n"
                      "书籍:https://book.douban.com/subject/xxxxx")
        exit(1)

    dbposter = DouBanPoster()

    dbposter.backgroundImg({"bgImgPath": BytesIO(doubaninfo.bgimg_content)})

    dbposter.titleAndDescribe({
        "title": {"name": doubaninfo.title_name},
        "alias": {"name": doubaninfo.alias_name},
        "describe": doubaninfo.describe
    })

    dbposter.rateAndDescribe({"rate": doubaninfo.rate,
                              "rating_people": doubaninfo.rating_people,
                              "star_rate": doubaninfo.star_rate,
                              "star_rate_details": doubaninfo.star_rate_details,
                              "betterthan": doubaninfo.betterthan
                              })

    dbposter.urlQRimg({"url": doubaninfo.url})

    # dbposter.template_image.show()

    dbposter.savePoster(doubaninfo.title_name)

    api_img_path = '/www/wwwroot/douban.sunguoqi.com/douban/DoubanPoster/result/' + doubaninfo.title_name + '_poster.png'

    return api_img_path


@app.route('/',methods=['get'])
def img():
    url = flask.request.args.get('url')
    img = main(url)

    return send_file(img)


if __name__ == '__main__':

    # main('https://movie.douban.com/subject/26794435/?from=playing_poster')
    main('https://movie.douban.com/subject/1291843/')
    print("程序执行完毕！")



