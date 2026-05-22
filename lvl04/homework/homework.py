
#1)მომხმარებელს სთხოვეთ input-ის გამოყენებით შეიყვანოს თავისი სახელი და print-ის (output) გამოყენებით მიესალმეთ მას.
#
#2)კომენტარების სახით ახსენით რა არის კონკატენაცია (concatenation) და მოიყვანეთ შესაბამისი მაგალითი.
#
#3)შექმენით ორი ცვლადი, სადაც input ინსტრუქციით შეინახავთ მომხმარებლის სახელსა და გვარს. დაბეჭდეთ ისინი ერთ წინადადებაში კონკატენაციის (+) გამოყენებით.
#
#4)შექმენით ცვლადი, სთხოვეთ მომხმარებელს input-ით საყვარელი ფერის შეყვანა. შემდეგ კონკატენაციის გამოყენებით დაბეჭდეთ ტექსტი: "შენი საყვარელი ფერია " და მიუერთეთ შემოტანილი მნიშვნელობა.
#
#5)input-ის საშუალებით მომხმარებელს შემოატანინეთ 3 განსხვავებული სიტყვა სხვადასხვა ცვლადში. კონკატენაციის დახმარებით შეაერთეთ ეს სიტყვები ისე, რომ მიიღოთ ერთი სრული წინადადება (space)-ის გათვალისწინებით და დაბეჭდეთ.


name = input("your name : ")

print(name)

#koneqtacia aris stringebis sheerteba an cvladebis maqlitad

string1 = "barack"

string2 = "obama"

print(string1 + " " + string2)

lastname = input("your lastname : ")

print(lastname + " " + name)

color = input("your fav color : ")

print("my favorite color is" + " " + color)

word1 = input("a word : ")

word2 = input("second word : ")

word3 = input("third word : ")

print(word1 + " " + word2 + " " + word3)