import faker
import time
import statistics

fake = faker.Faker()
scores = []

def get_sentence(choice):
    match choice:
        case "1":
            return fake.sentence(nb_words=6)
        case "2":
            return fake.sentence(nb_words=12)
        case "3":
            return fake.sentence(nb_words=24)
        case _:
            return None

def play_game():
    print("\n[1] Easy")
    print("[2] Medium")
    print("[3] Hard")

    choice = input("Difficulty: ")
    sentence = get_sentence(choice)

    if sentence == None:
        print("Invalid difficulty!")
        return

    print("\nType this sentence:")
    print(sentence)

    input("\nPress ENTER to start...")

    start = time.time()
    answer = input("\nYour answer: ")
    end = time.time()

    elapsed = end - start
    correct = 0


    for i in range(len(answer)):
        if i < len(sentence):
            if answer[i] == sentence[i]:
                correct += 1

    accuracy = correct / max(len(sentence), len(answer)) * 100
    wpm = (correct / 5) / (elapsed / 60)
    score = round(wpm * accuracy / 100)

    scores.append(wpm)

    if wpm >= 60:
        quote = "You're moving like prime McQueen!"
    elif wpm >= 40:
        quote = "Sheeesh, that's fast!"
    elif wpm >= 25:
        quote = "Not bad, keep going!"
    else:
        quote = "Practice makes perfect!"


    print("\n=== RESULTS ===")
    print("Time:", round(elapsed, 2), "seconds")
    print("WPM:", round(wpm, 2))
    print("Accuracy:", round(accuracy, 2), "%")
    print("Score:", score)
    print("\n" + quote)



def main():
    print("=== SPEED TYPING TEST ===")

    while True:
        print("\n[1] Start Game")
        print("[2] Exit")

        choice = input("Select: ")

        match choice:
            case "1":
                play_game()

            case "2":
                print("\n=== SESSION SUMMARY ===")

                if len(scores) > 0:
                    print("Games played:", len(scores))
                    print("Average WPM:", round(statistics.mean(scores), 2))
                    print("Best WPM:", round(max(scores), 2))
                else:
                    print("No games played.")

                print("Thanks for playing!")
                break

            case _:
                print("Invalid option!")

main()