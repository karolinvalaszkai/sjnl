@@ -13,12 +13,20 @@ class Syntaxfel(Exception):
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
# HASHTAG ska ej läsas in -> hur?
# Vart ska de nya syntaxfelen vara? + next ?
# Lägg till de nya ändringarna, typ "H"
# Läsa in enl. stdn input


# hitta startparentes
@ -76,6 +84,20 @@ def read_group(q):



<<<<<<< Updated upstream
=======
            if next.isdigit():
                num(next, q)
                return
            else: raise Syntaxfel("Saknad siffra vid radslutet " + printQueue(q))
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
>>>>>>> Stashed changes


        #raise Syntaxfel('Felaktig gruppstart vid radslutet + ?)
        #saknad högerparantes vid radslutet



"""ATOM"""
@ -83,8 +105,30 @@ def read_group(q):


def atom(first_char, q, next):
    upper_case_l(first_char)  #H
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





<<<<<<< Updated upstream
    if next is not None:
        if next.isdigit():
            return
@ -98,19 +142,44 @@ def atom(first_char, q, next):

    raise Syntaxfel("Okänd atom vid radslutet") #+vadå??)

=======







    if q.peek().islower():
        q.dequeue()
    raise Syntaxfel("Okänd atom vid radslutet " + printQueue(q))
>>>>>>> Stashed changes


"""UPPER CASE LETTER"""
#< LETTER >::= A | B | C | ... | Z


def upper_case_l(first_char):
def upper_case_l(first_char, next):

    #check both for int or letter
    if first_char.isupper(): #P if sant
        return

<<<<<<< Updated upstream
    raise Syntaxfel("Fel, borde vara uppercase: ") #+ first_char) #eller hela atomnamnet?

=======
    else:

        if next is not None:

            raise Syntaxfel("Saknad stor bokstav vid radslutet " + first_char + next)

        else:

            raise Syntaxfel("Saknad stor bokstav vid radslutet " + first_char)
>>>>>>> Stashed changes


"""LOWER CASE LETTER"""
@ -131,29 +200,43 @@ def lower_case_l(next):

def num(next, q):

    sum_int = ''
    if next is not '0':

    # while, körs tills påståendet är sant
    while next is not None and next.isdigit():  # kolla ifall number, jsdigit() pga string

        sum_int += next
        sum_int = ''

        q.dequeue()
        # while, körs tills påståendet är sant
        while next is not None and next.isdigit():  # kolla ifall number, jsdigit() pga string

        next = q.peek()
            sum_int += next

            q.dequeue() #plockar bort även 1an

            next = q.peek()


        if int(sum_int) > 1:
            return q

<<<<<<< Updated upstream
    if int(sum_int) > 1:
        return

    raise Syntaxfel("För litet tal vid radslutet")
=======
    else:
        q.dequeue() #pga 0

    raise Syntaxfel("För litet tal vid radslutet " + printQueue(q))
>>>>>>> Stashed changes


def printQueue(q):
    return_string = ""
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = " ")
        print()
        return_string += word
    return return_string

def storeSentence(atom_name):
    q = LinkedQ()