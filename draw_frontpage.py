#!/usr/bin/env python3
"""Draw the news-image-20261120 front page: 'The World in One Page'.

Friday 20 November 2026 - 40 stories, 6 continents, one page.
Lead: the ICJ rules Myanmar committed genocide against the Rohingya -
the first time the World Court has found a state guilty of genocide,
9-6, with reparations to be set later. Second: Trump pushes any Iran
war decision to 2027. Third: Cyclone Akvan makes landfall at noon
near Gopalpur, Odisha, after 105,000 people were evacuated.
Verified against Reuters, AP, BBC, The Hindu, IMD, OHCHR and UN
reporting for 19-20 November 2026. Hero: a PIL-drawn globe, no photo.
Output: 1024x1024 PNG, deterministic (no randomness, no network, no clock).
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (17, 17, 17)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = os.path.join(F, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(F, "DejaVuSerif.ttf")
SANS = os.path.join(F, "DejaVuSans.ttf")
SANS_B = os.path.join(F, "DejaVuSans-Bold.ttf")
HERE = os.path.dirname(os.path.abspath(__file__))

COL = {
    "ASIA": (0, 87, 183), "EUROPE": (15, 118, 110), "AFRICA": (166, 90, 0),
    "AMERICAS": (166, 25, 46), "OCEANIA": (109, 40, 217), "WORLD": (120, 90, 0),
    "SPORT": (51, 65, 85),
}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def trunc(draw, text, fnt, max_w):
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + "...", font=fnt) > max_w:
        text = text.rsplit(" ", 1)[0] if " " in text else text[:-1]
    return text + "..."


def draw_globe(d, cx, cy, r):
    """Stylised globe: cream disc, teal meridians, gold verdict badge."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(233, 240, 238),
              outline=(15, 118, 110), width=3)
    for k in range(-2, 3):
        rx = int(r * abs(k) / 2.6) or 6
        d.ellipse([cx - rx, cy - r, cx + rx, cy + r],
                  outline=(15, 118, 110), width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=(15, 118, 110), width=2)
    for dy in (-r // 2, r // 2):
        w = int(math.sqrt(max(r * r - dy * dy, 0)))
        d.line([(cx - w, cy + dy), (cx + w, cy + dy)],
               fill=(15, 118, 110), width=2)
    # continent blobs
    d.ellipse([cx - 52, cy - 48, cx - 8, cy - 6], fill=(15, 118, 110))
    d.ellipse([cx + 6, cy - 30, cx + 44, cy + 8], fill=(15, 118, 110))
    d.ellipse([cx - 30, cy + 14, cx + 12, cy + 48], fill=(15, 118, 110))
    d.ellipse([cx + 30, cy + 26, cx + 54, cy + 52], fill=(15, 118, 110))
    # verdict badge
    bx, by = cx + r - 34, cy - r + 6
    d.ellipse([bx - 26, by - 26, bx + 26, by + 26], fill=(166, 25, 46),
              outline=WHITE, width=2)
    d.text((bx, by - 11), "9-6", font=font(SANS_B, 17), fill=WHITE, anchor="ma")


# (region, headline, deck) - 37 grid stories; lead + 2 strips make 40.
ITEMS = [
    ("WORLD", "GTA VI: $1.84bn in a day", "19.1m copies; biggest launch ever."),
    ("WORLD", "Voyager 1 hits one light-day", "NASA confirms the milestone."),
    ("ASIA", "Trump, Xi, Putin met in Shenzhen", "First-ever three-way summit."),
    ("ASIA", "Modi meets William and Kate", "UK-India ties top the agenda."),
    ("ASIA", "Han Duck-soo conviction overturned", "Korea court voids martial-law case."),
    ("ASIA", "China extends US tariff truce", "24% tariff paused to 10 Jan 2027."),
    ("ASIA", "Iran widens Gulf attacks", "Kuwait base hit; Bahrain struck again."),
    ("ASIA", "APEC closes in Shenzhen", "21 leaders wrap the summit."),
    ("ASIA", "Takaichi seeks dialogue with China", "Japan PM urges calmer ties."),
    ("ASIA", "Taiwan drafts repression crime", "Bill targets cross-border threats."),
    ("ASIA", "AI 171 crash report nearly done", "Centre tells top court probe at fag end."),
    ("ASIA", "ADNOC vessel hit in Hormuz", "One crew member missing."),
    ("ASIA", "Houthis strike Riyadh tower", "Saudi wealth-fund tower damaged."),
    ("ASIA", "Sensex rallies 1.21%", "Nifty tops 25,400 on Thursday."),
    ("EUROPE", "Europe ready for Russia talks", "Leaders seek end to Ukraine war."),
    ("EUROPE", "EU proposes EUR 45bn Ukraine loan", "Covers Kyiv's EUR 70bn shortfall."),
    ("EUROPE", "Tanker off Bulgaria 'hit by projectiles'", "Officials confirm the strike."),
    ("EUROPE", "Ukraine hits Crimean Bridge", "Rail traffic disrupted."),
    ("EUROPE", "COP31 presses climate finance", "India pushes resilient infrastructure."),
    ("AFRICA", "Somalia accuses UAE of secret bases", "Mogadishu alleges unauthorised sites."),
    ("AFRICA", "Libya seizes cocaine, millions of pills", "Haul found in the east, officials say."),
    ("AMERICAS", "Jeffries nominated for Speaker, 251-11", "First Black Speaker if elected in Jan."),
    ("AMERICAS", "Peltola wins Alaska Senate race", "Democrats hold the Alaska seat."),
    ("AMERICAS", "US, Venezuela restore military ties", "Defence chiefs sign agreement."),
    ("AMERICAS", "Fed minutes point to more hikes", "Most officials back further rises."),
    ("AMERICAS", "US proposes tougher green-card rules", "Longer hiring process ahead."),
    ("AMERICAS", "Anthropic valued at $1.5tn", "Report puts AI firm at record high."),
    ("OCEANIA", "Fiji declares drought disaster", "El Nino dries water supplies."),
    ("OCEANIA", "Australia sanctions Israeli settlers", "Over West Bank expansion."),
    ("WORLD", "Hayabusa2 drops asteroid landing", "Engine trouble forces a new plan."),
    ("WORLD", "Pew: Islam largest faith by 2035", "Report projects the crossover."),
    ("WORLD", "Nvidia halts H-series chips to China", "Chipmaker cites export rules."),
    ("WORLD", "Oil slides as Gulf tension rises", "Crude futures fall over 3%."),
    ("SPORT", "Nicholls 113* lifts New Zealand", "NZ 243/5 on day one in Wellington."),
    ("SPORT", "Duckett 133 puts England on top", "England lead the third ODI."),
    ("SPORT", "India beat Malaysia in badminton", "Hong Kong Open progress."),
    ("SPORT", "Women's Asian Hockey Trophy begins", "Champions Trophy opens in 2026."),
]


def main():
    assert len(ITEMS) == 37, len(ITEMS)
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26
    # ---- masthead ----
    d.text((W // 2, 14), "THE WORLD", font=font(SERIF_B, 64), fill=INK, anchor="ma")
    d.text((W // 2, 92), "FRIDAY 20 NOVEMBER 2026  \u2022  40 STORIES  \u2022  6 CONTINENTS  \u2022  ONE PAGE",
           font=font(SANS_B, 15), fill=INK, anchor="ma")
    d.line([(M, 120), (W - M, 120)], fill=INK, width=4)
    d.line([(M, 126), (W - M, 126)], fill=INK, width=1)

    # ---- lead: ICJ genocide ruling, globe hero right ----
    d.text((M, 136), "THE HAGUE  \u2022  WORLD COURT", font=font(SANS_B, 14), fill=COL["EUROPE"])
    d.text((M, 156), "MYANMAR GUILTY", font=font(SERIF_B, 33), fill=INK)
    d.text((M, 194), "OF GENOCIDE", font=font(SERIF_B, 33), fill=INK)
    deck = ("The court finds Myanmar committed genocide against the "
            "Rohingya in 2017 \u2014 the first time a state has been "
            "found guilty of genocide. Nine judges to six.")
    y = 236
    for ln in wrap(d, deck, font(SERIF, 16), 560):
        d.text((M, y), ln, font=font(SERIF, 16), fill=INK)
        y += 21
    hx, hy, hw, hh = 600, 136, 398, 170
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=(16, 42, 54))
    draw_globe(d, hx + hw // 2, hy + 72, 62)
    d.rectangle([hx, hy, hx + hw, hy + hh], outline=INK, width=2)
    d.rectangle([hx, hy + hh - 26, hx + hw, hy + hh], fill=(15, 118, 110))
    d.text((hx + hw // 2, hy + hh - 22), "PEACE PALACE  \u2022  FIRST STATE VERDICT",
           font=font(SANS_B, 13), fill=WHITE, anchor="ma")

    # ---- strip 1: Trump pushes Iran decision to 2027 ----
    ty = 318
    d.rectangle([M, ty, W - M, ty + 40], fill=INK)
    d.text((M + 14, ty + 4), "TRUMP PUSHES IRAN WAR DECISION TO 2027  \u2022  ",
           font=font(SANS_B, 15), fill=(255, 213, 79))
    d.text((M + 14, ty + 22), "'No rush \u2014 we'll see what happens after Jan 1', president says",
           font=font(SANS, 14), fill=WHITE)
    d.text((W - M - 14, ty + 4), "AMERICAS", font=font(SANS_B, 15), fill=(255, 213, 79), anchor="ra")

    # ---- strip 2: Cyclone Akvan landfall ----
    gy = 364
    d.rectangle([M, gy, W - M, gy + 40], fill=(24, 24, 64))
    d.text((M + 14, gy + 4), "CYCLONE AKVAN MAKES LANDFALL AT NOON  \u2022  ",
           font=font(SANS_B, 15), fill=(255, 213, 79))
    d.text((M + 14, gy + 22), "105,000 evacuated as storm hits Odisha coast, winds 100 km/h",
           font=font(SANS, 14), fill=WHITE)
    d.text((W - M - 14, gy + 4), "ASIA", font=font(SANS_B, 15), fill=(255, 213, 79), anchor="ra")

    # ---- 37-item grid: 3 cols x 13 rows ----
    gx, gy2 = M, 416
    cw = (W - 2 * M - 24) // 3
    chh = 42
    for i, (reg, head, deck) in enumerate(ITEMS):
        x = gx + (i % 3) * (cw + 12)
        y = gy2 + (i // 3) * chh
        col = COL[reg]
        d.line([(x, y + 3), (x, y + chh - 7)], fill=col, width=4)
        d.text((x + 10, y), reg, font=font(SANS_B, 9), fill=col)
        d.text((x + 10, y + 11), trunc(d, head, font(SERIF_B, 12), cw - 12),
               font=font(SERIF_B, 12), fill=INK)
        d.text((x + 10, y + 27), trunc(d, deck, font(SANS, 10), cw - 12),
               font=font(SANS, 10), fill=(60, 60, 60))

    # ---- footer ----
    d.text((W // 2, 984), "Sources: Reuters, AP, BBC, The Hindu, IMD, OHCHR, UN  \u2022  Friday 20 November 2026",
           font=font(SANS, 11), fill=GREY, anchor="ma")
    out = os.path.join(HERE, "news.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
