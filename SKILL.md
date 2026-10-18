# The Fisher Online – modování ikon a textur

## Účel
Postup pro vyhledávání, tvorbu, náhradu a balení ikon The Fisher Online.

## Cesty v instalaci hry
Používej cestu relativně od `theFisher_Data/StreamingAssets`:
- Zdrojové ikony: `Textures/Weapons/<ID>.png`
- Anglické názvy: `Localization/English/WpnLang.xml`
- Workshop staging: `_WorkshopTextures`
- Zálohy originálů: `IconOriginalsBackup_YYYY-MM-DD/Textures/Weapons`

## Pravidla
- Herní názvy ani ID neměň, pokud o to uživatel výslovně nepožádá.
- Před náhradou ulož původní texturu do časově označené zálohy. Nikdy nepřepisuj první záložní kopii.
- Zachovej cílové rozměry PNG a průhlednost, pokud ji původní ikona používá.
- Před prací ověř existenci ID, názvy v lokalizaci, rozměry a stav aktuálního Workshop stagingu.
- Pro nové bitmapové ikony použij imagegen: jeden samostatný objekt, čitelný v malém rozměru, realistický herní styl, průhledné pozadí. Výsledné soubory přenes do projektu a ověř jejich alfa kanál a rozměry.
- Nový Workshop balíček má obsahovat `_MODINFO.xml`, `image.jpg`, `obsah.txt` a textury ve `Textures/Weapons/`. Náhled `image.jpg` musí mít přesně 800 × 452 px.
- Nový mod začíná s `steammid=0`. Steam ID doplň až po vytvoření/nahrání přes herní Workshop rozhraní. Nepřebírej ID jiného modu.
- Složky `_WorkshopTextures_*` jsou archivované/připravené balíčky; nepředpokládej, že jsou automaticky aktivní nebo publikované.
- Před změnou souborů v `_WorkshopTextures` ověř jeho aktuální obsah. Nepřepisuj metadata ani náhled jiného modu.

## Postup
1. Najdi všechny požadované ikony a ověř ID, názvy a původní rozměry.
2. Vygeneruj nové ikony nebo znovu použij uživatelem schválené výstupy.
3. Zálohuj originály; potom převeď nové PNG na rozměry cíle.
4. Nahraď soubory hry a vlož stejné výsledné PNG do samostatného Workshop balíčku.
5. Vytvoř metadata, seznam ID/názvů a náhled 800 × 452.
6. Ověř XML, počet souborů, shodu herních textur s balíčkem, rozměry a existenci záloh.
7. Ve shrnutí uveď balíček, zálohy, ID a skutečný stav publikování.

## Kontext
Předchozí stav projektu je v `PROJECT_NOTES.md`. Poznámky ber jako orientaci; před každým pokračováním znovu prohlédni aktuální soubory, protože herní adresáře a staging se mohou změnit.
