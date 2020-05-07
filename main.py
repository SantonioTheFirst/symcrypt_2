file = open('text', 'r')
string = file.read()
file.close()

def remove_symbols(string):
    remove_symbols = [',', '.', '!', '\"', '-', ' ', ';', ':', '?', '–']
    for symbol in remove_symbols:
        string = string.replace(symbol, '')
    return string

probabilities = [0.07998, 0.01592, 0.04533, 0.01687, 0.02977, 0.08483, 0.0094, 0.01641,
                 0.07367, 0.01208, 0.03486, 0.04343, 0.03203, 0.067, 0.10983, 0.02804,
                 0.04746, 0.05473, 0.06318, 0.02615, 0.00267, 0.00966, 0.00486, 0.0145,
                 0.00718, 0.00361, 0.00037, 0.01898, 0.00331, 0.00639, 0.02001, 0.170205779
                ]

def text_to_numbers(string):
    numbers = []
    for i in range(0, len(string)):
        if string[i] == 'а':
            numbers.append(0)
        elif string[i] == 'б':
            numbers.append(1)
        elif string[i] == 'в':
            numbers.append(2)
        elif string[i] == 'г':
            numbers.append(3)
        elif string[i] == 'д':
            numbers.append(4)
        elif string[i] == 'е':
            numbers.append(5)
        elif string[i] == 'ё':
            numbers.append(5)
        elif string[i] == 'ж':
            numbers.append(6)
        elif string[i] == 'з':
            numbers.append(7)
        elif string[i] == 'и':
            numbers.append(8)
        elif string[i] == 'й':
            numbers.append(9)
        elif string[i] == 'к':
            numbers.append(10)
        elif string[i] == 'л':
            numbers.append(11)
        elif string[i] == 'м':
            numbers.append(12)
        elif string[i] == 'н':
            numbers.append(13)
        elif string[i] == 'о':
            numbers.append(14)
        elif string[i] == 'п':
            numbers.append(15)
        elif string[i] == 'р':
            numbers.append(16)
        elif string[i] == 'с':
            numbers.append(17)
        elif string[i] == 'т':
            numbers.append(18)
        elif string[i] == 'у':
            numbers.append(19)
        elif string[i] == 'ф':
            numbers.append(20)
        elif string[i] == 'х':
            numbers.append(21)
        elif string[i] == 'ц':
            numbers.append(22)
        elif string[i] == 'ч':
            numbers.append(23)
        elif string[i] == 'ш':
            numbers.append(24)
        elif string[i] == 'щ':
            numbers.append(25)
        elif string[i] == 'ъ':
            numbers.append(26)
        elif string[i] == 'ы':
            numbers.append(27)
        elif string[i] == 'ь':
            numbers.append(26)
        elif string[i] == 'э':
            numbers.append(28)
        elif string[i] == 'ю':
            numbers.append(29)
        elif string[i] == 'я':
            numbers.append(30)
        elif string[i] == ' ':
            numbers.append(31)
    return numbers

def numbers_to_text(numbers_array):
    # print(len(numbers_array))
    string = ''
    for i in range(0, len(numbers_array)):
        if numbers_array[i] == 0:
            string += 'а'
        elif numbers_array[i] == 1:
            string += 'б'
        elif numbers_array[i] == 2:
            string += 'в'
        elif numbers_array[i] == 3:
            string += 'г'
        elif numbers_array[i] == 4:
            string += 'д'
        elif numbers_array[i] == 5:
            string += 'е'
        elif numbers_array[i] == 6:
            string += ('ж')
        elif numbers_array[i] == 7:
            string += ('з')
        elif numbers_array[i] == 8:
            string += ('и')
        elif numbers_array[i] == 9:
            string += ('й')
        elif numbers_array[i] == 10:
            string += ('к')
        elif numbers_array[i] == 11:
            string += ('л')
        elif numbers_array[i] == 12:
            string += ('м')
        elif numbers_array[i] == 13:
            string += ('н')
        elif numbers_array[i] == 14:
            string += ('о')
        elif numbers_array[i] == 15:
            string += ('п')
        elif numbers_array[i] == 16:
            string += ('р')
        elif numbers_array[i] == 17:
            string += ('с')
        elif numbers_array[i] == 18:
            string += ('т')
        elif numbers_array[i] == 19:
            string += ('у')
        elif numbers_array[i] == 20:
            string += ('ф')
        elif numbers_array[i] == 21:
            string += ('х')
        elif numbers_array[i] == 22:
            string += ('ц')
        elif numbers_array[i] == 23:
            string += ('ч')
        elif numbers_array[i] == 24:
            string += ('ш')
        elif numbers_array[i] == 25:
            string += ('щ')
        elif numbers_array[i] == 26:
            string += ('ь')
        elif numbers_array[i] == 27:
            string += ('ы')
        elif numbers_array[i] == 28:
            string += ('э')
        elif numbers_array[i] == 29:
            string += ('ю')
        elif numbers_array[i] == 30:
            string += ('я')
        elif numbers_array[i] == 31:
            string += (' ')
    return string

