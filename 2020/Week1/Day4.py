lst = open('input.txt', 'r').read().split('\n\n')
for i in range(len(lst)):
    lst[i] = lst[i].replace('\n', ' ')

dlst = []
for el in lst:
    d = {}
    tlst = el.split(" ")
    for i in tlst:
        a, b = i.split(":")
        d[a] = b
    dlst.append(d)
#zorg dat het dictionaries worden.

def Day4_1st():
    res = 0
    check = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    for d in dlst:
        Bo = True
        for el in check:
            if el not in d:
                Bo = False
        if  Bo:
            res += 1
    print(res)
    return

def Day4_2nd():
    res = 0
    for d in dlst:
        #d = {'ecl': 'hzl', 'hgt': '184cm', 'iyr': '2018', 'byr': '2001', 'pid': '453480077', 'eyr': '2025', 'hcl': '#a97842'}
        Bo = True
        ######################
        if not 'ecl' in d:
            Bo = False
        else:
            ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if not d['ecl'] in ecl:
                Bo = False
        #print(Bo)
        ######################
        if not 'pid' in d:
            Bo = False
        else:
            if len(d['pid']) != 9:
                Bo = False
        #print(Bo)
        ######################
        if not 'eyr' in d:
            Bo = False
        else:
            if not 2020 <= int(d['eyr']) <= 2030:
                Bo = False
        #print(Bo)
        ######################
        if not 'hcl' in d:
            Bo = False
        else:
            h = d['hcl']
            s = set('ghijklmnopqrstuvwxyz').intersection(d['hcl'])
            if h[0] != '#' or len(h) != 7 or len(s) != 0:
                Bo = False
        #print(Bo)
        ######################
        if not 'byr' in d:
            Bo = False
        else:
            if not 1920 <= int(d['byr']) <= 2002:
                Bo = False
        #print(Bo)
        ######################
        if not 'iyr' in d:
            Bo = False
        else:
            if not 2010 <= int(d['iyr']) <= 2020:
                Bo = False
        #print(Bo)
        ######################
        if not 'hgt' in d:
            Bo = False
        else:
            if 'in' in d['hgt']:
                if not 59 <= int(d['hgt'][0:2]) <= 76:
                    Bo = False
            elif 'cm' in d['hgt']:
                if d['hgt'][2] == 'c':
                    Bo = False
                elif not 150 <= int(d['hgt'][0:3]) <= 193:
                    Bo = False
            else:
                Bo = False
        #print(Bo)
        if Bo:
            res += 1
    print(res)
    return

Day4_2nd()
        
                
