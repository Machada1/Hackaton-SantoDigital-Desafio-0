from itertools import chain, combinations

def get_subsets(arr):
    return list(chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1)))

def main():

    try:
        input_string = input("Digite um array de números inteiros separados por espaço: ")
        arr = list(map(int, input_string.split()))
        
        result = get_subsets(arr)
        
        print("Todos os subconjuntos são:")
        for subset in result:
            print(list(subset))
    except ValueError:
        print("Digite números inteiros válidos separados por espaço.")

if __name__ == "__main__":
    main()
