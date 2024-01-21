import requests

def years(runtime_of_series):
    
    list0fseries=runtime_of_series.split(" ",1)

    if len(list0fseries) >= 2:
      if list0fseries[-1] == ')':
        runtime_of_series = list0fseries[0]

      else:
        runtime_of_series=list0fseries[1]
    else:
        runtime_of_series=list0fseries[0]
        
    removed_braces=runtime_of_series.replace("(","")
    removed_braces=removed_braces.replace(")","")
    
    split_on_hyp=removed_braces.split("-")
    
    if len(split_on_hyp)==1:
        return int(split_on_hyp[0]),int(split_on_hyp[0])
    elif len(split_on_hyp)==2:
        if split_on_hyp[1]=="":
            return int(split_on_hyp[0]),-1
        else:
            return int(split_on_hyp[0]),int(split_on_hyp[1]) if split_on_hyp[1] != ' ' else -1

    
def solution(s,e):
  currentPage=1
  totalPage=0
  ans=[]
  response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?page={currentPage}")

  json = response.json()
  totalPage=json["total_pages"]
  


  for i in range(currentPage,totalPage+1):
    response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?page={i}")
    json = response.json()
    data=json["data"]

    for d in data:
      startyear,endyear=years(d["runtime_of_series"])
      if e!=-1:
      
        if s<=startyear and e>=endyear and endyear!=-1:
          # print(d['name'],d['runtime_of_series'])
          ans.append(d["name"])
      else:
        if s<=startyear and endyear==-1:
          # print(d['name'],d['runtime_of_series'])
          ans.append(d['name'])


  # print(ans)
  return sorted(ans)

    
print(solution(2006,2011))
print(solution(2019,-1))


# print(years("(2020-2021)"))
# print(years("(2020- )"))
# print(years("(2020)"))
# print(years("(I) (2006-2010)"))
# print(years("(II) (2006- )"))


    
        
        
