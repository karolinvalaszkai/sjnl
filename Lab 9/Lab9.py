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


#[21] ej [2,1]

#FRÅGA!
# HASHTAG ska ej läsas in -> hur?
# Vart ska de nya syntaxfelen vara? + next ?
# Lägg till de nya ändringarna, typ "H"


# hitta startparentes
# dequa startparantesen
# leta efter slutparantesen




# <formel>::= <mol> \n





# <mol>   ::= <group> | <group><mol>

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









"""ATOM"""
#< atom >::= < LETTER > | < LETTER > < letter >


def atom(first_char, q, next):
    upper_case_l(first_char)  #H

    if next is not None:
        if next.isdigit():
            return

        else:
            #if next is not None:   #pga vissa är bara en bokstav?
            lower_case_l(next)
            q.dequeue()
    else:
        return

    raise Syntaxfel("Okänd atom vid radslutet") #+vadå??)



"""UPPER CASE LETTER"""
#< LETTER >::= A | B | C | ... | Z


def upper_case_l(first_char):
    #check both for int or letter
    if first_char.isupper(): #P if sant
        return

    raise Syntaxfel("Fel, borde vara uppercase: ") #+ first_char) #eller hela atomnamnet?



"""LOWER CASE LETTER"""
#< letter >::= a | b | c | ... | z


def lower_case_l(next):

    if next is not None and next.islower():  #
        return

    raise Syntaxfel("Fel, borde vara lowercase: " + next) #next eller word?



"""NUMBER"""
#< num >::= 2 | 3 | 4 | ...

def num(next, q):

    sum_int = ''

    # while, körs tills påståendet är sant
    while next is not None and next.isdigit():  # kolla ifall number, jsdigit() pga string

        sum_int += next

        q.dequeue()

        next = q.peek()


    if int(sum_int) > 1:
        return

    raise Syntaxfel("För litet tal vid radslutet")


def printQueue(q):
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = " ")
        print()

def storeSentence(atom_name):
    q = LinkedQ()

    for char in atom_name:
        q.enqueue(char)

    return q


def check_syntax(mening):
    q = storeSentence(mening)

    try:
        readformel(q)
        return "Formeln är syntastiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) #+  " före " + str()

def read_formel(q):
    read_mol(q)
    '\n'
    #+ev radbryt?

def main():
    mening = input("Skriv en atom: ")
    resultat = check_syntax(mening)
    print(resultat)

if __name__ == "__main__":
    main()


#print(check_syntax("cr12"))

