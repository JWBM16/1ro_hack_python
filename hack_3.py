"""
text: "fooziman" output => "Fooziman"
"""


def fn_hack_3():
    result = "fooziman"
    # ...
    return result.capitalize()


r = fn_hack_3()

print(r)
