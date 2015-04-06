class Element(object):
    indent = ""
    tag_name = "html"

    def __init__(self):
        self.lines = [u"<!DOCTYPE html>\n", u"<" + self.tag_name + ">\n",
                      u"</" + self.tag_name + ">\n"]

    def append(self, words):
        self.words = words
        self.lines.pop()
        self.lines.extend(self.words)
        self.lines.append(u"\n</" + self.tag_name + ">\n")

    def render(self, file_out):
        self.file_out = file_out
        [self.file_out.write(item) for item in self.lines]


class Html(object):
    def __init__(self, ind=""):
        self.ind = ind
        self.lines = [u"<!DOCTYPE html>\n", u"<html>\n", u"</html>\n"]

    def append(self, tag):
        self.tag = tag
        self.lines.insert(-1, self.tag.lines)
        interim_list = []
        for inner_list in self.lines:
            if isinstance(inner_list, list) == True:
                for item in inner_list:
                    interim_list.append(item)
            else:
                interim_list.append(inner_list)
        self.lines = interim_list

    def render(self, file_out):
        self.file_out = file_out
        [self.file_out.write(item) for item in self.lines]


class Body(object):
    def __init__(self, ind=u"    "):
        self.ind = ind
        self.lines = [self.ind + u"<body>\n", self.ind + u"</body>\n"]

    def append(self, tag):
        self.tag = tag
        try:
            self.lines.insert(-1, self.tag.output)
        except:
            self.lines.insert(-1, self.ind * 2 + self.tag + "\n")
        interim_list = []
        for inner_list in self.lines:
            if isinstance(inner_list, list) == True:
                for item in inner_list:
                    interim_list.append(item)
            else:
                interim_list.append(inner_list)
        self.lines = interim_list


class Head(object):
    def __init__(self, ind="    "):
        self.ind = ind
        self.lines = [self.ind + u"<head>\n", self.ind + u"</head>\n"]

    def append(self, tag):
        self.tag = tag
        self.lines.insert(-1, self.tag.output)


class Title(object):
    def __init__(self, text, ind="        "):
        self.text = text
        self.output = u'%s <title>%s</title>\n' % (ind, self.text)


class Meta(object):
    def __init__(self, charset="", ind="        "):
        self.charset = charset
        self.output = u'%s <meta charset="%s"/>\n' % (ind, self.charset)


class P(object):
    def __init__(self, text, style="", ind="        "):
        self.text = text
        self.style = style
        self.output = u'%s<p style="%s">%s</p>\n' % (ind, self.style, self.text)


class Hr():
    def __init__(self, ind="        "):
        self.ind = ind
        self.output = self.ind + u"<hr />\n"


class A(object):
    def __init__(self, url, text, ind=""):
        self.ind = ind
        self.url = url
        self.text = text
        self.output = u'%s<a href="%s">%s</a> ' % (ind, self.url, self.text)


class H(object):
    def __init__(self, num, text, ind="        "):
        self.num = num
        self.text = text
        self.output = u'%s<h%s>%s</h%s>\n' % (ind, self.num,
                                              self.text, self.num)


class Ul(object):
    def __init__(self, id="", style="", ind="        "):
        self.id = id
        self.style = style
        self.ind = ind
        self.output = [self.ind + u"<ul id='" + self.id + u"'>\n", self.ind +
                       u"</ul>\n"]

    def append(self, tag):
        self.tag = tag
        self.output.insert(-1, self.tag.output)
        interim_list = []
        for inner_list in self.output:
            if isinstance(inner_list, list) == True:
                for item in inner_list:
                    interim_list.append(item)
            else:
                interim_list.append(inner_list)
        self.output = interim_list


class Li(object):
    def __init__(self, text="", style="", ind="            "):
        self.text = text
        self.style = style
        self.ind = ind
        self.output = [self.ind + u"<li style='" + self.style + "'>",
                       self.text, u"</li>\n"]

    def append(self, text):
        self.text = text
        try:
            self.output.insert(-1, self.text.output)
        except:
            self.output.insert(-1, self.text)
