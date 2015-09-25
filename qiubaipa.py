# -*- coding: utf-8 -*-
import urllib.request
import urllib
import re
import _thread
import threading
import time

#------模块化------#
class Spider_Model():

        def __init__(self):
                self.page = 1
                self.pages = []
                self.enable = False
        def GetPage(self, page): #输入页数，输出该页HTML的BYTE码
                print("获取第%s页..." % page)
                myUrl = 'http://www.qiushibaike.com/8hr/page/' + page
                print(myUrl)
                user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2504.0 Safari/537.36'
                headers = { 'User-Agent' : user_agent }
                req = urllib.request.Request(myUrl, headers = headers)
                try:
                        myResponse = urllib.request.urlopen(req)
                except URLError as e:
                        print(e.reason)
                        print('wrong')
                myPage = myResponse.read()
                #print(myPage)
                #encode的作用是将byte(unicode/gbk)转换成其他编码的字符串
                #decode的作用是将其他编码的字符串转换成unicode编码
                #print(type(myPage))
                f = open('test.html', 'wb')
                f.write(myPage)
                f.close()
                input('')
                unicodePage = myPage.decode('utf-8')
                print(unicodePage)
                #print(unicodePage)
                items = []
                p = re.compile(r'.*\s<!--\d{10}-->')
                myItems = p.findall(unicodePage)
                for item in myItems:
                        items.append(item)
                #        print(item)
                #print(self.pages)
                return items
# spider=Spider_Model()
# print(spider.GetPage(str(1)))
        def LoadPage(self):
                while self.enable:
                        #print(len(self.pages))
                        if len(self.pages) < 2:
                                try:
                                        myPage = self.GetPage(str(self.page))
                                        #print('test point 1')
                                        #print(self.pages)
                                        self.page+=1
                                        self.pages.append(myPage)
                                        #print(len(self.pages))
                                except Exception as e:
                                        print('except:', e)
                                        print('无法连接糗百\n')
                        else:
                                time.sleep(1)
        def ShowPage(self, nowPage, page):
                for items in nowPage:
                        print('\n Show第%d页' % page, items)
                        myInput = input()
                        if myInput == 'quit':
                                self.enable = False
                                break
        def Start(self):
                self.enable = True
                page = self.page
                t = threading.Thread(target=self.LoadPage, name='thread')
                t.start()
                #_thread.start_new_thread(self.LoadPage())
                print('testtesttesttesttesttesttesttesttesttesttesttest')
                print(self.enable)
                print(self.pages)
                while self.enable:
                        if self.pages:
                                print('fuckfuckfuckfuckfuckfuckfuck')
                                nowPage = self.pages[0]
                                print(self.pages[0])
                                del self.pages[0]
                                self.ShowPage(nowPage, page)
                                page += 1

input('press')                                
spider = Spider_Model()
spider.Start()
#html = spider.GetPage(str(1))
#items = spider.GetContent(html)
#print(items)
