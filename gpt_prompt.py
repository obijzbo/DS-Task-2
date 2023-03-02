import openai
openai.api_key = "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"

def get_recommended_fruits(party_on_weekends, flavor, disliked_texture, price_range):
    prompt = f"Please recommend some fruits based on the following preferences:\n1. Do you go out to party on weekends? {party_on_weekends}\n2. What flavors do you like? {flavor}\n3. What texture do you not like? {disliked_texture}\n4. What price range will you buy a drink for? {price_range}\nRecommended fruits:"

    if party_on_weekends:
        allowed_fruits = ["apples", "pears", "grapes", "watermelon"]
    else:
        allowed_fruits = ["oranges", "apples", "pears", "grapes", "watermelon", "lemon", "lime"]
    if flavor == "cider":
        recommended_fruits = ["apples", "oranges", "lemon", "lime"]
    elif flavor == "sweet":
        recommended_fruits = ["watermelon", "oranges"]
    elif flavor == "waterlike":
        recommended_fruits = ["watermelon"]
    else:
        recommended_fruits = allowed_fruits

    if "grapes" in recommended_fruits and "watermelon" in recommended_fruits:
        recommended_fruits.remove("watermelon")

    if disliked_texture == "smooth":
        recommended_fruits.remove("pears")
    elif disliked_texture == "slimy":
        for fruit in ["watermelon", "lime", "grapes"]:
            if fruit in recommended_fruits:
                recommended_fruits.remove(fruit)
    elif disliked_texture == "waterlike":
        recommended_fruits.remove("watermelon")

    if price_range == "$1" or price_range == "$2":
        if "lime" in recommended_fruits:
            recommended_fruits.remove("lime")
        if "watermelon" in recommended_fruits:
            recommended_fruits.remove("watermelon")
    elif price_range == "$5" or price_range == "$6":
        if "pears" in recommended_fruits:
            recommended_fruits.remove("pears")
        if "apples" in recommended_fruits:
            recommended_fruits.remove("apples")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    return [fruit for fruit in recommended_fruits if fruit in response.choices[0].text.lower()]