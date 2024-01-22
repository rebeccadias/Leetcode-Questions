# Leadership teams using Rippling want to find data about salaries within their organisations. Today we will build a few data analysis tools for them.
# We first want to build a tool for a CEO who wants to compare salaries across the Sales team and the Marketing team.
# Each department head has given the CEO data about their employees, sorted by their salaries in USD, for example:


SALES = [
    "$190,000:Malik:Sales Director",
    "$160,000:Yuki:Sales Solutions Architect",
    "$160,000:Fatima:Sales Engineer",
    "$110,000:David:Regional Sales Manager",
    "$90,000:Eleanor:Account Executive",
    "$90,000:Marcus:Account Executive",
]

MARKETING = [
    "$130,000:Sophia:Marketing Director",
    "$95,000:Alice:Marketing Manager",
    "$72,000:Emma:Marketing Specialist",
    "$70,000:Olivia:Marketing Analyst",
    "$65,000:John:Marketing Coordinator",
]

#  # expect 95000

SALES2 = [
    "$190,000:Malik:Sales Director",
    "$160,000:Yuki:Sales Solutions Architect",
    "$160,000:Fatima:Sales Engineer",
    "$110,000:David:Regional Sales Manager",
    "$90,000:Eleanor:Account Executive",
]

MARKETING2 = [
    "$1,000,000:Sophia:Marketing Director",
    "$95,000:Alice:Marketing Manager",
    "$72,000:Emma:Marketing Specialist",
]

# expect 135000


SALES3 = [
]

MARKETING3 = [
    "$72,000:Emma:Marketing Specialist",
]
# expect 72000


#median of the two lists combined 
# Expected output: 95000

def Solution(SALES,MARKETING):
    median=[]
    for sale in SALES:
        s=sale.split(":")
        s[0]=s[0].replace("$","")
        s[0]=s[0].replace(",","")
        print(s[0])
        median.append(int(s[0]))
    for market in MARKETING:
        m=market.split(":")
        m[0]=m[0].replace("$","")
        m[0]=m[0].replace(",","")
        median.append(int(m[0]))
        # median.append(m[0])
    
    median.sort()
    n=len(median)
    # print("Length of the merged array",n)
    # print(n//2)
    print(median)
    if len(median)%2==0:
        #even array
        
        return (median[n//2-1]+median[n//2])/2
    else:
        #odd array
        return median[n//2]

# print(Solution(SALES,MARKETING))
# print(Solution(SALES2,MARKETING2))
# print(Solution(SALES3,MARKETING3))

def Solution2(SALES,MARKETING):
    
    Sale=[]
    Mark=[]
    
  
    for sale in SALES:
        s=sale.split(":")
        s[0]=s[0].replace("$","")
        s[0]=s[0].replace(",","")
        Sale.append(int(s[0]))
     
    
    for market in MARKETING:
        m=market.split(":")
        m[0]=m[0].replace("$","")
        m[0]=m[0].replace(",","")
        Mark.append(int(m[0]))

    i,j=0,0
    n=len(Sale)
    m=len(Mark)
    
    count=(n+m)//2
    
    while count !=0 and i!=len(Sale) and j!=len(Mark):
        if Sale[i]>Mark[j]:
            i+=1
        else:
            j+=1
        count-=1
    print(count)
    if count !=0:
        if i==len(Sale):
            while count!=0:
                j+=1
                count-=1
            return Mark[j]
        elif j==len(Mark):
            while count !=0:
                i+=1
                count-=1
            return Sale[i]
    else: 
        print(i,j) 
        if (n+m)%2==0:
            if Sale[i-1]>Mark[j]:
                return (Sale[i]+Sale[i-1])//2
            return(Sale[i]+Mark[j])//2
        else:
            return Mark[j]

print(Solution2(SALES,MARKETING))
print(Solution2(SALES2,MARKETING2))
print(Solution(SALES3,MARKETING3))

