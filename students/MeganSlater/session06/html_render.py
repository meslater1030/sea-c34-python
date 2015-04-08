class Element(object):
    indent = "    "
    tag_name = ""

    def __init__(self, text="", **kwargs):
        if text == "":
            self.text = ""
        else:
            self.text = self.indent + "    " + text + "\n"
        self.attribute_string = " ".join([" " + key + "='" + value + "'"
                                         for key, value in kwargs.iteritems()])
        self.output = [u"%s<%s%s>\n"
                       % (self.indent, self.tag_name, self.attribute_string),
                       self.text,
                       u"%s</%s>\n" % (self.indent, self.tag_name)]

    def append(self, tag):
        self.tag = tag
        try:
            self.output.insert(-1, self.tag.output)
        except:
            self.output.insert(-1, self.indent + self.tag + "\n")

    def render(self, file_out):
        self.file_out = file_out
        flat_list = [item for inner_list in self.output for item in inner_list]
        flat_list2 = [item for inner_list in flat_list for item in inner_list]
        flat_list3 = [item for inner_list in flat_list2 for item in inner_list]
        flat_list3 = "".join(flat_list3)
        self.file_out.write(flat_list3)


class OneLineTag(Element):
    def __init__(self, text="", **kwargs):
        self.text = text
        self.attribute_string = " ".join([" " + key + "= '" + value + "'"
                                         for key, value in kwargs.iteritems()])
        self.output = [u"%s<%s%s>%s</%s>\n" % (self.indent, self.tag_name,
                       self.attribute_string, self.text, self.tag_name)]


class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.attribute_string = " ".join([" " + key + "='" + value + "'"
                                         for key, value in kwargs.iteritems()])
        self.output = [u'%s<%s%s />\n' % (
                                       self.indent,
                                       self.tag_name, self.attribute_string)]


class Html(Element):
    tag_name = "html"

    def __init__(self):
        self.output = [u"<!DOCTYPE html>\n", u"<" + self.tag_name + ">\n",
                       u"</" + self.tag_name + ">\n"]


class Head(Element):
    tag_name = "head"


class Body(Element):
    tag_name = "body"


class H(OneLineTag):
    indent = "        "

    def __init__(self, num, text):
        self.num = str(num)
        self.text = text
        self.output = [u"%s<h%s> %s"
                       u"</h%s>\n" % (self.indent, self.num, self.text,
                                      self.num)]


class P(Element):
    tag_name = "p"
    indent = "        "


class Title(OneLineTag):
    tag_name = "title"
    indent = "        "


class Meta(SelfClosingTag):
    tag_name = "meta"
    indent = "        "


class Hr(SelfClosingTag):
    tag_name = "hr"
    indent = "        "


class A(Element):
    indent = "            "

    def __init__(self, url, text):
        self.url = url
        self.text = text
        self.output = u'<a href="%s">%s</a> ' % (
            self.url, self.text)


class Ul(Element):
    tag_name = "ul"
    indent = "        "


class Li(Element):
    tag_name = "li"
    indent = "            "

    def append(self, tag):
        self.tag = tag
        try:
            self.text = self.text + self.tag
            self.output = u"%s<%s>\n%s    %s\n%s</%s>\n" % (
                self.indent, self.tag_name, self.indent, self.text,
                self.indent, self.tag_name)
        except:
            self.text = self.text + self.tag.output
            self.output = u"%s" % (
                           self.text)
