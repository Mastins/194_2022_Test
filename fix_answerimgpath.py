with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('getElementById("AnswerImg_1").src="../"+act["Answer_1_Image"]',
     'getElementById("AnswerImg_1").src=act["Answer_1_Image"]'),
    ('getElementById("AnswerImg_2").src="../"+act["Answer_2_Image"]',
     'getElementById("AnswerImg_2").src=act["Answer_2_Image"]'),
    ('getElementById("AnswerImg_3").src="../"+act["Answer_3_Image"]',
     'getElementById("AnswerImg_3").src=act["Answer_3_Image"]'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'Opraveno: {old[:60]}...')
    else:
        print(f'NENALEZENO: {old[:60]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nCelkem opraveno: {count}/3')
