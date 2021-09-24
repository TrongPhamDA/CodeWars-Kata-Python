'''
Instructions
You can print your name on a billboard ad. Find out how much it will cost you. Each letter has a default price of £30, but that can be different if you are given 2 parameters instead of 1.
You can not use multiplier "*" operator.
If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a letter).
'''

# def billboard(name, price=30):
#     total = 0
#     for char in list(name): total += price
#     return total

def billboard(name, price=30):
    return sum(price for letter in name)

print(billboard("Jeong-Ho Aristotelis") == 600)
print(billboard( "Jeong-Ho Aristotelis") == 600)
print(billboard("Abishai Charalampos") == 570)
print(billboard("Idwal Augustin") == 420)
print(billboard("Hadufuns John", 20) == 260)
print(billboard("Zoroaster Donnchadh") == 570)
print(billboard("Claude Miljenko") == 450)
print(billboard("Werner Vigi", 15) == 165)
print(billboard("Anani Fridumar") == 420)
print(billboard("Paolo Oli") == 270)
print(billboard("Hjalmar Liupold", 40) == 600)
print(billboard("Simon Eadwulf") == 390)