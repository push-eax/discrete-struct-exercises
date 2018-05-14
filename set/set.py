"""
Kiernan Roche
CSCI 317 
Professor David Keil
Competency 2.1b: Set implementation

This is an implementation of a set in Python, as a class with the following methods:
- addElement:       Adds an element to the set, if it does not already exist in the set.
- removeElement:    Removes an element from the set, if it exists in the set.
- elementExists:    Returns true if an element exists in the set, false otherwise.
- getElements:      Returns the elements in the set.

"""

class Set:
    def __init__(self):
        self.elements = []                  # Elements are stored internally in an array.
                                            # Python arrays are variable-length and not prone to overflow, unlike C and Java in which arrays are fixed-length.
    def addElement(self, element):
        if not self.elementExists(element):    # If the element does not exist in the set,
            self.elements.append(element)   # add it.
    
    def removeElement(self, element):       
        if self.elementExists(element):     # If the element already exists in the set,
            self.elements.remove(element)   # remove it.
    
    def elementExists(self, element):
        return element in self.elements

    def getElements(self):
        return self.elements                # The contents of the set.

def main():
    print("Testing set class.")
    
    set = Set()                             # Instantiate the set object.
    set.addElement(1)                       # Add 1 to the set.
    set.addElement(2)                       # Add 2 to the set.
    set.addElement(3)                       # Add 3 to the set.

    print(set.getElements())    # [1, 2, 3]
    print(set.elementExists(1)) # True
    print(set.elementExists(2)) # True
    print(set.elementExists(4)) # False
    set.removeElement(1)
    print(set.getElements())    # [2, 3]
    print(set.elementExists(1)) # False


if __name__ == "__main__":
    main()
