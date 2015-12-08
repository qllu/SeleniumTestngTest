# coding=utf-8
"""
Created on 2015年10月14日
1.施設グループが追加されること
2.施設が追加されること
@author: QLLU
"""
# 导入需要的公共函数类
import time
import unittest
import sys
import os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class ChangeLanguages(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest

    def test1_change_to_japanese(self):
        global lang_url, garoon_url, default_lang
        dataoper = DataReader('QT_Common_change_languages.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 进入语言修改页面
        lang_url = WebDriver().testurl("qatest01") + "/settings/account"
        garoon_url = WebDriver().testurl("qatest01") + "/g/"
        WebDriver().geturl(lang_url)
        time.sleep(2)
        default_lang = Operations().confirm_language()
        WebDriver().click("byid", ":1")

        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":3")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().geturl(garoon_url)
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, u"ポータル"), "语言不能修改为日语"

    def test2_change_to_english(self):
        WebDriver().geturl(lang_url)
        time.sleep(2)
        WebDriver().click("byid", ":1")
        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":4")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().geturl(garoon_url)
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, "Portal"), "语言不能修改为英语"

    def test3_change_to_chinese(self):
        WebDriver().geturl(lang_url)
        time.sleep(2)
        WebDriver().click("byid", ":1")
        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":5")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().geturl(garoon_url)
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, u"门户"), "语言不能修改为中文"

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(lang_url)
            WebDriver().click("byid", ":1")
            WebDriver().click("byid", default_lang)
            WebDriver().click("byid", "form-submit-button-slash")
            print "语言已还原"
        except Exception as msg:
            print msg, "数据不能还原"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
