prompt='Hello, enter your age and see price'
prompt += '\n"enter quit to close prog"' 
prices={'3<=':'free',[4:12]:'10$','>=12':'15$',}
age= ""
while age!= quit:
     age= input(prompt)
     for k, v in prices.items():
        k=int(k)
if age == k:       
       print(v.title())