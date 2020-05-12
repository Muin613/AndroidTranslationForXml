# _*_ coding: utf-8 _*_

from selenium import webdriver
import time

__author__ = 'Silent_Coder'
__date__ = '2019/3/12 22:41'

HOME_PAGE = 'https://www.xuexi.cn/'
VIDEO_LINK = 'https://www.xuexi.cn/a191dbc3067d516c3e2e17e2e08953d6/b87d700beee2c44826a9202c75d18c85.html?pageNumber=39'
LONG_VIDEO_LINK = 'https://www.xuexi.cn/f65dae4a57fe21fcc36f3506d660891c/b2e5aa79be613aed1f01d261c4a2ae17.html'
LONG_VIDEO_LINK2 = 'https://www.xuexi.cn/0040db2a403b0b9303a68b9ae5a4cca0/b2e5aa79be613aed1f01d261c4a2ae17.html'
TEST_VIDEO_LINK = 'https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html'
SCORES_LINK = 'https://pc.xuexi.cn/points/my-points.html'
LOGIN_LINK = 'https://pc.xuexi.cn/points/login.html'
ARTICLES_LINK = 'https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(executable_path=r'C:\Users\M\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe',options=options)


def login_simulation():

    """模拟登录"""
    # 方式一：使用cookies方式
    # 先自己登录，然后复制token值覆盖
    # cookies = {'name': 'token', 'value': 'e7d27cbc9ce74f908909f9b3942d0ebe'}
    # browser.add_cookie(cookies)

    # 方式二：自己扫码登录
    browser.get(LOGIN_LINK)
    browser.maximize_window()
    browser.execute_script("var q=document.documentElement.scrollTop=1000")
    time.sleep(25)
    browser.get(HOME_PAGE)
    print("模拟登录完毕\n")


def watch_videos():
    """观看视频"""
    browser.get(VIDEO_LINK)
    time.sleep(5)
    videos = browser.find_elements_by_xpath("//div[@class='Iuu474S1L6y5p7yalKQbW grid-cell']")
    print(videos)
    spend_time = 0

    for i, video in enumerate(videos):
        if i > 6:
            break
        video.click()
        all_handles = browser.window_handles
        browser.switch_to_window(all_handles[-1])
        browser.get(browser.current_url)
        time.sleep(3)
        # 获取视频时长
        outter = browser.find_element_by_xpath("//div[@class='outter']")
        outter.click()
        video1 = browser.find_element_by_xpath("//span[@class='duration']")
        video_duration_str = video1.text
        video_duration = int(video_duration_str.split(':')[0]) * 60 + int(video_duration_str.split(':')[1])
        # # 保持学习，直到视频结束
        time.sleep(video_duration + 3)
        spend_time += video_duration + 3
        browser.close()
        browser.switch_to_window(all_handles[0])

    # if spend_time < 3010:
    #     browser.get(LONG_VIDEO_LINK)
    #     browser.execute_script("var q=document.documentElement.scrollTop=850")
    #     try:
    #         browser.find_element_by_xpath("//div[@class='outter']").click()
    #     except:
    #         pass
    #
    #     # 观看剩下的时间
    #     time.sleep(3010 - spend_time)
    # browser.get(TEST_VIDEO_LINK)
    # time.sleep(3010 - spend_time)
    print("播放视频完毕\n")


def read_articles():
    """阅读文章"""
    browser.get(ARTICLES_LINK)
    time.sleep(3)

    articles = browser.find_elements_by_class_name("grid-cell")
    print(articles)
    time.sleep(13)

    for index, article in enumerate(articles):
        if index > 7:
            break
        article.click()
        all_handles = browser.window_handles
        browser.switch_to_window(all_handles[-1])
        browser.get(browser.current_url)
        for i in range(0, 2000, 100):

            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(1)
        for i in range(2000, 0, -100):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(1)
        time.sleep(20)
        browser.close()
        browser.switch_to_window(all_handles[0])
    print("阅读文章完毕\n")


def get_scores():
    """获取当前积分"""
    browser.get(SCORES_LINK)
    time.sleep(5)
    gross_score = browser.find_element_by_xpath("//span[@class='my-points-points my-points-red']")\
        .text
    today_score = browser.find_element_by_xpath("//span[@class='my-points-points']").text
    print("当前总积分：" + str(gross_score))
    print("今日积分：" + str(today_score))
    print("获取积分完毕，即将退出\n")


if __name__ == '__main__':
    login_simulation()  # 模拟登录
    # read_articles()     # 阅读文章
    # watch_videos()      # 观看视频
    get_scores()        # 获得今日积分
    browser.quit()