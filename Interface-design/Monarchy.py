""" designing a Monarchy interface: 

"""
class Member:
    def __init__(self, name: str):
        self.name = name
        self.alive = True
        self.children = []
    def die(self):
        self.alive = False

class Monarchy:
    def __init__(self, headName : str):
        self.head = Member(headName)
        self.members = {headName: self.head}
    def birth(self, childName, parentName):
        #first of all parent must exist!!
        if self.members.get(parentName) is None:
            return 
        #child must also not exist before birth
        elif self.members.get(childName):
            return
        else:
            child = Member(childName)
            self.members[childName] = child
            parent = self.members.get(parentName)
            parent.children.append(child)
        return 
    def death(self, name: str):
        #the person must first be in existence:
        if self.members.get(name) is None:
            return
        person = self.members.get(name)
        person.die()
        return
    def getOrderOfSuccession(self):
        order = []
        self._dfs(self.head, order)
        return order

    def _dfs(self, parent: Member, order):
        if parent.alive:
            order.append(parent.name)
        for child in parent.children:
            self._dfs(child, order)
        return

if __name__ == "__main__":
    myMonarchy = Monarchy('Jake')
    myMonarchy.birth('Catherine','Jake')
    myMonarchy.birth('Jane','Catherine')
    myMonarchy.birth('Farah','Jane')
    myMonarchy.birth('Tom','Jake')
    myMonarchy.birth('Celine','Jake')
    myMonarchy.birth('Mark','Catherine')
    myMonarchy.birth('Peter','Celine')
    print(myMonarchy.getOrderOfSuccession())
    myMonarchy.death('Jake')
    myMonarchy.death('Jane')
    print(myMonarchy.getOrderOfSuccession())

