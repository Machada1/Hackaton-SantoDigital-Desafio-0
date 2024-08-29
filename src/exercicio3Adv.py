from itertools import chain, combinations

def get_subsets(arr, min_size=0, max_size=None, distinct_only=False, sort_subsets=False):
    if distinct_only:
        arr = list(set(arr))  

    if max_size is None:
        max_size = len(arr)  

    all_subsets = chain.from_iterable(combinations(arr, r) for r in range(min_size, max_size + 1))
    
    if sort_subsets:
        all_subsets = sorted((tuple(sorted(subset)) for subset in all_subsets), key=lambda x: (len(x), x))
    else:
        all_subsets = sorted(all_subsets, key=lambda x: (len(x), x))
    
    return list(all_subsets)

def main():
    try:
        input_string = input("Digite um array de números inteiros separados por espaço: ")
        arr = list(map(int, input_string.split()))
        
        min_size = int(input("Digite o tamanho mínimo dos subconjuntos (0 para sem limite): "))
        max_size = input("Digite o tamanho máximo dos subconjuntos (ou pressione Enter para sem limite): ")
        max_size = int(max_size) if max_size else None
        distinct_only = input("Garantir que os subconjuntos não contenham elementos duplicados (True/False)? ").strip().lower() == 'true'
        sort_subsets = input("Ordenar subconjuntos e elementos dentro dos subconjuntos (True/False)? ").strip().lower() == 'true'
        
        result = get_subsets(arr, min_size, max_size, distinct_only, sort_subsets)
        
        print("Todos os subconjuntos são:")
        for subset in result:
            print(subset)
    except ValueError:
        print("Digite números inteiros válidos.")

if __name__ == "__main__":
    main()
