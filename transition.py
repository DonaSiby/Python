import array
def transition(array,n):
  start = 0;
  end = n-1;
  while(start<=end):
    mid = (start+end)//2
    if(array[mid]==1):
      if(mid==0 or array[mid-1]==0):
        return mid;
      end = mid-1;
    else:
      start = mid+1;
  return -1;

arr=[0,0,0,0,1];
print("Transition point is  ",transition(arr,len(arr)));

    


