import json

with open('c99_final.json', encoding='utf-8') as f:
    data = json.load(f)
questions = data['questions']

compact = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))

with open('index.html', encoding='utf-8') as f:
    html = f.read()

start_tag = '<script type="application/json" id="Test_C99">'
end_tag = '</script>'

start_idx = html.index(start_tag) + len(start_tag)
end_idx = html.index(end_tag, start_idx)

new_html = html[:start_idx] + compact + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Done.', len(questions), 'questions written.')
