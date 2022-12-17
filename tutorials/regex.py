""" .   - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
"""

import re

text = """
Mr. Schafer
615-555-7164
173 Main St., Springfield RI 55924
dave1martin@gmail.com

Mr Smith
800-555-5669
969 High St., Atlantis VA 34075
charles.harris@university.edu

Ms Martin-White
560.555.5153
806 1st St., Faketown AK 86847
laura-williams@my-work.net

Mrs. Robinson
900*555*9340
826 Elm St., Epicburg NE 10671
corey.jefferson@my-work.net

Mr. T 
714-555-7405
212 Cedar St., Sunnydale CT 74983
jenni123-ferwhite@hotmail.com

"""

def print_regex(query, text):
    pattern = re.compile(query)
    matches = pattern.findall(text)
    print(matches)


query = r'\d\d\d.\d\d\d.\d\d\d\d'
print_regex(query, text)
# ['615-555-7164', '800-555-5669', '560-555-5153', '900*555*9340']

query = r'\d{3}-\d{3}-\d{4}'
print_regex(query, text)
# ['615-555-7164', '800-555-5669']

query = r'\d{3}[*.]\d{3}[*.]\d{4}'
print_regex(query, text)
# ['560.555.5153', '900*555*9340']

query = r'[89]00.\d{3}.\d{4}'
print_regex(query, text)
# ['800-555-5669', '900*555*9340']

query = r'Mr\.?\s[A-Z]\w*'
print_regex(query, text)
# ['Mr. Schafer', 'Mr Smith', 'Mr. T']

query = r'(?:Mr|Ms|Mrs)\.?\s[A-Z]\w*'
print_regex(query, text)
# ['Mr. Schafer', 'Mr Smith', 'Mr. T']
# without ?:
# ['r', 'r', 's', 'rs', 'r']
# https://stackoverflow.com/questions/64058532/difference-between-re-findall-and-re-finditer-when-using-groups-in-regex

query = r'[a-zA-Z0-9._]+@[a-zA-Z-]+\.(?:com|edu|net)'
print_regex(query, text)
# ['dave1martin@gmail.com', 'charles.harris@university.edu', 
# 'williams@my-work.net', 'corey.jefferson@my-work.net', 
# 'ferwhite@hotmail.com']

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov"""

query = r'https?://(?:www\.)?\w+\.\w+'
print_regex(query, urls)