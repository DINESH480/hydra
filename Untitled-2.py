def generate_username(name, birth_year):
    parts = name.lower().split()
    return parts[0][:3] + parts[-1][-2:] + str(birth_year)[-2:]

name = input("Enter your full name: ")
year = int(input("Enter your birth year: "))
print("Your username:", generate_username(name, year))
