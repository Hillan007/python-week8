class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # Default energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Happiness level (0 = sad, 10 = very happy)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate and feels better! 🍽️")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good rest! 😴")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and is happier! 🎾")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} learned a new trick: {trick}! 🏆")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 😔")

    def get_status(self):
        print(f"\n🐶 {self.name}'s Current Status:")
        print(f"🍽️ Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😃 Happiness: {self.happiness}/10\n")

    def interact(self):
        while True:
            action = input("Choose an action (eat, sleep, play, train, status, exit): ").strip().lower()
            if action == "eat":
                self.eat()
            elif action == "sleep":
                self.sleep()
            elif action == "play":
                self.play()
            elif action == "train":
                trick = input("Enter a trick to teach: ")
                self.train(trick)
            elif action == "status":
                self.get_status()
            elif action == "exit":
                print(f"Goodbye! {self.name} will miss you. 👋")
                break
            else:
                print("Invalid action. Try again.")

# Example usage
pet_name = input("Name your pet: ")
my_pet = Pet(pet_name)
my_pet.interact()
