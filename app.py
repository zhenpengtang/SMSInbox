import tornado.ioloop
import tornado.web

sms_data="sms/data.txt"

def data_append(number,datetime,text):
    f=open(sms_data,"a")
    f.write(number)
    f.write(" ")
    f.write(datetime)
    f.write(" ")
    f.write(text)
    f.write("\n")
    f.close()

def getSMSList():
    sms_list=[]
    f=open(sms_data,"r")
    sms_list=f.readlines()
    f.close()
    sms_list.reverse()
    return sms_list

def get_the_test_sms(sms_list):
    sms_test_list=[]
    for sms in sms_list:
        if sms.find("5359071") != -1:
			sms_test_list.append(sms)
    return sms_test_list


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument("get_token")=="get_token_md5":
            sms_list = getSMSList()
            self.render("templates/index.html",smslist=sms_list)

    def post(self):
        if self.get_argument("post_token")=="post_token_md5":
            number=self.get_argument("number").encode("utf-8")
            datetime=self.get_argument("datetime").encode("utf-8")
            text=self.get_argument("text").encode("utf-8")
            data_append(number,datetime,text)
            data=number+" "+datetime+" "+text
            #print data+"IS SENT"

class SmsHandler(tornado.web.RequestHandler):
    def get(self):
        sms_list=getSMSList()
	sms_test_list=get_the_test_sms(sms_list)
	self.render("templates/index.html",smslist=sms_test_list)

application = tornado.web.Application([
    (r"/test", MainHandler),
	(r"/showyoursms",SmsHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "static/css"}),
    (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "static/fonts"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/js"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

