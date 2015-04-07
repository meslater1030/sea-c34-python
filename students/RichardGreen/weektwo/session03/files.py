s = "Do something every day that you dont want to do"


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
        print "couldn't open file, please check to see if it exists"
    f.close()


def write_to_a_file(s, y):
    '''function definition: This function will take a string and write it to a
file. It will also take raw input from the user.
arguments: a string, x: and y a file to write out to '''

    f = open(y, 'w')
    print "I'll add content from the string s: %s into the file %s " % (s, y)
    print "Is there any other content you'd like to add? please enter it below"

    line1 = raw_input("Add:")
    f.write(line1)
    f.write("Text added: \n")
    f.write(s)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    file_exception('data.txt')
    write_to_a_file(s, 'results.txt')
