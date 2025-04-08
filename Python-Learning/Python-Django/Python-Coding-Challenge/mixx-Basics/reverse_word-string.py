## Concepts Used: String manipulation, List operations

# Reverse words 
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("Hello Django Developer"))


"""
1) def reverse_words(s)
- This defines function named reverse_words, which takes a single argument s, a string

2) s.spliy()
- The split() method splits the input string s into a list of words based on whitespace(space)

Ex: s = "Hello Django Developer"
s.split() # Output ["Hello","Django","Developer"]

3) [::-1]
- [::-1] is Python's slicing syntax for reversing the list.

4) words["Hello","Django","Developer"]
words[::-1] # Output ['Developer', 'Django','Hello']

5) " ".join()
- It takes a list of words and joins them back into a single string , with a space " " between each word



How it works:
1) Input: "Hello Django Developer"
2) .split() --> ['Hello','Django','Developer']
3) [::-1] --> ['Developer','Django','Hello']
4) " ".join(...) --> "Developer Django Hello"

Alternative method:

def reverse_words(s):
    return " ".join(reversed(s.split()))

print(reverse_words("Hello Django Developer"))
# Output: "Developer Django Hello"

"""