"5 funktioner för syntaxregler"
# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...


#rutan.atom
#rutan.num
#rutan.down ()-grupp

from linkedQFile import LinkedQ

import sys

from molgrafik import *

#Varje ruta motsvaras av ett objekt:


class Syntaxfel(Exception):
    pass



atomlist = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
            "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
            "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
            "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",
            "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa",
            "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",
            "Ds", "Rg", "Cn", "Fl", "Lv"]



""""FORMEL"""
# <formel>::= <mol> \n

def read_formel(q):

    q.enqueue("\n") #vaktecken, lägger längst bak i kön
    mol = read_mol(q)


    if q.peek() != "\n": # kön ej tom

        raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))

    return mol


"""MOLECULE"""
# <mol>   ::= <group> | <group><mol>

def read_mol(q):
    mol = read_group(q)

    next = q.peek()

    if next == ")":
        return mol

    # ifall det kommer en till mol
    if next.isalpha() or next == "(":
        mol.next = read_mol(q) # pekare till nästa molekyl

    return mol




"""GROUP"""
# <group> ::= <atom> |<atom><num> | (<mol>) <num>

#kolla vad vi får ha , itne vad vi inte söker
#raisa felmeddelanden på rätt ställe
def read_group(q):

    rutan = Ruta()   # skapar en tom ruta


    next = q.peek() # """Nästa gång den kallas - hur ska den peka på nästa?"""


    #< atom > | < atom > < num > |

    # atom -> stor bokstav
    if next.isalpha():

        atom(q, rutan)       # atom pga båda cases innehålller atom
        next = q.peek()


        if next is not None and next.isdigit():      #kolla ifall number, jsdigit() pga string
            num(q, rutan)


        return rutan



    # ( < mol >) < num >
    # vänsterparantes

    if next == "(":

        q.dequeue()        # för att få det inuti parentesen
        rutan.down = read_mol(q)# skapar pekare till det som är down
        next = q.peek()

        if next == ")":
            q.dequeue()
            if q.peek() is not None and q.peek().isdigit(): # kollar num
                num(q, rutan)
                return rutan

            else:
                raise Syntaxfel("Saknad siffra vid radslutet " + printQueue(q))


        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")


    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))



    # När readgroup är klar returnerar den rutan till anropet





"""ATOM"""
#< atom >::= < LETTER > | < LETTER > < letter >


def atom(q, rutan):

    atom_name = q.peek() #stor bokstav
    upper_case_l(q, rutan)

    next = q.peek()


    if next is not None and next.islower():
        q.dequeue()
        atom_name += next
        rutan.atom = atom_name        # värde på rutan ex. He
        #rutan.next = rutan.atom

    if atom_name not in atomlist:
        raise Syntaxfel("Okänd atom vid radslutet " + printQueue(q))



"""UPPER CASE LETTER"""
#< LETTER >::= A | B | C | ... | Z


def upper_case_l(q, rutan):
    #check both for int or letter

    next = q.peek()
    if next.isupper():
        rutan.atom = next      # värde på rutan
        #rutan.next = rutan.atom
        q.dequeue()
        return

    else:

        if next is not None:

            if next == ")":
                    raise Syntaxfel("Felaktig gruppstart vid radslutet " + printQueue(q))

            raise Syntaxfel("Saknad stor bokstav vid radslutet " + printQueue(q))

        else:



            raise Syntaxfel("Saknad stor bokstav vid radslutet " + next)

"""LOWER CASE LETTER"""
#< letter >::= a | b | c | ... | z


def lower_case_l(q):

    next = q.peek()

    if next.islower():  #
        return

    raise Syntaxfel("Fel, borde vara lowercase " + next) #next eller word?


"""NUMBER"""
#< num >::= 2 | 3 | 4 | ...


def num(q, rutan):

    next = q.peek()


    # pga kommer från group
    if not next.isdigit():
        raise Syntaxfel("Saknad siffra vid radslutet " + printQueue(q))

    if next is not '0':

        sum_int = ''

        while next is not None and next.isdigit():   # while, körs tills påståendet är sant, kolla ifall number, jsdigit() pga string

            sum_int += next

            q.dequeue()
            next = q.peek()


        if int(sum_int) > 1:

            rutan.num = sum_int    # värde på num
            #rutan.atom += rutan.num

            return q

        else:
            raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))



    else:
        q.dequeue()  # pga == 0

        raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))


def weight(mol):

    #preorder

    #lägg samman totala vikten av alla molekyler


    #läs in atomvikt för input atom från atomlista i hashtest.py
    weight = ""

    if mol.next != None:
        weight(mol.next)
        if mol.next != "( )":
            weight += mol.next

        print(rutan.value)
        weight(rutan.down)
        weight(rutan.next)

    return weight

def printQueue(q):
    return_string = ""
    while not q.isEmpty():
        word = q.dequeue()
        return_string += word
    return return_string

def storeSentence(atom_name):
    q = LinkedQ()

    for char in atom_name:
        q.enqueue(char)

    return q




def check_syntax(mening):
    q = storeSentence(mening)

    try:
        mol = read_formel(q)
        return mol #"Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        #return str(fel).strip() #+  " före " + str()
        return mol



def main():
     mening = input("Skriv en atom: ")
     resultat = check_syntax(mening)
     #print(resultat)

     #resultat = Ruta(atom="Cl", num=2)
     mg = Molgrafik()
     mg.show(resultat)
     input()


     #Låt programmet skriva ut vikten av molekylen i terminalfönstret
    print(weight(resultat))


    # for row in sys.stdin:  # standard input
    #
    #     row = row.strip()
    #
    #     if row == "#":
    #         break
    #
    #     resultat = check_syntax(row)
    #     print(resultat)

    # stdin = open("test_input.txt")
    # mol = stdin.readline()
    # while mol[0] != "#":
    #     mol = mol.strip("\n")
    #     result = check_syntax(mol)
    #     mol = stdin.readline()
    #     print(result)

if __name__ == "__main__":
    main()


#print(check_syntax("cr12"))

