###################################
#check if the string starts with "The" and ends with "Spain":

import re
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)

if x:
    print("Yes We have a Match !")
else:
    print("No match")