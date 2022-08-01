##############################################################################
#
#Replace the first two occurrences of a white-space character with the digit 9:
#
##############################################################################
import re
txt="The Rain in the Spain"
x=re.sub("\s","9",txt,2)
print(x)