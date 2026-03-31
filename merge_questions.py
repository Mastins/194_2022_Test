import re, json

# Načti aktuální c99_final.json
with open('c99_final.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
questions = data['questions']
current_ids = {q['Quest_ID']: q for q in questions}
print(f'c99_final.json: {len(questions)} otazek')

# Najdi chybějící IDs
all_ids = set(range(1, 541))
missing = sorted(all_ids - set(current_ids.keys()))
print(f'Chybejici ({len(missing)}): {missing}')

# Extrahuj data z 99002022.html
with open('99002022.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'id="Test_C99"[^>]*>(.*?)</script>', content, re.DOTALL)
if not m:
    print('Test_C99 NENALEZENO v 99002022.html')
    exit(1)

raw = m.group(1).strip()
html_questions = json.loads(raw)
html_ids = {q['Quest_ID']: q for q in html_questions}
print(f'99002022.html: {len(html_questions)} otazek')

# Přidej chybějící otázky z HTML
added = []
for qid in missing:
    if qid in html_ids:
        current_ids[qid] = html_ids[qid]
        added.append(qid)
    else:
        print(f'  STALE CHYBI ID {qid} - ani v html neni')

print(f'Doplneno z html: {len(added)} otazek: {added}')

# Seřaď podle Quest_ID a ulož
merged = sorted(current_ids.values(), key=lambda q: q['Quest_ID'])
data['questions'] = merged

with open('c99_final.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Ulozeno: {len(merged)} otazek do c99_final.json')
