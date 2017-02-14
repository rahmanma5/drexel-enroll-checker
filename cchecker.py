
from lxml import html
import requests
import time

courses = ['',
'',
'',
'',
'']

# List guide:
# ['CRN', 'Subject Code', 'Course Number', 'Section', 'Credits', 'Title', 'Campus', 'Instructor(s)', 'Instruction Type', 'Instructio      n M$
# ['31084', '101', '  3.00', 'University City', 'Lecture', '60', '\r\n\t\t\t\t\t\t\t\t']
# ['ANTH', '003', 'Introduction to Cultural Diversity', 'Judith A Storniolo', 'Face To Face', '13', 'Click on the link below to see       tex$

print ' '
print '[Class Enrollment Checker v0.1]'

text_file = open("Output.txt", "a")
for page in courses:
        web = requests.get(page)
        tree = html.fromstring(web.content)

        headers = tree.xpath('//td[@class="tableHeader"]/text()')
        even = tree.xpath('//td[@class="even"]/text()')
        odd = tree.xpath('//td[@class="odd"]/text()')

        headers = tree.xpath('//td[@class="tableHeader"]/text()')
        even = tree.xpath('//td[@class="even"]/text()')
        odd = tree.xpath('//td[@class="odd"]/text()')

        print 'Course name: ' + odd[2]
        print 'Enrollment: ' + odd[5] + '/' + even[5]
        print 'Instructor: ' + odd[3]
        print ' '
        text_file.write(time.strftime("[%m/%d/%Y %H:%M:%S]") + " Course: " + odd[2] + "\n")
        text_file.write(time.strftime("[%m/%d/%Y %H:%M:%S]") + " Enroll: " + odd[5] + '/' + even[5] + "\n")

text_file.write(" \n")
text_file.close()



