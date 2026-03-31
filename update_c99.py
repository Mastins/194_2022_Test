import json

with open('c99_final.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']
compact = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))
new_line = '<script type="application/json" id="Test_C99">' + compact + '</script>'

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines[341] = new_line + '\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f'Hotovo - nahrazen radek 342, {len(questions)} otazek, {len(new_line)} znaku')
