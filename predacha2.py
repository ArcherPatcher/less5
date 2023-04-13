messages=['Hello','GGGG','UTU','UwU']
def show_messages(messages):
    for message in messages:
        msg= f"Ur mess is:{message.title()}"
        print(msg)
show_messages(messages)
def send_messages(messages):
    while messages:
        current_message= messages.pop()
        sended_messages.append(current_message)
def print_sended(sended_mesage):
    print(f"Msgs send:")
    for sended_message in sended_messages:
        print(sended_messages)
sended_messages=[]
print_sended(sended_messages)
print(messages)
print(sended_messages)
send_messages(messages[:])
print(messages)
print(sended_messages)
