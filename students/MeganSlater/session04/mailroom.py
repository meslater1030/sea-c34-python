donors = {"Donor Full Name": [amount donated, second amount donated]}


def thankyous():
    userprompt = raw_input("Choose Send a Thank You or Create a Report. ")
    userprompt = userprompt.lower()

    if userprompt == "Send a Thank You":
        donorname = ""
        while donorname != "list":
            donorname = raw_input("What is the donor's full name?")
            if donorname == "list":
                for name, donation in donors:
                    print name
            elif donorname == "quit":
                thankyous()

        for name, donation in donors:
            if donorname != "name":
                donors["name"] = 0
                thankyous()
            else:
                amount = ""
                while amount.isdigit() == False:
                    amount = raw_input("How much did they donate? ")
                    if amount == "quit":
                        thankyous()
                donors["name"] = amount

        for name, donation in donors:
            print("""Thank you " + donor + " for your generous donation
                 of $" + donation ".  We couldn't do it without you!""")
        thankyous()

    elif userprompt == "Create a Report":
        for name, donation in donors:
            donation = donation.sort()
#        Sort the dictionary by total donation value
        for name, donation in donors:
            print("Donor Name, total donated, #of donations, average donation")
        thankyous()

    elif userprompt == "quit":
        exit()

    else:
        thankyous()

thankyous()
