#Calculadora de idade

year_birth = input("Enter your year of birth: ")
year_birth_int = int(year_birth)

actual_year = 2024

if len(year_birth) <= 4:
    age_calculator = actual_year - year_birth_int
    if '-' in str(age_calculator):
        print(f"This date doesn't exist")
    else: 
        print(f"You are or will be {age_calculator} years old")

else:
    print("Please, enter your year of birth correctly")
