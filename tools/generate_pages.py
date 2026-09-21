from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PAGES={
  'explore':'Explore RecLora','rooms':'Rooms','events':'Events','creators':'Creators','news':'News and announcements','about':'About RecLora','contact':'Contact','help':'Help center','guidelines':'Community guidelines','safety':'Safety and privacy','downloads':'Downloads','membership':'Membership','creator-studio':'Creator studio','creator-resources':'Creator resources','showcase':'Showcase','collections':'Collections','search':'Search','status':'Service status','changelog':'Changelog','press':'Press kit','partners':'Partners','terms':'Terms of use','accessibility':'Accessibility'
}

def doc(page, base):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Editable RecLora community page"><link rel="stylesheet" href="{base}assets/site.css"></head><body><div data-page="{page}" data-base="{base}"></div><script src="{base}assets/app.js"></script></body></html>\n'''

(ROOT/'index.html').write_text(doc('home',''),encoding='utf-8')
for slug in PAGES:
    (ROOT/'pages'/f'{slug}.html').write_text(doc(slug,'../'),encoding='utf-8')
print(f'Generated {len(PAGES)+1} HTML pages.')
