# write your code here
def header(level, text):
    if 1 <= int(level) <= 6:
        if int(level) == 1:
            return f'# {text}\n'
        elif int(level) == 2:
            return f'## {text}\n'
        elif int(level) == 3:
            return f'### {text}\n'
        elif int(level) == 4:
            return f'#### {text}\n'
        elif int(level) == 5:
            return f'##### {text}\n'
        else:
            return f'###### {text}\n'
    else:
        print('The level should be within the range of 1 to 6')


def plain(text):
    return text


def bold(text):
    return f'**{text}**'


def italic(text):
    return f'*{text}*'


def link(label, url):
    return f'[{label}]({url})'


def inline_code(text):
    return f'`{text}`'


def new_line():
    return '\n'


def print_header(lst):
    while True:
        level = input('Level: ')
        if int(level) > 6:
            print('The level should be within the range of 1 to 6')
            continue
        else:
            word = input('Text: ')
            phrase = header(level, word)
            lst.append(phrase)
            for x in lst:
                print(x)
            break


def print_word(element, lst):
    if element == 'plain':
        word = input('Text: ')
        phrase = plain(word)
        lst.append(phrase)
        for y in lst:
            print(y, end='')
    elif element == 'bold':
        word = input('Text: ')
        phrase = bold(word)
        lst.append(phrase)
        for z in lst:
            print(z, end='')
    elif element == 'italic':
        word = input('Text: ')
        phrase = italic(word)
        lst.append(phrase)
        for a in lst:
            print(a, end='')
    elif element == 'inline-code':
        word = input('Text: ')
        phrase = inline_code(word)
        lst.append(phrase)
        for b in lst:
            print(b, end='')
    elif element == 'link':
        label = input('Label: ')
        url = input('URL: ')
        phrase = link(label, url)
        lst.append(phrase)
        for c in lst:
            print(c, end='')


def ord_unord_list(element, lst):
    rows_list = []
    txt = ''
    while True:
        n_rows = input("Number of Rows: ")
        if int(n_rows) > 0 and element == 'ordered-list':
            for z in range(int(n_rows)):
                rows_list.append(str(z + 1) + '. ' + input(f'Row #{z + 1}: '))
            txt += '\n'.join(rows_list) + '\n'
            lst.append(txt)
            for y in lst:
                print(y, end='')
            break
        elif int(n_rows) > 0 and element == 'unordered-list':
            for v in range(int(n_rows)):
                rows_list.append('* ' + input(f'Row #{v + 1}: '))
            txt += '\n'.join(rows_list)
            lst.append(txt)
            for x in lst:
                print(x, end='')
            break
        else:
            print('The number of rows should be greater than zero')


formatters = [
    'header',
    'plain',
    'bold',
    'italic',
    'inline-code',
    'new-line',
    'link',
    'ordered-list',
    'unordered-list',
    '!done'
]
text_formatted = []
formatter = input('Choose a formatter: ').lower()
while True:
    if formatter == 'header':
        print_header(text_formatted)
        formatter = input('Choose a formatter: ').lower()
    elif formatter == 'new-line':
        newline = new_line()
        text_formatted.append(newline)
        for i in text_formatted:
            print(i, end='')
        formatter = input('\nChoose a formatter: ').lower()
    elif formatter not in formatters:
        print('Unknown formatting type or command')
        formatter = input('Choose a formatter: ').lower()
    elif formatter == 'ordered-list' or formatter == 'unordered-list':
        ord_unord_list(formatter, text_formatted)
        formatter = input('\nChoose a formatter: ').lower()
    elif formatter == '!done':
        with open('output.md', 'w') as output:
            for text in text_formatted:
                output.write(text)
        break
    else:
        print_word(formatter, text_formatted)
        formatter = input('\nChoose a formatter: ').lower()
