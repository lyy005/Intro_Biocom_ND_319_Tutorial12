import re

timeFile = open("MilitaryTime.txt","r")
speciesFile = open("Species.txt","r")
SSNFile = open("SSN.txt","r")


time = re.compile("(12:\d\d|13:\d\d|14:\d\d|15:\d\d|16:\d\d|17:\d\d|18:\d\d|19:\d\d|20:\d\d|21:\d\d|22:\d\d|23:\d\d|24:00)")
species = re.compile("[A-Z]\.\s\w+")
SSN = re.compile("\d\d\d-\d\d-\d\d\d")

print("Matches in MilitaryTime.txt")
for ln in timeFile:
    ln.strip()
    if re.search(time, ln) is not None:
        print(ln)
        
print("Matches in Species.txt")
for ln in speciesFile:
    ln.strip()
    if re.search(species, ln) is not None:
        print(ln)
        
print("Matches in SSN.txt")
for ln in SSNFile:
    ln.strip()
    if re.search(SSN, ln) is not None:
        print(ln)
        
timeFile.close()
speciesFile.close()
SSNFile.close()
