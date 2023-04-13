prompt= 'Hello select topping '
prompt += ' , enter quit to end the program'
message = ""
while message != 'quit':
      message= input(prompt)
      print(f"{message} added")