def find_min_difference_pairs(arr, allow_duplicates=True, sorted_pairs=False, unique_pairs=True):
    if len(arr) < 2:
        return []

    arr = sorted(arr)
    
    min_diff = float('inf')
    pairs = set()
    
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            pairs = set()
            pairs.add((arr[i], arr[i + 1]))
        elif diff == min_diff:
            pairs.add((arr[i], arr[i + 1]))
    
    if not allow_duplicates:
        pairs = {pair for pair in pairs if pair[0] != pair[1]}
    
    if unique_pairs:
        pairs = set(tuple(sorted(pair)) for pair in pairs)
    
    result = sorted(pairs) if sorted_pairs else list(pairs)
    
    return result

def main():
    try:
        input_string = input("Digite um array de números inteiros separados por espaço: ")
        arr = list(map(int, input_string.split()))
        
        allow_duplicates = input("Permitir pares com valores duplicados (True/False)? ").strip().lower() == 'true'
        sorted_pairs = input("Ordenar pares em ordem crescente (True/False)? ").strip().lower() == 'true'
        unique_pairs = input("Considerar apenas pares únicos (True/False)? ").strip().lower() == 'true'
        
        result = find_min_difference_pairs(arr, allow_duplicates, sorted_pairs, unique_pairs)
        
        print("Os pares com a menor diferença absoluta são:")
        for pair in result:
            print(pair)
    except ValueError:
        print("Digite números inteiros válidos separados por espaço.")

if __name__ == "__main__":
    main()
