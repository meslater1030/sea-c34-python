def question01():
    """What happens if you open a nonexistent file in r mode?"""

    print("Question 1: What happens if you open a nonexistent file in r mode?")
    try:
        f = open("i_do_not_exist.txt", "r")
    except IOError:
        print("An I/O error is raised.")
    else:
        print("Nothing too bad, apparently.")


def question02():
    """When opening a file in 'a' mode, does the pointer need to be reset
    after writing to read from the beginning?
    """

    print("When opening a file in 'a' mode, does the pointer need to be reset"
          " after writing to read from the beginning?")
    try:
        # I have my .gitignore set up to ignore any files with 'nogit' prefix
        f = open("nogit_task8output.txt", "a+")
    except IOError:
        print("An I/O error occurred")
        return

    for i in range(3):
        f.write("This is line {}\n".format(i))

    print("If the answer is yes, nothing should appear here:")
    for line in f:
        print(line)

    print("Only after this print should the lines appear:")
    f.seek(0)
    for line in f:
        print(line)

    f.close()


if __name__ == "__main__":
    question01()
    print("")
    question02()
