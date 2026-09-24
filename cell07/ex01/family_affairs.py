def redheads(family):
    def is_red(name):
        return family[name] == "red"
    x = filter(is_red, family)
    return list(x)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(redheads(dupont_family))
