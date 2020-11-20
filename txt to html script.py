#Main Heading
heading = input("What would you like the heading of your website to be? ")
headingconfirmation = False
while headingconfirmation != True:
    headingconfirmation = input("Are you fine with " + heading + " as your heading?  (Y/N): ")
    if headingconfirmation == "Y":
        headingconfirmation = True
    elif headingconfirmation == "N":
        heading = input("What would you like the heading of your website to be?  ")

#Configuring the second element
secondelementconfirmed = False
while secondelementconfirmed != True:
    secondelement = input("What would you like next in your website?  A sub-heading or a paragraph? (H/P): ")
    if secondelement == "P":
        secondelement = "paragraph"
        secondcontent = input("What would you like your paragraph to say?  Please only insert one paragraph. ")
        secondconfirmation = False
        while secondconfirmation != True:
            secondconfirmation = input("Are you okay with " + secondcontent + " as your paragraph?  (Y/N): ")
            if secondconfirmation == "Y":
                secondconfirmation = True
                secondelementconfirmed = True
            elif secondconfirmation == "N":
                secondcontent = input("What would you like your paragraph to say? ")
    elif secondelement == "H":
        secondelement = "heading"
        secondcontent = input("What would you like your sub-heading to say?  Only one line of text supported. ")
        secondconfirmation = False
        while secondconfirmation != True:
            secondconfirmation = input("Are you okay with " + secondcontent + " as your sub-heading?  (Y/N): ")
            if secondconfirmation == "Y":
                secondconfirmation = True
                secondelementconfirmed = True
            elif secondconfirmation == "N":
                secondcontent = input("What would you like your sub-heading to say? Only one line of text is supported. ")

#Configuring the third element
thirdelementconfirmed = False
while thirdelementconfirmed != True:
    thirdelement = input("What would you like next in your website?  A sub-heading or a paragraph? (H/P): ")
    if thirdelement == "P":
        thirdelement = "paragraph"
        thirdcontent = input("What would you like your paragraph to say?  Please only insert one paragraph. ")
        thirdconfirmation = False
        while thirdconfirmation != True:
            thirdconfirmation = input("Are you okay with " + thirdcontent + " as your paragraph?  (Y/N): ")
            if thirdconfirmation == "Y":
                thirdconfirmation = True
                thirdelementconfirmed = True
            elif thirdconfirmation == "N":
                thirdcontent = input("What would you like your paragraph to say? ")
    elif thirdelement == "H":
        thirdelement = "heading"
        thirdcontent = input("What would you like your sub-heading to say?  Only one line of text supported. ")
        thirdconfirmation = False
        while thirdconfirmation != True:
            thirdconfirmation = input("Are you okay with " + secondcontent + " as your sub-heading?  (Y/N): ")
            if thirdconfirmation == "Y":
                thirdconfirmation = True
                thirdelementconfirmed = True
            elif thirdconfirmation == "N":
                thirdcontent = input("What would you like your sub-heading to say? Only one line of text is supported. ")



#Printing the final code
print("<h1>" + heading + "</h1>")
if secondelement == "paragraph":
    print("<p>" + secondcontent + "</p>")
elif secondelement == "heading":
    print("<h2>" + secondcontent + "</h2>")

if thirdelement == "paragraph":
    print("<p>" + secondcontent + "</p>")
elif thirdelement == "heading":
    print("<h2>" + secondcontent + "</h2>")
