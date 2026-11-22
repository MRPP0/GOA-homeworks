food = ["pizza", "burger", "pizza", "fries"]

#დაამატე "salad" ბოლოში.
#ჩასვი "cola" ინდექსზე 1.
#წაშალე "fries".
#დაითვალე "pizza"-ს რაოდენობა.
#იპოვე "burger"-ის ინდექსი.

food.append ("salad")

food.insert(1 , "cola")

food.remove("fries")



print(food)

print(food.count("pizza"))


fruits = ["apple", "banana", "orange", "apple", "kiwi"]

#გამოიყენეთ მხოლოდ ეს მეთოდები: .append(), .insert(), .pop(), .remove(), .count(), .index()

#["apple", "grape", "banana", "apple", "kiwi", "melon"]
fruits.append("melon")

fruits.insert(1 , "grape")

fruits.pop(3)

print(fruits)

print(fruits.count("apple"))


print(fruits.index("banana"))


fast_food = ["pizza", "burger", "pizza", "pasta", "burger"]

#დაამატო "salad" ბოლოში
#"pasta" ჩასვა სიის დასაწყისში
#წაშალო ერთი "burger"
#გაიგო რამდენჯერ არის "pizza"
#იპოვო "salad"-ის ინდექსი

fast_food.append('salad')

fast_food.insert(0 , "pasta")

fast_food.remove('burger')

print(fast_food.count('pizza'))

print(fast_food.index("salad"))

print(fast_food)

games = ["Minecraft", "FIFA", "GTA", "Minecraft", "Fortnite"]

#დაამატე "Roblox" ბოლოში
#ჩასვი "Valorant" ინდექსზე 2
#ამოაგდე "GTA" მისი ინდექსით
#წაშალე "Fortnite"
#დაითვალე "Minecraft"-ის რაოდენობა
#იპოვე "Roblox"-ის ინდექსი

games.append('Roblox')

games.insert(2 , 'Valorant')

games.pop(2)

games.remove('Fortnite')

print(games.index('Roblox'))

# .append() listis bolos amatebs i9ndexs .insert() amatebs indexs .pop() amogdebs indexs listidan  .remove() washlis listidan indexs .count() itvlis ramdenjer meordeba .index() itvlis romel indeszea  len ari iseti functio romelic orvie lists da strings aaqvs da is itvlis im stringis and listiss sigrjes