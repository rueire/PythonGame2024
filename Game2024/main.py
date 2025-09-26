import lore
import game

def main():
    lore.guide()
    lore.start()
    while True:
        prompt = game.read_prompt()
        length = len(prompt)

    #    if game.validation(prompt):
    #        break

        if length == 0:
            continue
        elif length < 2:
            if game.act(prompt):
                print("Thank you for playing\n")
                break
        elif length == 2:
            game.validate(prompt[0], prompt[1])

        elif length > 2:
            print("Error! Invalid prompt.")


if __name__=='__main__':
    main()