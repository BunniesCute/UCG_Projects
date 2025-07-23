#Description: Mad Libs (Generates a random story using user inputs)

print ("=" *50)

print("\n📚Welcome to Mad Libs! 📖")

#Inputs
adj_1 = input("\nEnter an adjective: ")
clothes = input("\nArticle of clothing: ")
place = input("\nEnter a place(building): ")
drink = input ("\nEnter a drink: ")
celebrity = input ("\nEnter a celebrity: ")
loud_phrase =input("\nEnter a random phrase:(Something someone would say when they're startled): ")
liquid = input ("\nEnter a liquid: ")
verb_1 = input("\nEnter a -ed verb: ")
animal = input ("\nEnter an animal: ")
person =input ("\nEnter a random name: ")
object = input("\nEnter a object: ")
dialogue = input("\nEnter a dramatic line of dialogue: ")
item = input("\nEnter a pet or a random item: ")
adj_2 = input("\nEnter an adjective: ")
plur_noun = input("\nEnter a plural noun: ")
food = input ("\nEnter a random food: ")
verb2 = input("\nEnter a verb: ")
ly_adv = input ("\nEnter an -ly adverb: ")
sub = input("\nEnter a random substance: ")
exclamation = input("\nEnter a random phrase someone would say when they're mad(Ex:WHAT THE HECK!):")
verb_3 = input ("\nEnter a present tense verb: ")
num = input("\nPick a number 1-10: ")

#Processing bill total (tip is 15%)
bill = float(input("\nHow much was the bill?: $"))
tip=  0.15 * bill
total = tip + bill

#Outputs
print(f"\nThis morning I woke up feeling {adj_1}, so I threw on my favorite {clothes} and headed to {place} for a much-needed {drink}.")
print(f"As I walked in, the barista who looked very suspicious, turned out to be {celebrity}! Who then shouted {loud_phrase}! and spilled {liquid} all over the floor.")
print(f"\nI {verb_1} on it, flew across the room like a(n) {animal}, and crash landed into {person} holding a {object}. He/she glared at me and whispered, {dialogue}! before storming out with his/her(s) {item}. ")
print(f"Trying to recover, I ordered a {adj_2} latte with extra {plur_noun} and a side of {food}.{ly_adv}, I was given {sub} instead of my coffee,{exclamation}!. The bill was ${total}")
print(f"\n{num}/10. Would {verb_3} again.")

print("="*50)