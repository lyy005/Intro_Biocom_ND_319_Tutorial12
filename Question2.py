import re

testset1=['13:40','11:20','22:00','24:49']

regextime=r"(12)|(13)|(14)|(15)|(16)|(17)|(18)|(19)|(20)|(21)|(22)|(23)|(24)\:[0-9]{2}"
regextime2=re.compile(regextime)
filter(regextime2.match,testset1)


testset2='H. sapien','D. rerio','YYstutorial'

regexGenus=r"[A-Z]?\. [a-z]+"
regexGenus2=re.compile(regexGenus)
filter(regexGenus2.match,testset2)

testset3=['1wo-rd-me22','food','123-45-6789','555-55-5555']

regexSSN=r"[0-9]{3}\-[0-9]{2}\-[0-9]{4}"
regexSSN2=re.compile(regexSSN)
filter(regexSSN2.match,testset3)