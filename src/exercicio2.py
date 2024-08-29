def find_min_difference_pairs(arr):
    if len(arr) < 2:
        return []


    arr = sorted(arr)
    
    min_diff = float('inf')
    result = []


    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            result = [(arr[i], arr[i + 1])]
        elif diff == min_diff:
            result.append((arr[i], arr[i + 1]))
    
    return result

def main():
    try:
        input_string = input("Digite um array de números inteiros separados por espaço: ")
        arr = list(map(int, input_string.split()))
        
        result = find_min_difference_pairs(arr)
        
        if result:
            print("Os pares com a menor diferença absoluta são:")
            for pair in result:
                print(pair)
        else:
            print("Não há pares suficientes para calcular a diferença.")
    except ValueError:
        print("Digite números inteiros válidos separados por espaço.")

if __name__ == "__main__":
    main()
