"""värdet=None, dvs pekar inte på någonting."""
"""En kö kan implementeras likadant som en stack. Nu vill man ha en pekare i var ände på kön.
Den som hette top i stacken kallar vi first och så har vi last som pekar på sista noden. Där ska nämligen nya noder stoppas in."""
"""single linked"""
"""OBS gör dequeue o sen enqueue, ska funka med trollkarlsprogrammet"""

class Node():
    def __init__(self, value):
        self.data = value   #värdet?
        self.next = None    #pekar på next


class LinkedQ():
    def __init__(self):
        self.__first = None   #haller reda pa den forsta noden i kon
        self.__last = None      #pekar ut den sista

    def __str__(self):
        return str(self.__first.data) + "\n"

    # def __str__(self, next_in_q):
    #     return str(next_in_q) + "\n"


    def enqueue(self, x):
        """Stoppar in x sist i kön """
        new_node = Node(x)  #skapar noden
        if self.__first == None: #tom kö

            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = new_node


    def dequeue(self):      #ta bort element 0, visar
        """Plockar ut och returnerar det som står först i kön """
        if self.__first!= None:
            new_node = self.__first.data
            self.__first = self.__first.next
            return new_node
        else:
            return 'Bugg'


    def isEmpty(self):      #kolla om kon ar tom
        """Returnerar True om kön är tom, False annars """
        if self.__first == None:
            return True
        else:
            return False

    def peek(self):
        "Tittar på nästa värde i kön utan att plocka ut det. dvs. första värdet"
        #if self.__first is not None:
        next_in_q = self.__first.data

        return next_in_q



