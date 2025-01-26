import random

# Pelaaja, joka pyrkii voittamaan 60 % ajasta
def player(prev_play, opponent_history=[]):
    # Tallennetaan vastustajan historia
    if prev_play:
        opponent_history.append(prev_play)

    # Jos historiaa on riittävästi, analysoi vastustajan viimeinen siirto
    if len(opponent_history) > 0:
        # Ennusta, että vastustaja käyttää samaa siirtoa uudelleen
        prediction = opponent_history[-1]

        # Valitse siirto, joka voittaa vastustajan ennustetun siirron
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[prediction]
    else:
        # Aloita satunnaisella siirrolla
        return random.choice(['R', 'P', 'S'])

# Testauskoodi
if __name__ == "__main__":
    from random import choice

    # Testivastustajat
    def random_opponent(prev_play):
        return random.choice(['R', 'P', 'S'])

    def predictable_opponent(prev_play):
        return 'R'

    # Testi
    opponents = [random_opponent, predictable_opponent]
    results = {"wins": 0, "losses": 0, "ties": 0}

    for opponent in opponents:
        opponent_history = []
        for i in range(1000):  # Pelien määrä
            prev_play = "" if i == 0 else opponent_history[-1]
            opponent_move = opponent(prev_play)
            player_move = player(opponent_move, opponent_history)

            # Päivitä tulokset
            if player_move == opponent_move:
                results["ties"] += 1
            elif (player_move == "R" and opponent_move == "S") or \
                 (player_move == "P" and opponent_move == "R") or \
                 (player_move == "S" and opponent_move == "P"):
                results["wins"] += 1
            else:
                results["losses"] += 1

    print("Final results:", results)
    win_rate = results["wins"] / (results["wins"] + results["losses"] + results["ties"]) * 100
    print(f"Win rate: {win_rate:.2f}%")
