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
ProcessingClass.download_archive(dateTimeObj)

# ProcessingClass.extract_archive(filename)
# ProcessingClass.parse_insert()
