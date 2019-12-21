#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# picture_render =[[]]
# print(picture[0])
# print(picture[0][3])
# for number in range(len(picture)):
#     for item in range(len(picture[number])):
#         if picture[number][item] == 0:
#             symbol = ' '
#             picture_render[number][item].extend(symbol)
#         else:
#             symbol = '*'
#             picture_render[number][item].extend(symbol)
# print(picture_render[0])

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end = '')
        else:
            print(empty, end = '')
    print('')

# I thought way too complex