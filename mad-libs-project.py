#1.The task requires the user to pick one of several templates, but your code only has one fixed story.
#2.All story words (transport, name, noun, etc.) are hardcoded.The task specifically says: “ask the user to input words” using input().
#3.The task asks to use random. Your code doesn’t use it at all.
#4.The instructions say:“don’t bother with additional functions for now.” You’re using two functions (space_story and main), which is fine but not necessary for the minimal solution.

def space_story():
    transport = "Executor"
    name = "Darth Vader"
    noun = "rubber duck"
    planet = "Mustafar"
    adjective = "glowing"
    verb1 = "dance"
    verb2 = "run"

    story = f"""
Yesterday I flew to space on a {transport}.
With me was {name}, who brought a {noun}.
On planet {planet}, we met a {adjective} alien.
It asked us to {verb1}, but we decided to {verb2} and return home.
"""

    print("Space Adventure Story:")
    print(story)


def main():
    space_story()


if __name__sss == "__main__":
    main()

