# slicing = create a substring by extracting elements from a seperate string
# indexing[] or slice()
# [start:stop:step]

name = "Samero Ibra"

first_name = name[0:6]  # start is inclusive in counting, stop is exclusive in counting
last_name = name[7:]  # you can leave the last index blank and it will go to the end
# you can also leave the first idex blank and it will start at the front
step_name = name[::2]
reversed_name = name[::-1]


print(first_name)
print(last_name)
print(step_name)
print(reversed_name)


website1 = "https://www.google.com/"
website2 = "https://www.youtube.com/"

slice = slice(
    12,
    -5,
)

print(website1[slice])
print(website2[slice])
