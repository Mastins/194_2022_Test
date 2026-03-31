# 🔌 Elektro Testy - Revizní Technik

Interaktivní testovací aplikace pro přípravu na zkoušky revizního technika podle nařízení vlády č. 194/2022 Sb.

## ✨ Funkce

- 📚 **5 typů testů**: E2/A-1 až E2/A-5 plus C99 (540 otázek)
- 🖼️ **Podpora obrázků**: Schémata, diagramy a fotografie zařízení
- 📊 **Pokročilé vyhodnocení**: Detailní analýza výsledků 
- ⚡ **Offline funkčnost**: Vše funguje bez internetového připojení
- 🎯 **Responzivní design**: Funguje na PC i mobilních zařízeních

## 📁 Struktura projektu

```
📁 elektro-testy/
├── 📁 images/                      # Obrázky k otázkám
│   ├── 📁 general/                 # Obecné obrázky
│   ├── 📁 schemas/                 # Elektrická schémata
│   ├── 📁 equipment/               # Zařízení, komponenty
│   └── 📁 safety/                  # Bezpečnostní prvky
├── 📁 data/
│   └── 📄 99002022.html           # Hlavní testovací aplikace
├── 📄 index.html                   # Vstupní stránka
├── 📄 c99_final.json              # Data otázek s obrázky
├── 📄 add_images.py               # Skript pro přidávání obrázků
└── 📄 README.md                   # Tato dokumentace
```

## 🚀 Rychlý start

1. **Spuštění testů**: Otevřete `index.html` v prohlížeči
2. **Klikněte na "Spustit testy"** pro začátek testování
3. **Vyberte typ testu** a začněte odpovídat

## 🖼️ Přidávání obrázků

### Automatický způsob (doporučený)

```bash
python add_images.py
```

Skript vás provede:
- Vyhledáním otázky podle ID nebo textu
- Přidáním obrázku k otázce nebo odpovědi
- Automatickým uložením změn

### Manuální způsob

Upravte přímo `c99_final.json`:

```json
{
  "Quest_ID": 123,
  "Question": "Jak vypadá tento symbol?",
  "Question_Image": "images/schemas/resistor_symbol.jpg",
  "Answer_1": "Odpor",
  "Answer_1_Image": null,
  "Answer_2": "Kondenzátor", 
  "Answer_2_Image": "images/schemas/capacitor.jpg",
  "Answer_3": "Cívka",
  "Answer_3_Image": null,
  "CorrectA": [1]
}
```

## 📋 Příprava obrázků

### Doporučené formáty
- **JPG**: Pro fotografie a složité obrázky
- **PNG**: Pro schémata s průhledností
- **SVG**: Pro vektorové symboly (škálovatelné)

### Doporučené velikosti
- **Obrázky otázek**: max 600x400 px
- **Obrázky odpovědí**: max 300x200 px
- **Optimální**: 50-200 KB na obrázek

### Jak vystřihnout z PDF
1. Otevřete PDF v prohlížeči/čtečce
2. Udělejte screenshot požadované části
3. Ořízněte v editoru (Paint, GIMP, Photoshop)
4. Uložte jako JPG s kvalitou 80-90%

## 🗃️ Organizace obrázků

```
📁 images/
├── 📁 general/          # Obecné obrázky, loga
├── 📁 schemas/          # Elektrická schémata, obvody
│   ├── symbols/         # Elektrické symboly
│   ├── diagrams/        # Schéma zapojení
│   └── circuits/        # Kompletní obvody
├── 📁 equipment/        # Zařízení a komponenty
│   ├── meters/          # Měřící přístroje
│   ├── switches/        # Spínače, jističe
│   └── cables/          # Kabely, vodiče
└── 📁 safety/           # Bezpečnostní prvky
    ├── signs/           # Výstražné značky
    └── equipment/       # Ochranné pomůcky
```

## 🛠️ Technické informace

### Podporované formáty obrázků
- JPG/JPEG
- PNG  
- SVG
- GIF (statické)

### Kompatibilní prohlížeče
- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

### JSON struktura obrázků

Každá otázka může obsahovat:
- `Question_Image`: Obrázek k otázce
- `Answer_1_Image`: Obrázek k odpovědi A
- `Answer_2_Image`: Obrázek k odpovědi B  
- `Answer_3_Image`: Obrázek k odpovědi C

Hodnoty: `"images/category/filename.jpg"` nebo `null`

## 🔧 Řešení problémů

### Obrázek se nezobrazuje
1. ✅ Zkontrolujte cestu k souboru
2. ✅ Ověřte, že obrázek existuje
3. ✅ Zkontrolujte název souboru (velká/malá písmena)
4. ✅ Ujistěte se, že JSON je validní

### Testovací aplikace nefunguje
1. 🔍 Otevřete Developer Tools (F12)
2. 📋 Zkontrolujte Console pro chyby
3. 📁 Ověřte struktur souborů
4. 🔄 Zkuste obnovit cache (Ctrl+F5)

### Velké obrázky spomalují načítání
1. 🖼️ Optimalizujte obrázky (TinyPNG, ImageOptim)
2. 📐 Změňte velikost na doporučené rozměry
3. 🗜️ Snižte kvalitu JPG na 80-90%

## 📈 Další rozwoj

- [ ] Podpora video souborů
- [ ] Offline aplikace (PWA)
- [ ] Export statistik do Excel
- [ ] Mobilní optimalizace
- [ ] Tmavý režim

## 🤝 Kontribuce

1. Fork projektu
2. Vytvořte feature branch (`git checkout -b feature/nova-funkce`)
3. Commitněte změny (`git commit -m 'Přidat novou funkci'`) 
4. Push do branch (`git push origin feature/nova-funkce`)
5. Otevřete Pull Request

---

📝 **Licence**: MIT  
🔧 **Verze**: 2.0.0 (s podporou obrázků)  
📅 **Poslední aktualizace**: Březen 2026