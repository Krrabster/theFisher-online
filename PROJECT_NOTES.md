# The Fisher Online – projektové poznámky

## Repozitář
Tento repozitář uchovává pracovní postup, dokumentaci a připravené texturové balíčky. Existující archiv `3016425373-project.zip` zůstal nedotčený.

## Aktuální balíček
- `mods/cervi-a-larvy/` obsahuje 18 nových ikon, `_MODINFO.xml`, `obsah.txt` a Workshop náhled `image.jpg` 800 × 452 px.
- ID: `1010, 1018, 1019, 1020, 1088, 1163, 1239, 1445, 1648, 1763, 1766, 1767, 1928, 1929, 1930, 1931, 2056, 2425`.
- Názvy a ID herních položek zůstaly stejné.
- Ve hře byly textury nahrazeny; originály jsou v lokální záloze `IconOriginalsBackup_2026-10-19/Textures/Weapons`.
- `_MODINFO.xml` má `steammid=0`; tato sada nebyla zveřejněna na Steam Workshopu.

## Další předchozí práce
- Byly vytvořeny nové ikony mušek/vodního hmyzu pro ID `1436, 1763, 1766, 1767, 2173`.
- Byly připraveny ikony krmiv, dipů a těst (78 položek), úpravy žetonů a úpravy imitací návnad. Příslušné složky se při poslední kontrole nenacházely všechny v instalaci; neobnovovat je odhadem. Nejdřív ověřit aktuální soubory a stav repozitáře.
- Česká vlajka bez rybářské siluety je v `assets/vlajka-cz-800x452.jpg`; je samostatným grafickým assetem a nepatří do balíčku červů a larev.

## Před pokračováním
1. Zkontrolovat aktuální obsah `StreamingAssets/_WorkshopTextures` a jeho `_MODINFO.xml`.
2. Ověřit, které balíčky a herní textury stále existují.
3. Nezveřejňovat originální zálohy.
4. Steam ID doplnit až po vytvoření Workshop položky.

## Koncept nových rybích ikon – pokračovat příště
- Koncept candáta podle hmotnosti je uložen v `concepts/fish-icons/zander-weight-variants/`.
- Začít ID `105` (candát). Varianty se liší hmotností; číselná přípona `_číslo` je velikostní varianta.
- Poslední dvě varianty musí jasně působit jako trofejní kus a světový rekord, převážně změnou proporcí a mohutnosti.
- Před tvorbou finálních textur ověřit přesné pořadí názvů variant. Konceptový obrázek není hotový herní asset.
- Celé zadání a další kroky: `concepts/fish-icons/zander-weight-variants/README.md`.

## Nové rybí ikony – stav první sady
- Dokončena sada ID `5` White-Eye Bream v `concepts/fish-icons/white-eye-bream-id5/`.
- Soubory `5.png`, `5_0.png`, `5_1.png`, `5_2.png`, `5_3.png` zachovávají názvy a mají 512 × 256 px.
- Hmotnostní pořadí podle velikosti původních siluet: `_0` nejmenší, `_1`, nepříponovaná varianta, `_2` trofejní a `_3` světový rekord.
- `0.png`, `1.png`, `-1.png` vynechat. Další platné ID je `6` (Huso). Kompletní zadání první sady je v README dané složky.
