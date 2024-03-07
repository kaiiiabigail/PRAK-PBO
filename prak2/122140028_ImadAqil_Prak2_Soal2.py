import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.defense_power = 5
        print(f"Selamat datang, {self.name}!")

    def __del__(self):
        print(f"Selamat tinggal, {self.name}!")

    def display_info(self):
        print(f"{self.name} - Kesehatan: {self.health}")

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} menyerang {opponent.name} dan menyebabkan {damage} poin kerusakan.")

    def defend(self):
        defense_bonus = random.randint(self.defense_power - 2, self.defense_power + 2)
        self.health += defense_bonus
        print(f"{self.name} melakukan pertahanan dan mendapatkan {defense_bonus} poin kesehatan.")

def main():
    while True:
        print("Selamat datang di Game!")
        player_name = input("Masukkan nama Anda: ")

        player = Player(player_name)
        opponent = Player("Lawan")

        while player.health > 0 and opponent.health > 0:
            print("\n===== Giliran Andax =====")
            player.display_info()
            opponent.display_info()

            choice = input("Apa yang ingin Anda lakukan? (1: Serang, 2: Bertahan): ")
            if choice == '1':
                player.attack(opponent)
            elif choice == '2':
                player.defend()
            else:
                print("Pilihan tidak valid. Pilih 1 untuk menyerang atau 2 untuk bertahan.")

            if opponent.health <= 0:
                print(f"Selamat! Anda berhasil mengalahkan {opponent.name}.")
                break

            print("\n===== Giliran Lawan =====")
            opponent_choice = random.choice(['attack', 'defend'])
            if opponent_choice == 'attack':
                opponent.attack(player)
            else:
                opponent.defend()

            if player.health <= 0:
                print(f"{opponent.name} berhasil mengalahkan Anda. Game Over.")
                break

        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ")
        if play_again.lower() != 'y':
            print("Terima kasih sudah bermain!")
            break

if __name__ == "__main__":
    main()
