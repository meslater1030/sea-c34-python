import codecs
import cStringIO

#  step 1


class Element(object):
    def __init__(self, ind=u""):
        self.ind = ind
        self.html_list = [u"<!DOCTYPE html>\n", u"<html>\n", u"</html>\n"]

    def append(self, words):
        self.words = words
        self.html_list.pop()
        self.html_list.extend(self.words)
        self.html_list.append(u"\n</html>\n")

    def render(self, file_out):
        self.file_out = file_out
        for item in self.html_list:
            self.file_out.write(item)


def render(page, filename):
    f = cStringIO.StringIO()
    page.render(f)
    f.reset()
    print f.read()
    f.reset()
    codecs.open(filename, 'w', encoding="utf-8").write(f.read())

page = Element()
page.append(u"Here is a paragraph of text -- there could be more of them,"
            "but this is enough to show that we can do some text")
page.append(u"And here is another piece of text -- you should be able to"
            "add any number")
render(page, u"test_html_output1.html")

# step 2


class Html(object):
    def __init__(self, ind=""):
        self.ind = ind
        self.html_list = ["<!DOCTYPE html>\n", "<html>\n", "</html>\n"]

    def append(self, element):
        self.element = element
        self.html_list.pop()
        self.html_list.extend(self.element.lines)
        self.html_list.append("</html>\n")

    def render(self, file_out):
        self.file_out = file_out
        for item in page.html_list:
            self.file_out.write(item)


class Body(object):
    def __init__(self, ind="    "):
        self.ind = ind
        self.lines = [self.ind + "<body>\n", self.ind + "</body>\n"]

    def append(self, tag):
        self.tag = tag
        self.lines.pop()
        try:
            self.lines.extend(self.tag.output)
        except:
            self.lines.extend(self.ind * 2 + self.tag + "\n")
        self.lines.append(self.ind + "</body>\n")


class P(object):
    def __init__(self, text, style="", ind="        "):
        self.text = text
        self.style = style
        self.output = '%s<p style="%s">%s</p>\n' % (ind, self.style, self.text)
page = Html()
body = Body()
body.append(P(u"Here is a paragraph of text -- there could be more of them,"
            " but this is enough to show that we can do some text"))
body.append(P(u"And here is another piece of text -- you should be able to add"
            " any number"))
page.append(body)
render(page, u"test_html_output2.html")


# step 3


class Head(object):
    def __init__(self, ind="    "):
        self.ind = ind
        self.lines = [self.ind + "<head>\n", self.ind + "</head>\n"]

    def append(self, tag):
        self.tag = tag
        self.lines.pop()
        self.lines.extend(self.tag.output)
        self.lines.append(self.ind + "</head>\n")


class Title(object):
    def __init__(self, text, ind="        "):
        self.text = text
        self.output = '%s <title>%s</title>\n' % (ind, self.text)

page = Html()
head = Head()
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(P(u"Here is a paragraph of text -- there could be more of them,"
            " but this is enough to show that we can do some text"))
body.append(P(u"And here is another piece of text -- you should be able to add"
            " any number"))
page.append(body)
render(page, u"test_html_output3.html")


# step 4

page = Html()
head = Head()
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(P(u"Here is a paragraph of text -- there could be more of them,"
            "but this is enough to show that we can do some text",
              style=u"text-align: center; font-style: oblique;"))
page.append(body)
render(page, u"test_html_output4.html")

# step 5


class Hr():
    def __init__(self, ind="        "):
        self.ind = ind
        self.output = self.ind + "<hr />\n"

page = Html()
head = Head()
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(P(u"Here is a paragraph of text -- there could be more of them,"
            "but this is enough to show that we can do some text",
              style=u"text-align: center; font-style: oblique;"))
body.append(Hr())
page.append(body)
render(page, u"test_html_output5.html")

# step 6


class A(object):
    def __init__(self, url, text, ind=""):
        self.ind = ind
        self.url = url
        self.text = text
        self.output = '%s<a href="%s">%s</a> ' % (ind, self.url, self.text)


page = Html()
head = Head()
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(P(u"Here is a paragraph of text -- there could be more of them, "
            "but this is enough to show that we can do some text",
              style=u"text-align: center; font-style: oblique;"))
body.append(Hr())
body.append(u"And this is a ")
body.append(A(u"http://google.com", "link"))
body.append(u"to google")
page.append(body)
render(page, u"test_html_output6.html")

# step 7


class H(object):
    def __init__(self, num, text, ind="        "):
        self.num = num
        self.text = text
        self.output = '%s<h%s>%s</h%s>\n' % (ind, self.num, self.text, self.num)


class Ul(object):
    def __init__(self, id="", style="", ind="        "):
        self.id = id
        self.style = style
        self.ind = ind
        self.output = [self.ind + "<ul id='" + self.id + "'>\n", self.ind + "</ul>\n"]

    def append(self, list_item):
        self.list_item = list_item
        self.output.pop()
        self.output.extend(self.list_item.output)
        self.output.append(self.ind + "</ul>\n")


class Li(object):
    def __init__(self, text="", style="", ind="            "):
        self.text = text
        self.style = style
        self.ind = ind
        self.output = [self.ind + "<li style='" + self.style + "'>", self.text, "</li>\n"]

    def append(self, text):
        self.text = text
        self.output.pop()
        try:
            self.output.extend(self.text.output)
        except:
            self.output.extend(self.text)
        self.output.append("</li>\n")

page = Html()
head = Head()
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(H(2, u"PythonClass - Class 6 example"))
body.append(P(u"Here is a paragraph of text -- there could be more of them, "
            "but this is enough to show that we can do some text",
              style=u"text-align: center; font-style: oblique;"))
body.append(Hr())
list = Ul(id=u"TheList", style=u"line-height:200%")
list.append(Li(u"The first item in a list"))
list.append(Li(u"This is the second item", style="color: red"))
item = Li()
item.append(u"And this is a ")
item.append(A(u"http://google.com", u"link"))
#item.append(u"to google")
list.append(item)
body.append(list)
page.append(body)
render(page, u"test_html_output7.html")

# step 8


class Meta(object):
    def __init__(self, charset="", ind="        "):
        self.charset = charset
        self.output = '%s <meta charset="%s"/>\n' % (ind, self.charset)
page = Html()
head = Head()
head.append(Meta(charset=u"UTF-8") )
head.append(Title(u"PythonClass = Revision 1087:"))
page.append(head)
body = Body()
body.append(H(2, u"PythonClass - Class 6 example") )
body.append(P(u"Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text",
style=u"text-align: center; font-style: oblique;"))
body.append(Hr())
list = Ul(id=u"TheList", style=u"line-height:200%")
list.append(Li(u"The first item in a list") )
list.append(Li(u"This is the second item", style="color: red") )
item = Li()
item.append(u"And this is a ")
item.append(A(u"http://google.com", "link") )
item.append(u"to google")
list.append(item)
body.append(list)
page.append(body)
render(page, u"test_html_output8.html")
