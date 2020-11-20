import tkinter as tk #pyperclip module necessary for copy/paste function

#Main Heading
heading = input("What would you like the heading of your website to be? ")
headingconfirmation = False
while headingconfirmation != True:
    headingconfirmation = input("Are you fine with " + heading + " as your heading?  (Y/N): ")
    if headingconfirmation == "Y":
        headingconfirmation = True
    elif headingconfirmation == "N":
        heading = input("What would you like the heading of your website to be?  ")

finalcode = ("<h1>" + heading + "</h1>" + "\n")
x = 1

while x == 1:
    elementconfirmed = False
    while elementconfirmed != True:
        element = input("What would you like next in your website?  A sub-heading or a paragraph? (H/P): ")
        if element == "P":
            element = "paragraph"
            content = input("What would you like your paragraph to say?  Please only insert one paragraph. ")
            confirmation = False
            while confirmation != True:
                confirmation = input("Are you okay with " + content + " as your paragraph?  (Y/N): ")
                if confirmation == "Y":
                    confirmation = True
                    elementconfirmed = True
                    finalcode = finalcode + ("<p>" + content + "</p>\n")
                    print("Here's your code so far:\n" + finalcode)
                    codeend = input("Would you like to continue making your webpage?  (Y/N) ")
                    if codeend == "N":
                        x = 0
                        break
                    elif codeend == "n":
                        x = 0
                        break
                elif confirmation == "N":
                    content = input("What would you like your paragraph to say? ")
        elif element == "H":
            element = "heading"
            content = input("What would you like your sub-heading to say?  Only one line of text supported. ")
            confirmation = False
            while confirmation != True:
                confirmation = input("Are you okay with " + content + " as your sub-heading?  (Y/N): ")
                if confirmation == "Y":
                    confirmation = True
                    elementconfirmed = True
                    finalcode = finalcode + ("<h2>" + content + "</h2>\n")
                    print("Here's your code so far:\n" + finalcode)
                    codeend = input("Would you like to continue making your webpage?  (Y/N) ")
                    if codeend == "N":
                        x = 0
                        break
                    elif codeend == "n":
                        x = 0
                        break
                elif confirmation == "N":
                    content = input("What would you like your sub-heading to say? Only one line of text is supported. ")

root = tk.Tk()
root.withdraw #(prevents the tkinter window from showing)
root.clipboard_append(finalcode)
print("Your code should have copied automatically.  If it did not, please copy it manually below:")
print(finalcode)
