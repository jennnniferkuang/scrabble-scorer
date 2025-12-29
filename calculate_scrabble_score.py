LETTER_POINTS = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

PLAYER_SCORES = {}

def register_players():
    while(True):
        name = input("player name (type 'DONE' to exit): ")
        if name == "DONE":
            break
        PLAYER_SCORES[name] = 0
    return

def create_letter_array(word):
    letter_array = []
    i = 0
    while i < len(word):
        letter = word[i]
        if (i + 1) < len(word):
            lookahead = word[i + 1]
            if lookahead.isdigit():
                letter_array.append((letter, int(lookahead)))
                i += 2 # skip lookahead
            else:
                letter_array.append((letter, 1))
                i += 1
        else:
            letter_array.append((letter, 1))
            i += 1
    print(letter_array)
    return letter_array

def calculate_scrabble_score(player, word, multipliers):
    letter_array = create_letter_array(word)
    word_score = calculate_word_score(letter_array)
    scrabble_score = apply_multipliers(word_score, multipliers)
    PLAYER_SCORES[player] += scrabble_score
    print(player + " earned " + str(scrabble_score) + " points")
    return

def calculate_word_score(letter_array):
    word_score = 0
    for letter, letter_multiplier in letter_array:
        word_score += LETTER_POINTS[letter] * letter_multiplier
    return word_score

def apply_multipliers(word_score, multipliers):
    multiplier_score = word_score
    bingo = False
    for multiplier in multipliers:
        if multiplier.isdigit():
            multiplier_score *= int(multiplier)
        elif multiplier == "BINGO":
            bingo = True
    if (bingo):
        multiplier_score += 50
    return multiplier_score

def print_final_scores():
    print("-----FINAL SCORES-----")
    for player in PLAYER_SCORES:
        print(player + ": " + str(PLAYER_SCORES[player]))
    return


# input of the format: jennifer wo2r3d 2 2 3
# adds points to player named jennifer
# o has 2x letter multiplier, r has 3x letter multiplier
# whole word multipliers 2x 2x 3x

def main():
    register_players()

    while(True):
        user_input = input("input (type 'END GAME' to quit): ")

        if user_input == "END GAME":
            print_final_scores()
            break

        user_input = user_input.split()
        player = user_input[0]
        word = user_input[1]
        multipliers = user_input[2:]
        calculate_scrabble_score(player, word, multipliers)
    
    return

main()