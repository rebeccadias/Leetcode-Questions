def solution(ip_address):
    ans=[]
    flag=True
    for i in ip_address:
        flag=True
        list_of_octet=i.split(".")
        first=list_of_octet[0]
        #list_of_octect=["234","345","344","89"]
        if len(list_of_octet)!=4:
            ans.append(-1)
            continue
        # print(list_of_octet)
        for j in list_of_octet:
            # print(j.isdigit())
            if j.isdigit() and int(j)>255:
                ans.append(-1)
                flag=False
                break
            
         
        if flag:
       
            first=int(first)
            if 0<=first<=127:
                ans.append(1)
            elif 128<=first<=191:
                ans.append(2)
            elif 192<=first<=223:
                ans.append(3)
            elif 224<=first<=239:
                ans.append(4)
            else:  
                ans.append(5)
    return ans
    
print(solution(["123.211.102.13","271.142.67.142","225.217.132.58"]))

print(solution(["15.231.268.11","234.11.89.45","249.255.12.91","178.102.163.34"]))
            
            
