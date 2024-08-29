def generate_asterisk_list(n):
    return ['*' * i for i in range(1, n + 1)]

def main():
    try:
        n = int(input("Digite um número inteiro para gerar a lista de asteriscos: "))
        result = generate_asterisk_list(n)
        print(result)
    except ValueError:
        print("Digite um número inteiro válido.")

if __name__ == "__main__":
    main()
