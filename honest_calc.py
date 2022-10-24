# write your code here
memory = 0

msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]


def is_one_digit(v):
    if (-10 < v < 10) and (v.is_integer()):
        return True
    return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]

    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_[7]

    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_[8]

    if msg != '':
        msg = msg_[9] + msg
        print(msg)


while True:

    print(msg_[0])
    calc = input()
    x, oper, y = calc.split()

    if x == 'M' and y == 'M':
        x = y = memory
    elif x == 'M':
        x = memory
    elif y == 'M':
        y = memory

    if str(x).isalpha() or str(y).isalpha():
        print(msg_[1])
    elif oper == '+' or oper == '-' or oper == '*' or oper == '/':
        x = float(x)
        y = float(y)
        check(x, y, oper)
        if oper == '+':
            result = x + y
            print(result)
            print(msg_[4])
            answer4 = input().lower()
            if answer4 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input().lower()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()
            elif answer4 == 'n':
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()

        elif oper == '-':
            result = x - y
            print(result)
            print(msg_[4])
            answer4 = input().lower()
            if answer4 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input().lower()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()
            elif answer4 == 'n':
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()

        elif oper == '*':
            result = x * y
            print(result)
            print(msg_[4])
            answer4 = input().lower()
            if answer4 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input().lower()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()
            elif answer4 == 'n':
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()

        elif oper == '/' and y != 0:
            result = x / y
            print(result)
            print(msg_[4])
            answer4 = input().lower()
            if answer4 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input().lower()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                        else:
                            continue
                else:
                    memory = result
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()
            elif answer4 == 'n':
                print(msg_[5])
                answer5 = input().lower()
                if answer5 == 'y':
                    continue
                elif answer5 == 'n':
                    break
                else:
                    print(msg_[5])
                    answer5 = input().lower()

            else:
                print(msg_[3])
    else:
        print(msg_[2])


