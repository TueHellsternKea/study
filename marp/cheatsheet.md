# Cheat Sheet
Her er de Markdown kommandoer jeg brugere mest

## Opstart
Denne *kode* skal placeres i topen af Markdown filen

    ---
    title: Din titel
    theme: gaia
    _class: lead
    paginate: true
    marp: true
    backgroundColor: #fff
    size: 4K
    @auto-scaling true
    html: true
    ---

## Background
Du kan sætte baggrund farven på alle slide eller på et enkelt slide.

Denne kode sætter baggrunds farven på dette slide og alle efterfølgende

        <!-- backgroundColor: black -->
        
Hvis det kun er på det slide hvor koden står skal du bruge, forskelden er en **_
**

        <!-- _backgroundColor: black -->
        
## Tekst farve
Du kan sætte tekst farven på alle slide eller på et enkelt slide.

Denne kode sætter tekst farven på dette slide og alle efterfølgende

        <!-- color: white -->
        
Hvis det kun er på det slide hvor koden står skal du bruge, forskelden er en **_
**
        <!-- _color: white -->

## Footer
Footer teksten indsættes i nederste venstre hjørne. Det er ikke muligt at inkludere billeder i footer

Indsætter samme footer tekst, fra dette slide og frem

        <!-- footer: Tekst -->

Brug denne kommado til at *nulstile*

        <!-- footer: "" -->

Denne footer tekst indsættes kun på dette ene slide

        <!-- _footer: Kun dette slide -->
