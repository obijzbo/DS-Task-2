Problem Statement

We have 5 ingredient:
oranges
apples
pears
grapes
watermelon
lemon
lime


Questions we ask client:
1.Do you go out to party on weekends? (yes or no)
2.What flavours do you like? (cider, sweet, waterlike)
3.What texture you don't like? (smooth, slimy, rough)
4.What price range will you buy drink for? ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)

If they party on weekends, apples, pears, grapes, watermelon are allowed.
If they like cider, show apples, oranges, lemon, lime.
If they like sweet, show watermelon, orange.
If they like waterlike, show watermelon.
If grapes is chosen, remove watermelon from the list.
If texture you don't like is smooth, remove pears.
If texture you don't like is slimy, remove watermelon, lime and grape.
If texture you don't like is waterlike, remove watermelon.
If price < $3 remove lime, watermelon.
If price > $4 and < $7 remove pears, apples.


Tasks:

Make a function passing in the answer to the 4 questions and structure GPT3 prompt given these rules to give you the list of recommeded fruits.
Make a simple flask POST API where we return the answers given the input in POST Body with content type application/json