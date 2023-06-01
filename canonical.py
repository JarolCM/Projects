def primes_until(number: int):
    primes = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            primes.append(i)
    return primes
                

def decomposition(number_to_decompose: int):
    initial_response = f"{number_to_decompose} es descompuesto por:"
    descomposed_final_list_output = []
    descomposed_numbers_list = []
    primes_list = primes_until(number_to_decompose)

    for prime in primes_list:
        if (number_to_decompose % prime == 0):
            descomposed_numbers_list.append(prime)

    for descomposed_number in descomposed_numbers_list:
        elevated_number_times = 0
        while (number_to_decompose % descomposed_number == 0):
            elevated_number_times += 1
            number_to_decompose = number_to_decompose / descomposed_number
        descomposed_final_list_output.append(f"{descomposed_number} ^ {elevated_number_times}")

    return f"{initial_response} {' x '.join(descomposed_final_list_output)}"

if __name__ == '__main__':
    print("==================")
    number_input = int(input("Ingrese el numero: "))
    print("------------------")
    print(decomposition(number_input))
    print("==================")
