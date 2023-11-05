def LargestFrequency(arr):
  frequency = {};
  for element in arr:
    if element in frequency:
      frequency[element] += 1;
    else:
      frequency[element] = 1;
  sorted(frequency);
  print(frequency);
  print("Largest frequency : ",max(frequency.values()));

arr = [1,1,2,2,2,3,3,3,4,4,4];
LargestFrequency(arr)
