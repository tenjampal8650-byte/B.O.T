from core.agent import Jarvis


def main():
    jarvis = Jarvis()

    print("JARVIS is online.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("JARVIS: Goodbye.")
            break

        response = jarvis.process(user_input)

        print(f"JARVIS: {response}")


if __name__ == "__main__":
    main()
