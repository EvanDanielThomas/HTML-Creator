import tkinter as tk #pyperclip module necessary for copy/paste function

finalcode = "<!DOCTYPE html>\n<html>\n"

finalcode = finalcode + "<header>\n"
title = input("What would you like the title of your webpage to be?   This is the text that shows at the top of the tab when you open it.  ")
titleconfirmation = "N"
while titleconfirmation != "Y":
    titleconfirmation = input("Are you sure you want " + title + " to be your heading? (Y/N): ")
    if titleconfirmation == "N":
        title = input("What would you like the title of your webpage to be?   This is the text that shows at the top of the tab when you open it.  ")

finalcode = finalcode + "<title>" + title + "</title>\n</header>\n"


finalcode = finalcode + "<body>\n"
#Main Heading
heading = input("What would you like the heading of your website to be?  This will the the large text displayed at the top of your webpage.  ")
headingconfirmation = False
while headingconfirmation != True:
    headingconfirmation = input("Are you fine with " + heading + " as your heading?  (Y/N): ")
    if headingconfirmation == "Y":
        headingconfirmation = True
    elif headingconfirmation == "N":
        heading = input("What would you like the heading of your website to be?  ")

finalcode = finalcode + ("<h1>" + heading + "</h1>" + "\n")
x = 1

while x == 1:
    elementconfirmed = False
    while elementconfirmed != True:
        element = input("What would you like next in your website?  A sub-heading, a paragraph, or a list? (H/P/L): ")
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
        elif element == "L":
            listtype = input("Would you like a bulleted or numbered list? (B/N): ")
            if listtype == "B":
                finalcode = finalcode + "<ul>\n"
                content = " "
                while listtype == "B" and content != "*ABORT*":
                    content = input("What would you like this bullet to say?  Type *ABORT* if you'd like to stop adding bullets. ")
                    if content == "*ABORT*":
                        finalcode = finalcode + "</ul>\n"
                        print("Here's your code so far: " + finalcode)
                        break
                    finalcode = finalcode + "\t<li>" + content + "</li>\n"
            if listtype == "N":
                finalcode = finalcode + "<ol>\n"
                content = " "
                while listtype == "N" and content != "*ABORT*":
                    content = input("What would you like this bullet to say?  Type *ABORT* if you'd like to stop adding bullets. ")
                    if content == "*ABORT*":
                        finalcode = finalcode + "</ol>\n"
                        break
                    finalcode = finalcode + "\t<li>" + content + "</li>\n"
                
finalcode = finalcode + "</body>\n</html>"

root = tk.Tk()
#root.withdraw #(prevents the tkinter window from showing)
root.clipboard_append(finalcode)

outF = open("code.html", "w")
outF.writelines(finalcode)
outF.close()

print("Your code should also have also copied to your clipboard automatically.  If it did not, please copy it manually below:")
print(finalcode)
