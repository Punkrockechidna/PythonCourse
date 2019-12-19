is_magician = True
is_expert = False

# check to see if magician and expert: "you are a master magician"
# check if magician but not expert: "at least you're getting there"
# if you are not a magician: "You need magic powers"

if is_expert and is_magician:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
else:
    print("You need magic powers")
