import sys
from processingclass import ProcessingClass
from dateutil import parser

if len(sys.argv) <= 1:
    print("Error: Not enough arguments")
    sys.exit(0)
elif len(sys.argv) == 2:
    dateTimeObj = parser.parse(sys.argv[1], dayfirst=True)
else:
    dateTimeObj = [
        parser.parse(sys.argv[1], dayfirst=True),
        parser.parse(sys.argv[2], dayfirst=True)
    ]
if isinstance(dateTimeObj, dict):
    filename = ProcessingClass.download_archive()
filename = ProcessingClass.download_archive()
ProcessingClass.extract_archive(filename)
ProcessingClass.parse_insert()
