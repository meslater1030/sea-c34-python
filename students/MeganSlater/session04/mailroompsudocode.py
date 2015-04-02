donors = {"Donor Full Name": [amount donated, second amount donated]}


def thankyous():
    """ask user wether to send thank you or create report.  Take action based
    on input
    """
    userprompt = ask_for_input("Choose Send a Thank You or Create a Report. ")
    userprompt = userprompt.lower_case()

    if userprompt == "Send a Thank You":
        donorname = empty_string
        while donorname does not equal "list":
            donorname = ask_for_input("What is the donor's full name?")
            """if the user doesn't know any names the user will input 'list' and we
            print all the names and let them choose one
            """
            if donorname == "list":
                for name, donation in donors:
                    print name
            """if instead of sending a thank you the user wants to start over they can
            type quit and go back to the beginning
            """
            elif donorname == "quit":
                thankyous()
        """If the user enters an unknown name we add that name to the dictionary
            and return to the beginning.
        """
        for name, donation in donors:
            if donorname does not equal any dictionary "name":
                donors["name"] = 0
                thankyous()
                """If the donor name is in the dictionary we prompt the user for
                a donated amount and enter it into the dictionary"""
            else:
                amount = ""
# keep asking the user about how much was donated until they enter a number
                while amount_is_not_a_number:
                    amount = ask_for_input("How much did they donate? ")
                    # if the user wants out here they can go to the beginning
                    if amount == "quit":
                        thankyous()
                donors["name"] = amount
        """Once an amount has been added the user will receive a print
        out of an email for every donor and return to the beginning.
        """
        for name, donation in donors:
            print("""Thank you " + donor + " for your generous donation
                 of $" + donation ".  We couldn't do it without you!""")
        thankyous()
# If the user wants a report at the beginning we give them one
    elif userprompt == "Create a Report":
        totaldonated = []
        total = 0
# add up the total donations for each donor and put it in a list
        for name, donation in donors:
            for i in donation:
                total += i
            totaldonated.append(total)
# sort that list highest to lowest
        totaldonated.sort()
        donortotal = 0
# match the list against dictionary entries and print them higest to lowest
        for total in totaldonated:
            for name, donation in donors:
                for i in donation:
                    donortotal += i
                if donortotal == total:
                    print(name, /tab total, /tab length(donations), /tab total/length(donations))
# return to the beginning
        thankyous()
# The user can exit this function from the beginning prompt by typing quit
    elif userprompt == "quit":
        exit()
# If the user enters something unexpected they are asked to try again.
    else:
        print("I'm sorry, I don't understand.  Try again. ")
        thankyous()

thankyous()
