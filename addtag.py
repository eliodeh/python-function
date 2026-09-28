# # part A 
# predicted output:

['python', 'testing']
False
True

# Explaination:
# 1. profile.copy creates new dictionary object with same keys
# 2. For "tags key, value is a list"

# so:
# 1. updated is new dictionary object that why changed is original is False
# 2. updated["tags"] and profile["tags"] point to sssame list object that why changed["tags"] is original["tags"] is True
# 3. .append connect both names and make it visible that why orriginal["tags"] prints ['python', 'testing']



# part B 
def add_tag(profile, tag):
    updated = profile.copy
    updated["tags"] = profile["tags"].copy()
    updated["tags"].append(tag)
    return updated


# part C
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

# Original tags remain unchanged
assert original["tags"] == ["python"]

# Returned tags contain the new tag
assert changed["tags"] == ["python", "testing"]

# Append to the returned list, then confirm original is still unaffected
changed["tags"].append("extra")
assert original["tags"] == ["python"]

