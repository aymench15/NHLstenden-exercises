
def id_to_fruit(fruit_id, fruits):
    # Check if the fruit_id is within the valid range
    if 0 <= fruit_id < len(fruits):
        return fruits[fruit_id]
    else:
        return "Invalid fruit_id"

# The fruits are passed to the function as a set, which causes an error
# because the set does not have access to the elements through the index.
# As a result, the fruits must be sent to the function as a list or tuple.

# Example usage
name1 = id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"])
name3 = id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"])
name4 = id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"])

# Print the results
print(name1)  # Expected: 'orange'
print(name3)  # Expected: 'kiwi'
print(name4)  # Expected: 'strawberry'
