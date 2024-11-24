from main import UserData, Automobile

user1 = UserData('Baxtiyor', 'Tuychiyev', 24)
user1.lastname = 'Tuych'
user1.firstname = 'Baxa'
print(user1)
print(user1.get_count)


auto1 = Automobile('BMW', 'X6', 'black', 35000, 1000)
auto2 = Automobile('GM', 'Malibu', 'white', 26000)

print(auto1.get_id())
auto1.add_km(1000)
print(auto1.get_km())
print(auto2.get_num_auto())
auto1.add_km(-500)
