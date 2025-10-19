import lore
import actions

def main():
    lore.guide()
    lore.start()
    while True:
        prompt = actions.read_prompt()
        length = len(prompt)

        if length == 0:
            continue
        elif length < 2:
            if actions.act(prompt):
                print("Thank you for playing\n")
                break
        elif length == 2:
            actions.validate(prompt[0], prompt[1])

        elif length > 2:
            print("Error! Invalid prompt.")


if __name__=='__main__':
    main()