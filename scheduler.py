data = []
with open("participants_2022.txt") as f:
    data = f.read()

users = data.split("\n")
posts = set([y for x in users for y in x.split(",")])

results = {}
for post in posts:
    results[post] = []
    for user_posts in users:
        if post in user_posts:
            results[post] += (user_posts.split(","))
for post in results:
    results[post] = list(set(results[post]))
    results[post].remove(post)
results

possible_overlaps = []
for post in results:
    for x in results:
        if x not in results[post] and x != post:
            possible_overlaps.append([post, x])

# find all unique sets in possible_overlaps
unique_possible_overlaps = []
for x in possible_overlaps:
    if x not in unique_possible_overlaps and x[::-1] not in unique_possible_overlaps:
        unique_possible_overlaps.append(x)

for x in unique_possible_overlaps:
    print("Possible overlap between {} and {}".format(x[0], x[1]))
