import re

data = "day21.txt"
pat = re.compile(r"^([a-z\s]+) \(contains ([a-z,\s]+)\)$")
ingredients = []
allergen_reference = dict()

for i, line in enumerate(open(data)):
    ing, allerg = pat.match(line).groups()
    ingredients.append(ing.split())
    for al in allerg.split(", "):
        this_list = allergen_reference.get(al, list())
        this_list.append(i)
        allergen_reference[al] = this_list

allergen_candidates = {
    key: set.intersection(*[set(ingredients[k]) for k in allergen_reference[key]])
    for key, value in allergen_reference.items()
}

no_ingredient = set(i for l in ingredients for i in l).difference(set.union(*(allergen_candidates.values())))


print(len([i for l in ingredients for i in l if i in no_ingredient]))