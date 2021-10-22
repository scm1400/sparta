input = "hello my name is sparta"

alphabet_occurrence_array = [0] * 26

def find_max_occurred_alphabet(string):
    for char in input:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char)-ord('a')] +=1

    return chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array))+97)


result = find_max_occurred_alphabet(input)
print(result)