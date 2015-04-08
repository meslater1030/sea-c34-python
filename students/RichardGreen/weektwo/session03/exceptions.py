import io
a = int(4)
b = int(8)

c = '45.6'
d = 'fish'


'''The functions below are work of the strings above and utilize exceptions.
The questions thay are trying to answer are to report an exception when
the substring of interest is not present against a larger string and'''


def adding_ints_exception(x, y):
    '''def of function: determine if the values are integers, if they are not
throw up a value error. regardless add the items in the end and return them'''

    try:
        x_int = int(x)
        y_int = int(y)
    except ValueError:
        print "x and y must be a integers"
    else:
        return (x_int + y_int)


def file_exception(x):
    '''function definition: This function answers the question is my file and
if so what some of its contents. If it exists show me the beginning of the file
 arguments: a file'''
    try:
        header_size = 4096
        f = open(x)
        results = f.read(header_size)
        print results
        f.close()
    except IOError:
        print "couldn't open data.txt, please check to see if it exists"
    f.close()
if __name__ == "__main__":
        print(adding_ints_exception(a, b))
        # throws a value error
        print(adding_ints_exception(c, d))
        file_exception('data.txt')
        # Throws an exception
        # file_exception('foo.txt')
