import re
a = r'([1][2-9]|[2][0-3]):[0-5][0-9]'
re.search(a, "21:30")
b = r'[A-Z]\.\s[a-z]+'
re.search(b,"H. sapiens")
c = r'[0-9]{3}-[0-9]{2}-[0-9]{4}'
re.search(c,"389-05-4771")
