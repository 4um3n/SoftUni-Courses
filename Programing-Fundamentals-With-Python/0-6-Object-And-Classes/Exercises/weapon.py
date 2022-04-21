class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets
    

    def shoot(self):
        if self.bullets <= 0:
            return f"no bullets left"
        self.bullets -= 1
        return f"shooting..."
    

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)