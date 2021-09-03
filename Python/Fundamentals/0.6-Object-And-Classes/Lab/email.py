class Email:
    def __init__(self, sender, receiver, content, is_send = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send
    

    def send(self):
        self.is_send = True
    

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


data, emails = input(), []
while data != "Stop":
    s, r, c = data.split()
    email = Email(s, r, c)
    emails.append(email)
    data = input()

indexes = [int(n) for n in input().split(', ')]
for i in range(len(emails)):
    if i in indexes:
        emails[i].send()
    print(emails[i].get_info())
