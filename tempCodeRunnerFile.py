evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )


for item in evenNumbersGenerator:    
    print(item)

print(sys.getsizeof(evenNumbersGenerator))
