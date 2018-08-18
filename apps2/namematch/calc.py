import re

def isAllChineseText(text):
    m = re.match(u'^[\u4e00-\u9fa5]+', text)
    if m:
        return text == m.group()
    return False

def isChineseWord(word):
    if len(word) == 1:
        if u'\u4e00' <= word <= u'\u9fff':
            return True

    return False

UNKNOWN = 0
MALE = 1
FEMALE = 2

def getNumber(word):
    if len(word) == 1 and isChineseWord(word):
        num = word.encode('unicode_escape')[2:].decode()
        result = (int(num, 16))%99
        while result < 10:
            result = result + 10
        return result

    else:
        return 0

# 计算名字
def calcName(name1, gender1, name2, gender2):
    gender1 = FEMALE
    gender2 = MALE
    count = max(len(name1), len(name2), 3)
    
    names = []
    if gender1 == gender2:        
        names = [name1, name2]
        names.sort()
    else:
        if gender1 == FEMALE:   # 女性排在前面
            names = [name1, name2]
        else:
            names = [name2, name1]
    
    words = []
    for i in range(count):
        if i< len(names[0]):
            words.append(names[0][i])
        else:
            words.append('❤')

        if i< len(names[1]):
            words.append(names[1][i])
        else:
            words.append('❤')

    data = {
        'words': words
    }

    calc = []
    for i in words:
        calc.append(getNumber(i))

    def getSum(numbers, result):
        result.append(numbers)
        if len(numbers) == 2:            
            res = (numbers[0]*10+numbers[1])%1000
            while res < 100:
                res += 100
            return res

        items = []
        for i in range(len(numbers)-1):
            items.append( (numbers[i] + numbers[i+1]))

        return getSum(items, result)

    data['process'] = []

    data['score'] = getSum(calc, data['process'])

    return data