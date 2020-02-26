import random
def getRandomArray(n):
  a = random.sample(range(1, n+1), n)
  return a

#----------------------------------------------------------------

def getSortedArray(n):
  arr = []
  for i in range(n):
    arr.append(i+1)
  arr.sort(reverse=True)
  return arr

