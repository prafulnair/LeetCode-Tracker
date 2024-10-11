




def runLengthEncoding(s:str):
    if s == "":
        return s
    
    counter = 0
    char = s[0]
    result = ""

    for i in range(len(s)):
        if s[i] == char:
            counter+=1
        elif s[i]!= char:   
            result = result + str(counter)+ char
            char = s[i]
            counter = 1

    result = result + str(counter+1) + char
    
    return result

print(runLengthEncoding("aaaabbbccca"))
