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
if isinstance(dateTimeObj, object):
    filename = ProcessingClass.download_archive(dateTimeObj)
elif isinstance(dateTimeObj, dict):
    filename = ProcessingClass.download_archive(dateTimeObj[0], dateTimeObj[1])
else:
    filename = ProcessingClass.download_archive()
# ProcessingClass.extract_archive(filename)
# ProcessingClass.parse_insert()
