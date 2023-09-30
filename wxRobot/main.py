from fake_useragent import UserAgent
import itchat
import requests
import re
from bs4 import BeautifulSoup

import SparkApi

ua = UserAgent()
user_agent = ua.random


@itchat.msg_register("Text", isGroupChat=True)
def group_reply(msg):
    """
    自动回复
    """
    if msg["isAt"]:
        # index = msg_has_xingzuo(msg.content)
        # if index >= 0:
        #     return "@%s\u2005%s" % (
        #         msg["ActualNickName"],
        #         get_xingzuo(index) or "收到：" + msg["Text"],
        #     )
        # elif "新闻" in msg.content:
        #     return "@%s\u2005%s" % (
        #         msg["ActualNickName"],
        #         getNews() or "收到：" + msg["Text"],
        #     )
        if 'quit' in msg.content:
            return 0
        st = spark_talk()
        question = re.search(r'\u2005(.+)', msg.content).group(1)
        answer = st.get_spark_answer(question)
        return "@%s\u2005%s" % (
            msg["ActualNickName"],
            answer or "收到：" + msg["Text"],
        )


class spark_talk(object):
    def __init__(self):
        """
        初始化
        """
        self.appid = "f349c6f3"
        self.api_secret = "NTRkYjM1NTlmM2Y2ZTE2MjE3NjdmYTNj"
        self.api_key = "b2e656f09287222be0c82b670ba10421"
        # self.domain = "general"
        self.domain = "generalv2"    # v2.0版本
        # self.Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"
        self.Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

        self.text = []

    def getText(self, role, content):
        """
        获取回复的文本
        """
        jsoncon = {}
        jsoncon["role"] = role
        jsoncon["content"] = content
        self.text.append(jsoncon)
        return self.text

    def getlength(slef, text):
        """
        获取文本长度
        """
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length

    def checklen(self, text):
        """
        文本长度超过8000 删除之前的内容
        """
        while self.getlength(text) > 200:
            del text[0]
        return text

    def get_spark_answer(self, content):
        """
        启动对话
        """
        self.text.clear
        while 1:
            question = self.checklen(self.getText("user", content))
            SparkApi.answer = ""
            SparkApi.main(
                self.appid,
                self.api_key,
                self.api_secret,
                self.Spark_url,
                self.domain,
                question,
            )
            self.getText("assistant", SparkApi.answer)
            return str((self.text[1]['content']))


