def sentence():
    sent = str(input("Give me a full sentence\n\n"))
    print("\n\nNow I give you reverse order\n\n"+" ".join(sent.split()[::-1]))

sentence()
