class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        allIndSet = list(range(len(candidates)))
        stack = [(target, allIndSet, tuple())]
        processed = set()
        while stack:
            # print(stack)
            remTarget, remIndSet, curTuple = stack.pop()
            if remTarget == 0:
                result.append(curTuple)
            else:
                for i, nxtInd in enumerate(remIndSet):
                    nxt = candidates[nxtInd]
                    newRemTarget = remTarget - nxt
                    if newRemTarget >= 0:
                        nxtTuple = list(curTuple)
                        nxtTuple.append(nxt)
                        nxtTuple.sort()
                        nxtTuple = tuple(nxtTuple)
                        
                        if nxtTuple not in processed:
                            processed.add(nxtTuple)
                            nxtIndSet = remIndSet[:i]
                            nxtIndSet.extend(remIndSet[i + 1:])                            
                            stack.append((newRemTarget, nxtIndSet, nxtTuple))
                    else:
                        break
        
        return result