def question01():
    """Answer the question: Can I use a slice with a negative step to iterate through a collection backwards?"""
    print("Question 1: Can I use a slice with a negative step to iterate through a collection backwards?")

    teststring = "backwards?"
    teststring_backwards = "?sdrawkcab"
    output = ""
    for l in teststring[::-1]:
        output += l

    if output == teststring_backwards:
        print("Yes, you can!")
    else:
        print("No, you can't!")


def question02():
    """Answer the question: If so, will enumerate return the indices backwards too?"""
    print("Question 2: If so, will enumerate return the indices backwards too?")

    expected_output = [4, 3, 2, 1, 0]
    idx_output = []
    num_output = []
    for idx, num in enumerate(range(5)[::-1]):
        idx_output.append(idx)
        num_output.append(num)

    if idx_output == num_output == expected_output:
        print("Yes, it does!")
    else:
        print("No! Not what I was expecting.")


def question03():
    """Answer the question: Do for loops execute the else block if continue is used?"""
    print("Question 3: Do for loops execute the else block if continue is used?")

    for x in range(3):
        continue
    else:
        print("Yes, they do!")
        return

    print("No, they do not. Too bad.")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()
