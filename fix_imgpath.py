with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'document.getElementById("QuestionImg").src="../"+act["Question_Image"]'
new = 'document.getElementById("QuestionImg").src=act["Question_Image"]'

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Opraveno - odstranen "../" prefix z cesty obrazku')
else:
    print('NENALEZENO - retezec nebyl nalezen')
