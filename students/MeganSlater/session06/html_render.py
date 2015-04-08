class Element(object):
    indent = "    "
    tag_name = "html"

    def __init__(self, text="", **kwargs):
        self.text = text
        self.attribute_string = " ".join([" " + key + "= '" + value + "'"
                                         for key, value in kwargs.iteritems()])
        self.output = [u"<%s%s>\n"
                       % (self.tag_name, self.attribute_string),
                       self.text + "\n", u"</%s>\n" % (self.tag_name)]

    def append(self, tag):
        self.tag = tag
        try:
            self.output.insert(-1, self.tag.output)
        except:
            self.output.insert(-1, self.tag + "\n")

    def render(self, file_out):
        self.file_out = file_out
        count = 0
        multiplier = 1
        while count < len(self.output):
            interim_list = []
            for inner_list in self.output:
                if isinstance(inner_list, list) == True:
                    for item in inner_list:
                        if isinstance(item, list) == True:
                            interim_list.append(item)
                        else:
                            map(interim_list.append(self.indent * multiplier +
                                item), inner_list)
                else:
                    interim_list.append(inner_list)
                    count += 1
            multiplier += 1
            self.output = interim_list
        [self.file_out.write(item) for item in self.output]


class OneLineTag(Element):
    def __init__(self, text="", **kwargs):
        self.text = text
        self.attribute_string = " ".join([" " + key + "= '" + value + "'"
                                         for key, value in kwargs.iteritems()])
        self.output = [u"<" + self.tag_name + self.attribute_string + ">" + self.text +
                       u"</" + self.tag_name + u">\n"]


class SelfClosingTag(Element):
    def __init__(self):
        self.output = [u"<" + self.tag_name + u" />\n"]


class Html(Element):
    def __init__(self):
        self.output = [u"<!DOCTYPE html>\n", u"<" + self.tag_name + ">\n",
                       u"</" + self.tag_name + ">\n"]


class Head(Element):
    tag_name = "head"


class Body(Element):
    tag_name = "body"


class H(OneLineTag):
    def __init__(self, num, text):
        self.num = str(num)
        self.text = text
        self.output = [u"<h%s> %s"
                       u"</h%s>\n" % (self.num, self.text, self.num)]


class P(Element):
    tag_name = "p"


class Title(OneLineTag):
    tag_name = "title"


class Meta(SelfClosingTag):
    def __init__(self, charset=""):
        self.charset = charset
        self.output = u'<meta charset="%s"/>\n' % (self.charset)


class Hr(SelfClosingTag):
    tag_name = "hr"


class A(Element):
    def __init__(self, url, text):
        self.url = url
        self.text = text
        self.output = u'<a href="%s">%s</a> ' % (self.url, self.text)


class Ul(Element):
    tag_name = "ul"


class Li(OneLineTag):
    tag_name = "li"

    def append(self, tag):
        self.tag = tag
        try:
            self.text = self.text + self.tag
            self.output = [u"<" + self.tag_name + self.attribute_string + ">" + self.text +
                       u"</" + self.tag_name + u">\n"]
        except:
            self.text = self.text + self.tag.output
            self.output = [u"<" + self.tag_name + self.attribute_string + ">" + self.text +
                       u"</" + self.tag_name + u">\n"]
