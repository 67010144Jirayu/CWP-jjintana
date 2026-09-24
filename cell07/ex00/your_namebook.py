def array_of_names(persons):
    y = []
    for first_name in persons:
        last_name = persons[first_name]
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        y.append(full_name)
    return y

print(array_of_names(persons))
persons = {"jean": "valjean",
           "grace": "hopper",
           "xavier": "niel",
           "fifi": "brindacier"}

print(array_of_names(persons))
