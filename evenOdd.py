def evenOdd(arr,N):
  even = []
  odd = []
  for element in elements:
    if (element%2)==0:
      even.append(element)
    else:
      odd.append(element)

  print(even)
  print(odd)

elements = [1,2,3,4,5,6,7,8]
evenOdd(elements,len(elements))