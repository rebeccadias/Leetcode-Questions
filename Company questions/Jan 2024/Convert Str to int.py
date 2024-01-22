# Given a string convert it into Int wihtout using any built in function like. int().

# Example 1
# s = "123"
# Outout 
# 123

#s=1&8
#output=0



def solution(s):
    s=s.strip()
    ans=0
    flag=True
    decimal=False
    res=0
    count=0
    hashmap={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
    for chars in s:
        if not chars.isdigit():
            if chars=="-":
                if flag:
                    flag=False
                else:
                    return 0
            elif chars==".":
                if not decimal:
                    decimal=True
                else:
                    return 0
            else:
                return 0
        else:
            if chars in hashmap:
                if not decimal:
                    ans=ans*10+hashmap[chars]
                else:
                    res=res*10+hashmap[chars]
                    count+=1

    if not flag:
        ans=-1*ans
    if  decimal:
        decimals=res/(10**count)
        ans+=decimals
    return ans

print(solution("123.11.11"))


