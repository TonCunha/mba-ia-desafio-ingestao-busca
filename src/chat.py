from search import search_prompt

def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("Bem-vindo ao chat! Digite sua pergunta ou 'sair' para encerrar.")

    while True:
        try:
            question = input("Você: ").strip()

            if question.lower() == "sair":
                print("Até logo!")
                break

            if not question:
                continue

            answer = chain.invoke(question)
            
            print(f"Bot: {answer.content}")

        except KeyboardInterrupt:
            print("\nAté logo!")
            break
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()