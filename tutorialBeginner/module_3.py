
opleidingen = ["Geschiedenis", "Wiskunde", "Natuurkunde"]

# for opleiding in opleidingen:
#     print(opleiding)

# opleidingen.insert(0, "Aardrijkskunde")
# opleidingen.sort()
# print(opleidingen)

opleidingen_2 = ['Maatschappijkunde', 'Nederlands', 'Engels']

opleidingen.extend(opleidingen_2)
for opleiding in opleidingen:
    print(opleiding)
    