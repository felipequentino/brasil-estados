import turtle
import pandas as pd


def load_map_shape(screen, image): # Necessary methods of turtle library
    screen.addshape(image)
    turtle.shape(image)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    return t


def read_state_data():  # path to your doc
    return pd.read_csv("estados_coords.csv")


def get_missing_states(all_states, states_guessed):  # comparing the states that you guessed with all of them
    missing_states = [state for state in all_states if state not in states_guessed]
    return missing_states


def save_missing_states(missing_states):
    new_data = pd.DataFrame(missing_states, columns=['Estado'])
    new_data.to_csv("Estados_que_voce-esqueceu.csv", index=False)


def main():
    screen = turtle.Screen()
    image = "mapa.gif"
    t = load_map_shape(screen, image)

    df = read_state_data()
    all_states = df['Estado'].tolist()
    count_data = len(df)  # df.X.count() will work as well

    contador = 0
    states_guessed = []

    while count_data > 0:
        answer_state = screen.textinput(title=f"Advinhe o Estado ({contador}/26)",
                                        prompt="Diga o nome de um estado brasileiro vazio.\nDigite 'SAIR' para sair.").upper()
        if answer_state == "SAIR":  # word to get out (the 'EXIT')
            missing_states = get_missing_states(all_states, states_guessed)
            save_missing_states(missing_states)
            break

        if answer_state in all_states:
            states_guessed.append(answer_state)
            query = df[df['Estado'] == answer_state]
            t.goto(int(query['X']), int(query['Y']))
            t.write(answer_state)
            contador += 1
            count_data -= 1  # The game will over when this count hit 26 (number of brazil states)

    screen.exitonclick()


if __name__ == "__main__":
    main()