def get_xingzuo(index):
    """
    获取星座内容
    """
    star_emoji = "\U0001F31F"
    constellation_list = [
        "cancer",
        "scorpio",
        "taurus",
        "capricorn",
        "libra",
        "gemini",
        "aquarius",
        "pisces",
        "aries",
        "leo",
        "virgo",
        "sagittarius",
    ]
    apiurl = "https://www.xzw.com/fortune/" + constellation_list[index] + "/"
    headers = {"user-agent": user_agent}
    result = requests.get(url=apiurl, headers=headers).text
    soup = BeautifulSoup(result, "html.parser")
    targe_dls = soup.find_all("dl")
    info_short = targe_dls[1]
    info_long = soup.find("div", class_="c_cont")

    sign = info_short.find("dt").find("img")["title"]
    date = info_short.find("h4").find("small").text
    comprehensive_value = stars_count(
        int(
            info_short.select_one('li:contains("综合运势：")')
            .find("em")["style"]
            .split(":")[1]
            .split("px")[0]
            .strip()
        )
    )
    comprehensive_stars = "综合运势：{}\n".format(comprehensive_value * star_emoji)
    love_value = stars_count(
        int(
            info_short.select_one('li:contains("爱情运势：")')
            .find("em")["style"]
            .split(":")[1]
            .split("px")[0]
            .strip()
        )
    )
    love_stars = "爱情运势：{}\n".format(love_value * star_emoji)
    career_value = stars_count(
        int(
            info_short.select_one('li:contains("事业学业：")')
            .find("em")["style"]
            .split(":")[1]
            .split("px")[0]
            .strip()
        )
    )
    career_stars = "事业运势：{}\n".format(career_value * star_emoji)
    wealth_value = stars_count(
        int(
            info_short.select_one('li:contains("财富运势：")')
            .find("em")["style"]
            .split(":")[1]
            .split("px")[0]
            .strip()
        )
    )
    wealth_stars = "财富运势：{}\n".format(wealth_value * star_emoji)
    health_index = "健康指数：{}\n".format(
        info_short.select_one('li:contains("健康指数：")').text.split("：")[
            1].strip()
    )
    negotiation_index = "商谈指数：{}\n".format(
        info_short.select_one('li:contains("商谈指数：")').text.split("：")[
            1].strip()
    )
    lucky_color = "幸运颜色：{}\n".format(
        info_short.select_one('li:contains("幸运颜色：")').text.split("：")[
            1].strip()
    )
    lucky_number = "幸运数字：{}\n".format(
        info_short.select_one('li:contains("幸运数字：")').text.split("：")[
            1].strip()
    )
    compatible_sign = "速配星座：{}\n".format(
        info_short.select_one('li:contains("速配星座：")').text.split("：")[
            1].strip()
    )
    comment = "短评：{}\n".format(
        info_short.find("li", class_="desc").text.split("：")[1].strip()
    )
    comprehensive_desc = "综合运势：{}\n".format(
        info_long.find("strong", class_="p1").find_next(
            "span").text[:-5].strip()
    )
    love_desc = "爱情运势：{}\n".format(
        info_long.find("strong", class_="p2").find_next("span").text.strip()
    )
    career_desc = "事业学业：{}\n".format(
        info_long.find("strong", class_="p3").find_next("span").text.strip()
    )
    wealth_desc = "财富运势：{}\n".format(
        info_long.find("strong", class_="p4").find_next("span").text.strip()
    )
    health_desc = "健康运势：{}\n".format(
        info_long.find("strong", class_="p5").find_next("span").text.strip()
    )

    xingzuo_response = "\n{}\t{}\n{}{}{}{}{}{}{}{}{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        sign,
        date,
        comprehensive_stars,
        love_stars,
        career_stars,
        wealth_stars,
        health_index,
        negotiation_index,
        lucky_color,
        lucky_number,
        compatible_sign,
        comment,
        comprehensive_desc,
        love_desc,
        career_desc,
        wealth_desc,
        health_desc,
    )
    return xingzuo_response


def msg_has_xingzuo(msg):
    signs = ["巨蟹", "天蝎", "金牛", "摩羯", "天秤", "双子",
             "水瓶", "双鱼", "白羊", "狮子", "处女", "射手"]
    for item in signs:
        if item in msg:
            return signs.index(item)
    return -1


def stars_count(num):
    if num >= 0 and num <= 20:
        return 1
    elif num >= 21 and num <= 40:
        return 2
    elif num >= 41 and num <= 60:
        return 3
    elif num >= 61 and num <= 80:
        return 4
    elif num >= 81 and num <= 100:
        return 5
    else:
        return 0


def getNews():
    news = "\n"
    url = "https://user.guancha.cn/?s=wapsyfw"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": user_agent,
        "Connection": "keep-alive",
        "Host": "user.guancha.cn",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://m.guancha.cn/",
    }
    result = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    news_ul = soup.find("ul", class_="fengwen-most-hot")
    li_list = news_ul.findAll("li")
    for item in li_list:
        a = item.find("a")
        title = a.get_text(strip=True)
        link = "https://user.guancha.cn/" + a["href"]
        news += "{}\n{}\n".format(title, link)
    return news


itchat.auto_login(loginCallback=True, enableCmdQR=2,
                  exitCallback=True, hotReload=True)
itchat.run()
