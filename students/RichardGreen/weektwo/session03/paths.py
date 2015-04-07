import os


def path_info():
    '''function definition: determine the path I'm currently in and list off
the available files in my path. Arguments: None. Just be in current working
directory where you have permissions
.'''

    path = os.getcwdu()

    print "My current path is: %s " % (path)
    print "The files in the current path are:"
    print(os.listdir(path))

if __name__ == "__main__":
    path_info()
