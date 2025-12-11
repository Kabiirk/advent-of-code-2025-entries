import re

day4 = open("day4.txt", "r")

#combine all entries in 1 string
entries = ""
for line in day4:
    entries += line
day4.close()

#Split into list with empty line as delimiter which is essentially 2 newlines
passports = entries.split("\n\n") # => [string1, string2, ......]

for i in range(len(passports)):
    passports[i] = passports[i].replace("\n"," ") #each password is now just a 1-liner string with fields separated by space
    # What the above line does is
    # 
    # "hcl:#888785
    # hgt:164cm byr:2001 iyr:2015 cid:88   ===>   "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"
    # pid:545766238 ecl:hzl eyr:2022"

def validPassport(l):
    #Find Values of fields and put them in a list
    byr = re.findall(r'byr:(\d+)',l)
    iyr = re.findall(r'iyr:(\d+)',l)
    eyr = re.findall(r'eyr:(\d+)',l)
    hgt = re.findall(r'hgt:(\d+)(\w+)',l) #This gives a list of Tuple i.e. [(value1, value2)]
    hcl = re.findall(r'hcl:(#\w+)',l)
    ecl = re.findall(r'ecl:(\w+)',l)
    pid = re.findall(r'pid:(\d+)',l)

    is_false = []

    #byr
    if(len(byr)!=0):
        if(int(byr[0])>=1920 and int(byr[0])<=2002):
            pass
        else:
            is_false.append("byr_False")
    else:
        is_false.append("byr_empty")

    #iyr
    if(len(iyr)!=0):
        if(int(iyr[0])>=2010 and int(iyr[0])<=2020):
            pass
        else:
            is_false.append("iyr_False")
    else:
        is_false.append("iyr_empty")

    #eyr
    if(len(eyr)!=0):
        if(int(eyr[0])>=2020 and int(eyr[0])<=2030):
            pass
        else:
            is_false.append("eyr_False")
    else:
        is_false.append("eyr_empty")

    #hgt (This is a Tuple, so tuple indexed first before indexing values)
    if(len(hgt)!=0):
        if( (hgt[0][1]=="cm" and int(hgt[0][0])>=150 and int(hgt[0][0])<=193) or (hgt[0][1]=="in" and int(hgt[0][0])>=59 and int(hgt[0][0])<=76) ):
            pass
        else:
            is_false.append("hgt_False")
    else:
        is_false.append("hgt_empty")

    #hcl
    if(len(hcl)!=0):
        if(len(hcl[0])==7):
            pass
        else:
            is_false.append("hcl_False")
    else:
        is_false.append("hcl_empty")

    #ecl
    if(len(ecl)!=0):
        if( ecl[0]=="amb" or ecl[0]=="blu" or ecl[0]=="brn" or ecl[0]=="gry" or ecl[0]=="grn" or ecl[0]=="hzl" or ecl[0]=="oth"):
            pass
        else:
            is_false.append("ecl_False")
    else:
        is_false.append("ecl_empty")

    #pid
    if(len(pid)!=0):
        if(len(pid[0])==9):
            pass
        else:
            is_false.append("pid_False")
    else:
        is_false.append("pid_empty")

    if(len(is_false)==0):
        return True
    else:
        return False

counter = 0
for passport in passports:
    if(validPassport(passport)):
        counter+=1

print(counter)