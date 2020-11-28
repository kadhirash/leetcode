class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        peopledict, height, res = {}, [], []
        
        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledict:
                peopledict[p[0]] += (p[1], i),
            else:
                peopledict[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()     

        
        for h in height[::-1]:
            peopledict[h].sort()
            for p in peopledict[h]:
                res.insert(p[0], people[p[1]])

        return res