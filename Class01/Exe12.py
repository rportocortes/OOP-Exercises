class Contacts:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone):
        self.contacts[name] = phone

    def search(self, name):
        return self.contacts[name]

    def remove(self, name):
        del self.contacts[name]

    def list_contacts(self):
        for name in sorted(self.contacts):
            print(f"Name: {name}")

c1 = Contacts()
c1.add("Rafael", 923923993)
c1.add("Ana", 454545454)
c1.add("Gabriel", 343434)
print(c1.search("Rafael"))
c1.remove("Ana")
c1.list_contacts()
