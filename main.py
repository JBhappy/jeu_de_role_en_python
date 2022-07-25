from random import randint as random

class Player:

    def __init__(self, name, isBot):
        self.bot = isBot
        self.name = name
        self.vie = 50
        self.potions = isBot and 0 or 3
        self.potionUsed = False

    def takePotion(self) -> bool:
        if self.potions < 1: return False
        health = random(15, 50)
        self.potions -= 1
        self.potionUsed = True
        self.vie += health
        print(f"{self.name} s'est soigné de {health} grace a une potion")
        return True

    def attaque(self, cible):
        damage = random(5, self.bot and 15 or 10)
        cible.vie -= damage
        print(f"{self.name} à fais {damage} de dégat à {cible.name}")

class Game:

    def __init__(self):
        self.joueur = Player("Joueur", False)
        self.ennemi = Player("Ennemi", True)
        self.status = True

    def start(self):
        joueur = self.joueur
        ennemi = self.ennemi
        while self.status:
            if not joueur.potionUsed: self.play(joueur)
            else: joueur.potionUsed = False
            if self.status: self.play(ennemi)

    def play(self, player):
        player_bot = player.bot
        if player_bot == True: player.attaque(self.joueur)
        while player_bot == False:
            choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
            if choix == "1":
                player.attaque(self.ennemi)
            elif choix == "2":
                if not player.takePotion():
                    print("Impossible d'utilisé de potions il ne vous en reste plus")
                    continue
            else:
                print("Choix incorrect, veuieillez choisir uniqument entre 1 ou 2")
                continue
            break
        self.recap()

    def end(self):
        self.status = False

    def recap(self):
        joueur = self.joueur
        ennemi = self.ennemi
        if joueur.vie <= 0:
            print("Dommage, Vous avez perdut!!!")
            print(f"Le joueur ennemie avais encore {ennemi.vie} points de vie")
            self.end()
        elif ennemi.vie <= 0:
            print("BRAVO!!! Vous avez gagné!!!")
            print(f"Il vous restait encore {joueur.vie} points de vie")
            self.end()
        else:
            print(f"{joueur.name}: {joueur.vie} HP")
            print(f"{ennemi.name}: {ennemi.vie} HP")


if __name__ == '__main__':
    Game().start()
    print("PARTIE TERMINÉE")