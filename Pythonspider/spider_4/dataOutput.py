# coding:utf-8

import codecs,json

class dataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_json(self):
        if self.datas is None:
            return
        with open("baike.json","w",encoding="utf-8") as fp:
            json.dump(self.datas,fp = fp,indent = 4,ensure_ascii = False)

    def output_html(self):
        if  self.datas is None:
            return
        with codecs.open("daike.html","w",encoding="utf-8") as f:
            f.write("<html>")
            f.write("<head><meat charset = 'utf-8'/></head>")
            f.write("<body>")
            f.write("<table>")
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>" % data.get("url").encode("utf-8"))
                f.write("<td>%s</td>" % data.get("title"))
                f.write("<td>%s</td>" % data.get("summary"))
                f.write("<tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")