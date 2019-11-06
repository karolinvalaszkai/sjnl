"5 funktioner för syntaxregler"
# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass


atomlist = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
            "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
            "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
            "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",
            "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa",
            "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",
            "Ds", "Rg", "Cn", "Fl", "Lv"]


#[21] ej [2,1]

#FRÅGA!
# Vart ska de nya syntaxfelen vara? + next ?
# Läsa in enl. stdn input


# hitta startparentes
# dequa startparantesen
# leta efter slutparantesen



"""FORMEL"""
# <formel>::= <mol> \n
def read_formel(q):
    read_mol(q)
    '\n'
    #+ev radbryt?


"""MOLECULE"""
#  <mol>   ::= <group> | <group><mol>
def read_mol(q):
    read_group(q)
    next = q.peek()

    if next is not None:
        read_mol(next)


"""GROUP"""
#ex P21
# <group> ::= <atom> |<atom><num> | (<mol>) <num>

def read_group(q):
    first_char = q.dequeue()    # tar bara ut P
    next = q.peek()             # kollar på 21an

    if first_char != "(":
        atom(first_char, q, next)   # atom pga båda cases innehålller atom

        if next is not None and next.isdigit():      #kolla ifall number, jsdigit() pga string
            num(next, q)
        return

    elif first_char == "(":
        read_mol(q)
        if q.peek() == ")":
            num(next, q)
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet")


        if next.isdigit():
            num(next, q)
            return
        else: raise Syntaxfel("Saknad siffra vid radslutet " + printQueue(q))
    else:
        raise Syntaxfel("Saknad högerparentes vid radslutet ")


        #raise Syntaxfel('Felaktig gruppstart vid radslutet + ?)
        #saknad högerparantes vid radslutet



"""ATOM"""
#< atom >::= < LETTER > | < LETTER > < letter >

def atom(first_char, q, next):
    atom_name = first_char
    if next != None and next.islower():
        atom_name += next        # vad händer om next == None

    if atom_name in atomlist:

        upper_case_l(first_char, next)  #H

        if next == None:
            return

        if next.isdigit() or next.isupper() or next == "(" or next == ")": # Om next == digit eller Stor bokstav
            return # ska vi kolla  num, "(" eller ")" i denna funktion

        elif next is not None:
            lower_case_l(next)
            q.dequeue()
            return


    if next is not None:
        if next.isdigit():
            return

        else:
            #if next is not None:   #pga vissa är bara en bokstav?
            lower_case_l(next)
            q.dequeue()
    else:
        return


    if q.peek().islower():
        q.dequeue()
    raise Syntaxfel("Okänd atom vid radslutet " + printQueue(q))


"""UPPER CASE LETTER"""
#< LETTER >::= A | B | C | ... | Z


def upper_case_l(first_char, next):

    #check both for int or letter
    if first_char.isupper(): #P if sant
        return



    else:

        if next is not None:

            raise Syntaxfel("Saknad stor bokstav vid radslutet " + first_char + next)

        else:

            raise Syntaxfel("Saknad stor bokstav vid radslutet " + first_char)


"""LOWER CASE LETTER"""
#< letter >::= a | b | c | ... | z


def lower_case_l(next):

    if next is not None and next.islower():  #
        return

    raise Syntaxfel("Fel, borde vara lowercase: " + next) #next eller word?



"""NUMBER"""
#< num >::= 2 | 3 | 4 | ...

def num(next, q):

    if next is not '0':


        sum_int = ''

        # while, körs tills påståendet är sant
        while next is not None and next.isdigit():  # kolla ifall number, jsdigit() pga string

            sum_int += next

            q.dequeue() #plockar bort även 1an

            next = q.peek()


        if int(sum_int) > 1:
            return q


    else:
        q.dequeue() #pga 0

    raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))


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
        read_formel(q)
        return "Formeln är syntastiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) #+  " före " + str()






def main():
    mening = input("Skriv en atom: ")
    resultat = check_syntax(mening)
    print(resultat)

if __name__ == "__main__":
    main()


#print(check_syntax("cr12"))

