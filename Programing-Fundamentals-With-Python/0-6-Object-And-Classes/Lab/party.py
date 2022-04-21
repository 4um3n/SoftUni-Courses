class Party:
    def __init__(self):
        self.people = []


data, party = input(), Party()
while data != "End":
    party.people.append(data)
    data = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")