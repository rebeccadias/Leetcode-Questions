class Solution(object):

  def isAnagram(self, s, t):
  
    s_hashmap={}
    t_hashmap={}
    for i in range(len(s)):
      print(s[i])
      if s[i] not in s_hashmap:
          s_hashmap[s[i]]=1
      else:
          s_hashmap[s[i]]+=1

    for j in range(len(t)):
      if t[j] not in t_hashmap:
          t_hashmap[t[j]]=1
      else:
          t_hashmap[t[j]]+=1
    print(s_hashmap,t_hashmap)
    if s_hashmap==t_hashmap:
        return True
    return False
