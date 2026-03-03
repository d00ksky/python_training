string = "jan kowalski"

# n


def parse_name(full_name: str) -> dict:
    result = {}
    full_name = full_name.strip()
    full_name = full_name.split()
    if len(full_name) == 2:
        result["first_name"] = full_name[0].capitalize()
        result["last_name"] = full_name[1].capitalize()
        result["initials"] = result["first_name"][0] + "." + result["last_name"][0] + "."
        return result
    raise ValueError("Expected 'first_name last_name'")


res = parse_name(string)

print(res)
# for word in string_list:
#     capital = word.capitalize()
#     print(capital)

