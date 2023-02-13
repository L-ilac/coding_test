h,w=map(int,input().split())
ans=0
blocks=list(map(int,input().split())) 
pivot=-1
temp_block=[]
for block in blocks:
  if block>=pivot:
  
    
    while temp_block:
      x=temp_block.pop()
      ans+= pivot-x

    pivot=block
    

  else:
    temp_block.append(block)

if not temp_block:
  print(ans)
else:
  temp_block=[blocks[-1-len(temp_block)]] + temp_block
  
  pivot=-1
  temp_block2=[]
  for block in temp_block[::-1]:
    
    if block>=pivot:
    
      
      while temp_block2:
        x=temp_block2.pop()
        ans+= pivot-x

      pivot=block
      

    else:
      temp_block2.append(block)
  
  print(ans)
