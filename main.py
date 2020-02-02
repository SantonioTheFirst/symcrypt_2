string = """а годы шли да шли быстро и неслышно как подснежные воды протекала молодость елены в бездействии внешнем во внутренней борьбе и тревоге подруг у нее не было изо всех девиц посещавших дом стаховых она не сошлась ни с одной родительская власть никогда не тяготела над еленой а с шестнадцатилетнего возраста она стала почти совсем независима она зажила собственной своею жизнью но жизнью одинокой ее душа и разгоралась и погасала одиноко она билась как птица в клетке а клетки не было никто не стеснял ее и никто не удерживал а она рвалась и томилась она иногда сама себя не понимала даже боялась самой себя все что окружало ее казалось ей не то бессмысленным не то непонятным как жить без любви а любить некого думала она и страшно становилось ей от этих дум от этих ощущений восемнадцати лет она чуть не умерла от злокачественной лихорадки потрясенный до основания весь ее организм от природы здоровый и крепкий долго не мог справиться последние следы болезни исчезли наконец но отец елены николаевны все еще не без озлобления толковал об ее нервах иногда ей приходило в голову что она желает чего то чего никто не желает о чем никто не мыслит в целой россии потом она утихала даже смеялась над собой беспечно проводила день за днем но внезапно что то сильное безымянное с чем она совладеть не умела так и закипало в ней так и просилось вырваться наружу гроза проходила опускались усталые не взлетевшие крылья но порывы эти не обходились ей даром как она ни старалась не выдать того что в ней происходило тоска взволнованной души сказывалась в самом ее наружном спокойствии и родные ее часто были вправе пожимать плечами удивляться и не понимать ее странностей в день с которого начался наш рассказ елена дольше обыкновенного не отходила от окна она много думала о берсеньеве о своем разговоре с ним потребность в защите информации возникает в связи с необходимостью обеспечить секретность исследований в стратегических областях правильно распределять информацию о промышленных разработках и регулировать информацию о личности в современном обществе начало восьмидесятых годов рассматривается как начальный пункт когда социальные протесты в демократических странах помогли сплестись глобальной сети хакеров политический флирт на почве нарушения прав человека породил тьму организаций хакеров в массе стран мира почти одновременно менее чем за год эти группы узнали прелесть сотрудничества их члены свободно обменивались идеями через национальные границы часто по украденным паролям дающим бесплатный доступ к телефонной сети несколько причин обьединившись вместе сделали международный компьютерный разбой лекгим и действенным новые технологии создавшие более мощные и дешевые компьютеры развитие коммуникаций для связи и международный характер стандартов установленных транснациональными корпорациями в принципе есть лишь два вида угрозы раскрытие и видоизменение данных раскрытие данных предполагает что кому то случайно или после целенаправленных действий стал известен смысл информации этот вид нарушения встречается наиболее часто последствия могут быть самые разные если похищен текст книги справочника на которую потрачены месяцы работы десятков людей то для коллектива авторов это катастрофа и потери могут выражаться в тысячах долларов однако если книга уже издана то достаточно лишь слегка пожурить похитителя и рассказать о случившемся в отделе новостей газеты или по телевидению похититель может сделать книге великолепную рекламу очень важную информацию оберегаемую от раскрытия представляют сведения о людях истории болезни письма состояния счетов в банках однако по мнению большого числа специалистов угрозы личности с введением компьютеров остались на том же уровне и в том же состоянии что и до обширного использования эвм в современном мире туризм становится все более важной быстроразвивающейся отраслью хозяйства доходы от туризма становятся важной частью валютных поступлений во многих странах развитие туризма способствует росту общественного производства улучшению его структуры росту производительности труда во многих отраслях экономики даже не имеющих к туризму прямого отношениям еждународное туристское потребление стимулирует многочисленные экономические процессы открывающие дополнительные рынки для продукции нетуристских отраслей создавая тем самым условия для роста производства все эти факторы делают развитие индустрии туризма очень важным для стран с переходным типом экономики экономические трудности которые переживают эти государства не могут не сказаться на уровне развития туризма но при этом каждая страна имеет в этом отношении свою специфику цель данной работы рассмотреть и проанализировать организацию туристской деятельности в стране с переходным типом экономики на примере венгрии в начале рассматриваются теоретико методические положения исследования затем дается оценка различных факторов развития индустрии туризма венгрии природноресурсный культурноисторический и инфраструктурный потенциал комплексное туристское районирование далее проводится анализ современного состояния индустрии туризма венгрии ее отдельных компонентов на фоне общего уровня экономического развития страны дается оценка социально экономической роли индустрии туризма в экономике венгрии и в заключение проводится общий анализ организации туристской деятельности в странах с переходным типом экономики в общем и венгрии в частности венгрия принадлежа к странам с переходным типом экономики имеет тем не менее специфические черты которые отличают ее от других стран этого типа в отношении развития индустрии туризма основной такой чертой является то что туризм венгрии развивается уже давно еще в начале двадцатого века в этой стране сложились традиционные туристские связи туризм является важной отраслью народного хозяйства современной"""

def remove_symbols(string):
    remove_symbols = [',', '.', '!', '\"', '-', ' ', ';', ':', '?', '–']
    for symbol in remove_symbols:
        string = string.replace(symbol, '')
    return string

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

string = string.lower()
string.replace('\n', ' ')
string.replace('\0', ' ')
text_numbers = text_to_numbers(string)
key_string = 'матвей лох'
key_numbers = text_to_numbers(key_string)
length_of_text = len(text_numbers)
key_sequence = key_sequence_generator(length_of_text, key_numbers)
encrypted_numbers = encrypt(text_numbers, key_sequence)
encrypted_text = numbers_to_text(encrypted_numbers)
print(encrypted_text)
encrypted_numbers1 = text_to_numbers(encrypted_text)
decrypted_numbers = decrypt(encrypted_numbers1, key_sequence)
text = numbers_to_text(decrypted_numbers)
# print(text)
