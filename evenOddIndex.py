from operator import indexOf


def evenOddIndex(arr,N):
  evenIndex = []
  oddIndex = []
  for element in arr:
    if indexOf(arr,element)%2==0:
      evenIndex.append(element)
    else:
      oddIndex.append(element)
  print(evenIndex)
  print(oddIndex)

arr = [3,2,5,7,1,7,4,9]
evenOddIndex(arr,len(arr))
