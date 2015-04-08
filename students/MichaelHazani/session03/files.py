import io


def readself():
    """can a function open the file it's in and read it?"""
    f = io.open('files.py', encoding='utf-8')
    selfref = f.read()
    f.close()
    print(selfref)

    for line in selfref:
        print line

# readself()
# result: yes! Ungainly but printed!
# Sweet lord, gotta find out how to format soon


def readonly():
    """can python write to a read-only file?"""
    f = io.open('cantwrite.me', 'w', encoding='utf-8')
    for i in range(10):
        f.write("I can totally write to a read-only file!")

readonly()

# result: nope, it adheres to privileges!
# IOError: [Errno 13] Permission denied: 'cantwrite.me'
