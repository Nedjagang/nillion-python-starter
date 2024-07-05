from nada_dsl import *

def nada_main():
    # Create the parties
    party1 = Party(name="Adventurer")
    party2 = Party(name="Cryptographer")
    party3 = Party(name="Trusted Third-Party")

    # Gather the secret clues
    a = SecretInteger(Input(name="Clue A", party=party1))
    b = SecretInteger(Input(name="Clue B", party=party2))

    # Solve the puzzle
    treasure = a + b

    # Reveal the treasure
    return [Output(treasure, "Treasure", party3)]