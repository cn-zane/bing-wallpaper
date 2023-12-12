# coding=UTF-8
import requests
from urllib import request
import os
import datetime
import json
from PIL import Image


def print_hi():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    res_html = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&uhd=1", headers=headers)
    res = res_html.content.decode("utf-8")
    json_res = json.loads(res)
    url = json_res["images"][2]["url"]
    # url截取
    url = url[:url.find('&')];
    picture_title = json_res["images"][2]["copyright"]
    end_date = json_res["images"][2]["enddate"]
    # 截取标题
    picture_title = picture_title[:picture_title.rfind('(')].strip()
    # 拼接url
    url = "https://www.bing.com{}".format(url)
    # 获取当前日期信息
    now = datetime.datetime.now()
    curr_year = now.year
    curr_date = datetime.datetime.strftime(now, "%Y-%m")
    webp_date = datetime.datetime.strftime(now, "%Y-%m-%d")
    # 保存的路径(自动创建年月目录)
    path = "/mydata/projects/bing-wallpaper/download"
    webp_path = "/mydata/nginx/images"
    month_dir_path = path + "/{}/{}".format(curr_year, curr_date)

    # 月份路径(不存在则创建)
    if not os.path.exists(month_dir_path):
        os.makedirs(month_dir_path)

    # webp月份路径(不存在则创建)
    if not os.path.exists(webp_path):
        os.makedirs(webp_path)

    # 图片下载路径
    pic_down_load_path = month_dir_path + "/{}-{}.jpg".format(picture_title, end_date)
    webp_pic_down_load_path = webp_path + "/{}.webp".format(webp_date)

    # 图片不存在->下载
    if not os.path.exists(pic_down_load_path):
        request.urlretrieve(url, pic_down_load_path)
        print(picture_title, "下载成功")

    # 图片格式转换为webp保存
    if not os.path.exists(webp_pic_down_load_path):
        im = Image.open(pic_down_load_path)
        im.save(webp_pic_down_load_path, "webp", quality=20)
        print(webp_pic_down_load_path, "图片格式转换为webp完成")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi()
