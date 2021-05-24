from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A is not knight and knave at the same time
    Or(And(AKnight, AKnave), Not(And(AKnight, AKnave))), # A's sentence is true or false
    Not(And(And(AKnight, AKnave), Not(And(AKnight, AKnave)))), # A's sentence is not both true and false at the same time
    Implication(AKnight, And(AKnight, AKnave)), # if A is a knight, his sentence is true
    Implication(AKnave, Not(And(AKnight, AKnave))) # if A is a knave, his sentence is false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A is not knight and knave at the same time
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B is not knight and knave at the same time
    Or(And(AKnave, BKnave), Not(And(AKnave, BKnave))), # A's sentence is either true or false
    Implication(AKnight, (And(AKnave, BKnave))), # if A is a knight, his sentence is true
    Implication(AKnave, Not(And(AKnave, BKnave))) # if A is a knave, his sentence is false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A is not knight and knave at the same time
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B is not knight and knave at the same time
    
    Or((Or(And(AKnight, BKnight), And(AKnave, BKnave))), Not((Or(And(AKnight, BKnight), And(AKnave, BKnave))))), # A's sentence is true or false
    Or((Or(And(AKnight, BKnave), And(AKnave, BKnight))), Not((Or(And(AKnight, BKnave), And(AKnave, BKnight))))), # B's sentence is true or false
    
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    Implication(BKnight, (Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))           
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
# basic scenario
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A is not knight and knave at the same time
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B is not knight and knave at the same time
    Or(CKnight, CKnave),  # C is either a knight or a knave
    Not(And(CKnight, CKnave)), # C is not knight and knave at the same time
    
# first statement
    # this statement is not required for the puzzle to be solved
    # and is not giving us any information
    # as the statement "I am a knave" is impossible given the game rules
    # so the statement was "I am a knight" hence A can be both knight and knave 
# second statement
Implication(BKnight, Implication(AKnave, AKnight)),
Implication(BKnight, Implication(AKnight, AKnave)),
Implication(BKnave, Implication(AKnight, AKnight)),
Implication(BKnave, Implication(AKnave, AKnight)),


# third statement
    Or(CKnave, Not(CKnave)),
    Not(And(CKnave, Not(CKnave))),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
# fourth statement
    Or(AKnight, Not(AKnight)),
    Not(And(AKnight, Not(AKnight))),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
    
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
