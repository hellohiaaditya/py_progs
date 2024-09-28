import art
print(art.logo)

end = False

data = {}

while not end:

    name = input("What is your name?: ")

    bid = int(input("What is your bid?: $"))

    data.update({name : bid})

    ask = input("Are there any other bidders? Type 'yes or no'\n").lower()

    if ask == "yes":
        print("\n" * 100)

    elif ask == "no":
        end = True

winner = ""

val = 0

for i in data:
    bid_amount = data[i]
    if bid_amount > val:
        val = bid_amount
        winner = i

print(f"The winner is {winner} with a bid of ${val}")