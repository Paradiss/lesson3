with open('referat.txt', 'r', encoding = 'utf-8') as referat:
    text = ''
    for line in referat:
        text += line
    print(len(text))
    words = text.split()
    print(len(words))
    text = text.replace('.','!')    
with open('referat2.txt', 'w', encoding = 'utf-8') as referat2:
    referat2.write(text)