def key_sequence_generator(length_of_text, key_numbers):
    key_length = len(key_numbers)
    key_sequence = []
    for i in range(0, length_of_text):
        key_sequence.append(key_numbers[i % key_length])
    return key_sequence

def encrypt(text_numbers, key_sequence):
    encrypted_numbers = []
    mod = 32
    for i in range(0, len(text_numbers)):
        encrypted_numbers.append((text_numbers[i] + key_sequence[i]) % mod)
    return encrypted_numbers

def mod_sub(a, b, mod):
    result = a - b
    if result > mod:
        while result > mod:
            result -= mod
    elif result < mod and result > 0:
        return result
    elif result < 0:
        while result < 0:
            result += mod
    return result

def decrypt(text_numbers, key_sequence):
    mod = 32
    result_numbers = []
    for i in range(0, len(text_numbers)):
        result = mod_sub(text_numbers[i], key_sequence[i], mod)
        result_numbers.append(result)
    return result_numbers

def calculate_Dr(encrypted_text):
    Dr_array = []
    for r in range(2,50):
        if r >= len(encrypted_text):
            break
        temp = 0
        for i in range(0,len(encrypted_text)-r):
            if encrypted_text[i] == encrypted_text[i + r]:
                temp += 1
        Dr_array.append(temp)
    print(Dr_array)

def create_blocks(encrypted_text_numbers):
    r = int(input('Длина ключа: '))
    Y = []
    for i in range(0, r):
        Y.append([])
        Y[i].append(encrypted_text_numbers[i::r])
    # print(Y)
    return Y

def calculate_count(array, element):
    counter = 0
    for i in range(0, len(array)):
        if array[i] == element:
            counter += 1
    return counter

def find_position_of_max_element(array):
    max = array[0]
    pos = 0
    for i in range (0,len(array)):
        if array[i] > max:
            max = array[i]
            pos = i
    return pos

def crack(encrypted_text_numbers, probabilities):
    Y = create_blocks(encrypted_text_numbers)
    # print(type(Y))
    key = []
    print(len(Y))
    for block in Y:
        array_of_summs = []
        for k in range(0, 32):
            summ = 0
            for a in range(0, 32):
                summ += (probabilities[a] * block[0].count((a + k) % 32))
                # print(summ, 'a:', a, 'k:', k, 'a+k:', (a+k)%32, 'count:', block.count(3), 'prob:', probabilities[a])
            array_of_summs.append(summ)
        key.append(find_position_of_max_element(array_of_summs))
        # print(key)
    return key

string = string.lower()
string.replace('\n', ' ')
string.replace('\0', ' ')
text_numbers = text_to_numbers(string)
key_string = 'кавалеристы спешились'
key_numbers = text_to_numbers(key_string)
length_of_text = len(text_numbers)
key_sequence = key_sequence_generator(length_of_text, key_numbers)
encrypted_numbers = encrypt(text_numbers, key_sequence)
encrypted_text = numbers_to_text(encrypted_numbers)
# print(encrypted_text)
# encrypted_numbers1 = text_to_numbers(encrypted_text)
# decrypted_numbers = decrypt(encrypted_numbers1, key_sequence)
# text = numbers_to_text(decrypted_numbers)
# print(text)
calculate_Dr(encrypted_numbers)
print(numbers_to_text(crack(encrypted_numbers, probabilities)))

#
# file = open('crack_it', 'r')
# crack_it = file.read()
# file.close()
# crack_in_numbers = text_to_numbers(crack_it)
# calculate_Dr(crack_in_numbers)
# print(numbers_to_text(crack(crack_in_numbers, probabilities)))
