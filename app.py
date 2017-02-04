import tornado.ioloop
import tornado.web

def data_append(number,datetime,text):
    f=open("sms/data.txt","a")
    f.write(number)
    f.write(" ")
    f.write(datetime)
    f.write(" ")
    f.write(text)
    f.write("\n")
    f.close()

def getSMSList():
    sms_list=[]
    f=open("sms/data.txt","r")
    sms_list=f.readlines()
    f.close()
    return sms_list

def get_sms_list_sort(sms_list):
    sms_list_sort=[]
    k=len(sms_list)
    print k
    for i in range(k):
        sms_list_sort.append(sms_list[(k-1-i)])
        #print sms_list[k-1-i]
    return sms_list_sort

class MainHandler(tornado.web.RequestHandler):
    def get(self):
<<<<<<< HEAD
        if self.get_argument("get_token")=="52599d9d8aa170e7ec476a70b1bf1c93":
=======
        if self.get_argument("myid")=="XXXXXXXXX md5sum code XXXXXXXXXXX":
>>>>>>> b3942465ac4a3806a6f3b0872a8b3537ad136fea
            sms_list = getSMSList()
            self.render("templates/index.html",smslist=get_sms_list_sort(sms_list))

    def post(self):
<<<<<<< HEAD
        if self.get_argument("post_token")=="42062e9f759545e081c2b85fa77d591f":
=======
        if self.get_argument("myid")=="XXXXXXXXX another md5sum code XXXXXXXXXXX":
>>>>>>> b3942465ac4a3806a6f3b0872a8b3537ad136fea
            number=self.get_argument("number").encode("utf-8")
            datetime=self.get_argument("datetime").encode("utf-8")
            text=self.get_argument("text").encode("utf-8")
            data_append(number,datetime,text)
            data=number+" "+datetime+" "+text
            #print data+"IS SENT"

application = tornado.web.Application([
    (r"/test", MainHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "static/css"}),
    (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "static/fonts"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/js"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

