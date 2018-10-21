import sys
from processingclass import ProcessingClass
from dateutil import parser

if len(sys.argv) <= 1:
    dateTimeObj = False
elif len(sys.argv) == 2:
    dateTimeObj = parser.parse(sys.argv[1], dayfirst=True)
else:
    dateTimeObj = [
        parser.parse(sys.argv[1], dayfirst=True),
        parser.parse(sys.argv[2], dayfirst=True)
    ]
processingClass = ProcessingClass(dateTimeObj)
filename = processingClass.download_archive()
processingClass.extract_archive(filename)
processingClass.parse_insert()
