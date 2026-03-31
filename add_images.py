import json
import os

def add_image_to_question():
    """Interaktivní skript pro přidávání obrázků k otázkám"""
    
    # Načti JSON
    with open('c99_final.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("🖼️ Skript pro přidávání obrázků do otázek")
    print("=" * 50)
    
    while True:
        # Zobraz možnosti
        print("\n📋 Co chcete udělat?")
        print("1. Přidat obrázek k otázce")
        print("2. Přidat obrázek k odpovědi")
        print("3. Najít otázku podle textu")
        print("4. Zobrazit otázku podle ID")
        print("5. Uložit a ukončit")
        
        choice = input("\n👉 Vaše volba (1-5): ").strip()
        
        if choice == "1":
            add_question_image(data)
        elif choice == "2":
            add_answer_image(data)
        elif choice == "3":
            search_question(data)
        elif choice == "4":
            show_question_by_id(data)
        elif choice == "5":
            save_and_exit(data)
            break
        else:
            print("❌ Neplatná volba!")

def add_question_image(data):
    """Přidá obrázek k otázce"""
    try:
        quest_id = int(input("🆔 Zadejte Quest_ID otázky: "))
        question = find_question_by_id(data, quest_id)
        
        if not question:
            print(f"❌ Otázka s ID {quest_id} nebyla nalezena!")
            return
        
        print(f"\n📝 Otázka: {question['Question'][:80]}...")
        
        print("\n📁 Dostupné kategorie:")
        print("  - images/general/")
        print("  - images/schemas/") 
        print("  - images/equipment/")
        print("  - images/safety/")
        
        image_path = input("🖼️ Zadejte cestu k obrázku (např. images/schemas/symbol.jpg): ").strip()
        
        if image_path:
            question['Question_Image'] = image_path
            print(f"✅ Obrázek přidán k otázce {quest_id}")
        
    except ValueError:
        print("❌ Neplatné ID!")

def add_answer_image(data):
    """Přidá obrázek k odpovědi"""
    try:
        quest_id = int(input("🆔 Zadejte Quest_ID otázky: "))
        question = find_question_by_id(data, quest_id)
        
        if not question:
            print(f"❌ Otázka s ID {quest_id} nebyla nalezena!")
            return
        
        print(f"\n📝 Otázka: {question['Question'][:80]}...")
        print(f"A: {question['Answer_1'][:60]}...")
        print(f"B: {question['Answer_2'][:60]}...")
        print(f"C: {question['Answer_3'][:60]}...")
        
        answer_num = input("\n📝 Ke které odpovědi přidat obrázek? (A/B/C): ").strip().upper()
        
        if answer_num not in ['A', 'B', 'C']:
            print("❌ Musíte zadat A, B nebo C!")
            return
        
        image_path = input("🖼️ Zadejte cestu k obrázku: ").strip()
        
        if image_path:
            answer_key = f"Answer_{{'A': '1', 'B': '2', 'C': '3'}[answer_num]}_Image"
            question[answer_key] = image_path
            print(f"✅ Obrázek přidán k odpovědi {answer_num}")
        
    except ValueError:
        print("❌ Neplatné ID!")

def search_question(data):
    """Hledá otázku podle textu"""
    search_text = input("🔍 Zadejte text k hledání: ").strip().lower()
    
    found = []
    for q in data['questions']:
        if search_text in q['Question'].lower():
            found.append(q)
    
    if found:
        print(f"\n✅ Nalezeno {len(found)} otázek:")
        for q in found[:10]:  # max 10 výsledků
            print(f"  ID {q['Quest_ID']}: {q['Question'][:80]}...")
    else:
        print("❌ Žádné otázky nenalezeny!")

def show_question_by_id(data, quest_id=None):
    """Zobrazí otázku podle ID"""
    try:
        if quest_id is None:
            quest_id = int(input("🆔 Zadejte Quest_ID: "))
        
        question = find_question_by_id(data, quest_id)
        
        if question:
            print(f"\n📋 Otázka ID {quest_id}:")
            print(f"❓ {question['Question']}")
            print(f"🖼️ Obrázek otázky: {question.get('Question_Image', 'Žádný')}")
            print(f"\nA: {question['Answer_1']}")
            print(f"🖼️ Obrázek A: {question.get('Answer_1_Image', 'Žádný')}")
            print(f"\nB: {question['Answer_2']}")
            print(f"🖼️ Obrázek B: {question.get('Answer_2_Image', 'Žádný')}")
            print(f"\nC: {question['Answer_3']}")
            print(f"🖼️ Obrázek C: {question.get('Answer_3_Image', 'Žádný')}")
            print(f"\n✅ Správné odpovědi: {question['CorrectA']}")
        else:
            print(f"❌ Otázka s ID {quest_id} nebyla nalezena!")
            
    except ValueError:
        print("❌ Neplatné ID!")

def find_question_by_id(data, quest_id):
    """Najde otázku podle Quest_ID"""
    for question in data['questions']:
        if question['Quest_ID'] == quest_id:
            return question
    return None

def save_and_exit(data):
    """Uloží data a ukončí"""
    # Záloha
    with open('c99_final_backup.json', 'w', encoding='utf-8') as f:
        with open('c99_final.json', 'r', encoding='utf-8') as orig:
            f.write(orig.read())
    
    # Uložení
    with open('c99_final.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✅ Data uložena!")
    print("📄 Záloha vytvořena: c99_final_backup.json")

if __name__ == "__main__":
    add_image_to_question()