s = '12:09:01AM'

dn = s[-2:]

if dn == "AM":
    time = s[:2]
    if time == '12':
        result = '00:'+s[3:-2]
        print(result)
    else:
        print(s[:-2])
else:
    time = s[:2]
    time  = int(time)
    time = time + 12
    time = str(time)
    result = time+":"+s[3:-2]
    print(result)