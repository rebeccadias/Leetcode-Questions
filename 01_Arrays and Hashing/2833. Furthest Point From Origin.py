class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        hashmap={}
        left_moves,right_moves=0,0
        underscores=0

        for move in moves:
            if move=="L":
                if move not in hashmap:
                    hashmap[move]=1
                else:
                    hashmap[move]+=1
            if move =="R":
                if move not in hashmap:
                    hashmap[move]=1
                else:
                    hashmap[move]+=1
            if move=="_":
                if move not in hashmap:
                    hashmap[move]=1
                else:
                    hashmap[move]+=1
        print(hashmap)

        if "L" in hashmap:
            left_moves=hashmap['L']
        if "R" in hashmap:
            right_moves=hashmap['R']
        if "_" in hashmap:
            underscores=hashmap['_']

        if left_moves>right_moves:
            ans=int(underscores) + int(left_moves-right_moves)
            return ans
          
        elif right_moves>left_moves:
            ans=int(underscores) + int(right_moves-left_moves)
            return ans
        else:
            return underscores
