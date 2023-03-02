from gpt_prompt import get_recommended_fruits

def user_input():
    party = input("Party on weekends? Yes or No ")
    flavour = input("Which flavour do you prefer? cider, sweet or waterlike ")
    texture = input("What texture you don't like? smooth, slimy, rough ")
    price = input("What price range will you buy drink for? $1, $2, $3, $4, $5, $6, $7, $8, $9, $10 ")

    recommended_fruits = get_recommended_fruits(party_on_weekends=party, flavor=flavour, disliked_texture=texture, price_range=price)
    print(recommended_fruits)

if __name__ == "__main__":
    user_input()