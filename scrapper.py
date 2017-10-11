import re
import mechanize

br = mechanize.Browser()
br.open("https://www.indiapost.gov.in/VAS/Pages/trackconsignment.aspx")
# follow second link with element text matching regular expression
for f in br.forms():
    print f
    print"______________-"
