# Now it's your turn. Try this practice below.
#
# The core idea in this chapter was about dictionaries and data structures in general. Create a simple program that creates a dictionary called d such that the following runs without error and prints what is expected:
#
# # d = create d using core concepts above.
#
# print(d["Sam"])          # outputs 7
# print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
# print(d.get('Sarah'))    # outputs None
# print(d.get('Jeff', -1)) # outputs -1
# print(d['done'])         # outputs True

# rolls = {
#     'rock': {
#         'defeats': ['scissors'],
#         'defeated_by': ['paper']
#     },
#     'paper': {
#         'defeats': ['rock'],
#         'defeated_by': ['scissors']
#     },
#     'scissors': {
#         'defeats': ['paper'],
#         'defeated_by': ['rock']
#     },
# }


d = {
    'Sam': 7,
    'rolls': ['rock', 'paper', 'scissors'],
    'Sarah': None,
    'Jeff': 0,
    'done': True,
}

print(d["Sam"])  # outputs 7
print(d['rolls'])  # outputs ['rock', 'paper', 'scissors']
print(d.get('Sarah'))  # outputs None
print(d.get('Jeff', -1))  # outputs -1
print(d['done'])  # outputs True

# print(d)
