#!/usr/bin/env python3
"""Render the front page of The World Register for Friday 20 November 2026.

Draws a one-page newspaper: masthead with the date in large type, a lead
story beside a dotted world map, three columns of regional sections and a
science / tech / culture strip along the foot of the page. The picture is
written to entry.png next to this file; main.py only copies that file.
"""

from PIL import Image, ImageDraw, ImageFont

PAGE_W = 1024
PAGE_H = 1024
PAPER = (247, 243, 234)
INK = (26, 24, 20)
FAINT = (92, 86, 76)
ACCENT = (142, 26, 22)
RULE = (40, 38, 34)

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)


F_NAME = font(SERIF_B, 57)
F_DATE = font(SANS_B, 30)
F_SUB = font(SANS_R, 12.5)
F_KICK = font(SANS_B, 12)
F_LEAD_H = font(SANS_B, 25)
F_LEAD_B = font(SANS_R, 12.5)
F_SEC = font(SANS_B, 14.5)
F_HEAD = font(SANS_B, 12.5)
F_BODY = font(SANS_R, 10.2)
F_CAP = font(SANS_R, 10.5)
F_FOOT = font(SANS_R, 11)

LEAD_HEAD = "US, China and Russia Sign Joint Peace Declaration in Shenzhen"
LEAD_BODY = (
    "Trump, Xi and Putin, meeting face to face for the first time as a trio, "
    "reaffirmed that nuclear war must never be fought and pledged further "
    "nuclear-risk talks. The declaration set no arms cuts and no timetable, "
    "and settled neither the war in Ukraine nor the conflict with Iran."
)

SECTIONS_LEFT = [
    ("EUROPE", [
        ("Russian Missiles Strike Three Kyiv Bridges",
         "An overnight barrage hit three bridges over the Dnipro in Kyiv, "
         "killing at least 3 people and injuring about 15. Mayor Klitschko "
         "said fires broke out across the capital."),
        ("Ukrainian Drones Hit Russian Chemical Plant",
         "Kyiv's drones struck the Dorogobuzh fertiliser complex in "
         "Russia's Smolensk region, sparking explosions and a fire. The "
         "plant makes ammonium nitrate; damage was unverified."),
        ("Merz Rejects a 'New Yalta' for Europe",
         "Chancellor Friedrich Merz warned Europe will not accept a "
         "settlement negotiated by the great powers alone, invoking "
         "Yalta in 1945. Macron backed a European seat at talks."),
        ("EU and Britain Hold Second Brussels Summit",
         "Antonio Costa and Ursula von der Leyen met Prime Minister Andy "
         "Burnham to deepen post-Brexit ties, with trade, energy, security "
         "and youth mobility on the summit agenda."),
        ("Denmark Approves Arctic Pact With US and Greenland",
         "Parliament in Copenhagen ratified a trilateral deal expanding "
         "the US defence presence around Pituffik Space Base, affirming "
         "Danish sovereignty over Greenland."),
    ]),
    ("AFRICA", [
        ("Somalia Orders UAE Ambassador Out in 72 Hours",
         "Mogadishu gave the Emirati envoy three days to leave in a dispute "
         "over sovereignty and security ties in the Horn of Africa. Abu "
         "Dhabi rejected the hostile characterisation of its role."),
        ("Sudan's War Deepens the Displacement Crisis",
         "Fighting ground on, driving more civilians from their homes "
         "in what aid agencies call the world's largest displacement "
         "crisis, as armed groups shift allegiances."),
        ("Africa Presses COP31 for Faster Climate Finance",
         "African negotiators demanded that adaptation money pledged at "
         "the Antalya climate talks reach drought- and flood-hit countries "
         "faster, saying delays cost harvests and lives."),
        ("Nigeria Moves to Decriminalise Attempted Suicide",
         "Lawmakers advanced a reform ending criminal penalties for "
         "attempted suicide, shifting the response toward medical care "
         "and social support in a landmark legal change."),
    ]),
]

SECTIONS_MID = [
    ("ASIA-PACIFIC", [
        ("World Court: Myanmar Committed Genocide",
         "The International Court of Justice found Myanmar responsible "
         "for genocide against the Rohingya in 2017 and ordered "
         "reparations. A million Rohingya remain displaced."),
        ("Cyclone Akvan Makes Landfall in India",
         "Cyclone Akvan came ashore on India's eastern coast after mass "
         "evacuations, bringing flooding rains and damaging winds and "
         "threatening coastal crops."),
        ("Russian Bombers Enter Taiwan's Air Zone",
         "Two Russian Tu-95 bombers entered Taiwan's air defence zone "
         "during the APEC summit in China, and Taiwan scrambled fighter "
         "jets to shadow them."),
        ("China Holds Lending Rates for 18th Month",
         "The People's Bank kept benchmark loan prime rates unchanged "
         "for an eighteenth straight month, balancing support for a "
         "slowing economy against yuan pressure."),
        ("Japan Core Inflation Rises to 2.2%",
         "Core consumer prices rose 2.2% in October from a year earlier, "
         "keeping pressure on the Bank of Japan as households weigh "
         "higher food and energy bills against slow wage growth."),
        ("South Korea Reports First Cholera Case in a Decade",
         "Health authorities confirmed the country's first cholera case "
         "in about ten years and began tracing the source of infection "
         "to check whether anyone else was exposed."),
    ]),
    ("OCEANIA", [
        ("Severe Cyclone Xavier, Category 4, Stalks the Pacific",
         "Fiji's meteorological centre tracked Severe Tropical Cyclone "
         "Xavier at Category 4 in the South Pacific, warning island "
         "communities to prepare for destructive winds."),
        ("Pacific Islands Demand Reliable Climate Support",
         "Island governments facing drought, rising seas and salt water "
         "in their wells pressed COP31 for adaptation finance they can "
         "count on, not pledges that arrive years late."),
        ("Australia and Japan Tighten Security Coordination",
         "Canberra and Tokyo agreed to deepen defence and maritime "
         "coordination with Indo-Pacific partners after APEC, balancing "
         "trade with China against regional security concerns."),
    ]),
]

SECTIONS_RIGHT = [
    ("MIDDLE EAST", [
        ("US Blockade Holds as Tanker Attacks Near Hormuz Rise",
         "The US Navy kept its blockade of Iranian shipping in Hormuz "
         "while attacks on tankers near Oman's Khasab port rose to a "
         "new monthly high, the UK agency UKMTO said."),
        ("Iraq Strikes Deal With Kataib Hezbollah",
         "Baghdad reached a compromise letting state forces enter Jurf "
         "al-Sakhar while the Iran-backed militia relocates, testing "
         "the government's authority."),
        ("US Iran Campaign Cost Put at $48.3 Billion",
         "A Pentagon official told lawmakers the American military "
         "campaign against Iran has cost about $48.3 billion so far, "
         "fuelling debate over the open-ended operation."),
        ("Gaza Child Death Toll Passes 22,000, Authorities Say",
         "Palestinian health authorities reported more than 22,000 "
         "children killed in Gaza during the war, as aid groups warned "
         "over damaged hospitals."),
    ]),
    ("AMERICAS", [
        ("Anthropic's $81 Billion IPO Is the Largest Ever",
         "The AI company raised $81 billion in a record Nasdaq debut, "
         "surpassing SpaceX's listing; shares opened 33% above the "
         "offer price on heavy demand."),
        ("California Subpoenas Nvidia Over China Chip Fears",
         "Attorney General Rob Bonta is investigating whether advanced "
         "Nvidia processors or trade secrets reached China and whether "
         "investors were misled. No wrongdoing is shown."),
        ("Senate Passes Energy Permitting Reform 62-33",
         "The Senate approved a bipartisan bill speeding permits for "
         "energy and data-centre projects over environmental objections, "
         "sending it toward the president's desk."),
        ("Haiti Police Say 34 Gang Suspects Killed",
         "Police reported killing at least 34 suspected gang members in "
         "an operation in Port-au-Prince's Martissant district, a "
         "neighbourhood long held by armed groups."),
        ("Lula Advances Indigenous Land Rights With Raoni",
         "President Lula da Silva moved to grant legal recognition to "
         "Indigenous territory on a visit to Amazon leader Chief Raoni, "
         "tying land rights to fighting deforestation."),
    ]),
]

STRIP = [
    ("Voyager 1's Signals Now Take a Day",
     "NASA's 1977 probe is so far off that its radio signals take about "
     "24 hours to reach Earth: a one-light-day milestone."),
    ("Microsoft 365 Outage Disrupts Work Worldwide",
     "Outlook, Teams and other services were down for over nine hours, "
     "disrupting governments, schools and businesses."),
    ("COP31 Deadlocked on Fossil Fuels at the Close",
     "The Antalya climate summit reached its final day with negotiators "
     "split over wording on phasing out fossil fuels."),
    ("GTA VI Tops $2 Billion in Early Sales",
     "Early industry estimates put the game's launch revenue above $2 "
     "billion, an entertainment record; official figures are pending."),
    ("Cincinnati Mourns Fiona the Hippo",
     "The zoo's beloved hippo, famous since her premature birth, died "
     "after swallowing a visitor's hat, prompting grief."),
]

# Dotted world map: (row, first col, last col) land spans on a 56x24 grid.
MAP_SPANS = [
    (1, 4, 13), (1, 30, 33), (1, 37, 53),
    (2, 3, 17), (2, 27, 27), (2, 29, 34), (2, 36, 55),
    (3, 3, 18), (3, 28, 35), (3, 36, 55),
    (4, 4, 18), (4, 29, 35), (4, 36, 54), (4, 50, 50),
    (5, 5, 17), (5, 29, 34), (5, 36, 53),
    (6, 6, 16), (6, 37, 52), (6, 50, 50),
    (7, 8, 13), (7, 26, 35), (7, 36, 48),
    (8, 9, 12), (8, 25, 36), (8, 37, 47), (8, 43, 44),
    (9, 25, 36), (9, 39, 41), (9, 43, 45),
    (10, 26, 35), (10, 40, 41), (10, 43, 45),
    (11, 26, 35), (11, 40, 40), (11, 43, 44),
    (12, 15, 18), (12, 27, 34),
    (13, 15, 19), (13, 27, 34), (13, 43, 43), (13, 46, 46), (13, 49, 49),
    (14, 15, 20), (14, 28, 33), (14, 44, 44), (14, 47, 47),
    (15, 16, 20), (15, 28, 33), (15, 46, 50),
    (16, 16, 21), (16, 28, 32), (16, 45, 51),
    (17, 16, 21), (17, 29, 32), (17, 45, 51),
    (18, 17, 21), (18, 29, 31), (18, 34, 34), (18, 46, 50),
    (19, 17, 20), (19, 29, 31), (19, 46, 49),
    (20, 17, 20), (20, 47, 48),
    (21, 18, 19), (21, 54, 54),
    (22, 18, 19), (22, 54, 54),
    (23, 18, 18),
]


def wrap(draw, text, fnt, width):
    """Greedy word wrap against a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def story(draw, x, y, w, head, body, head_f=F_HEAD, body_f=F_BODY):
    """Draw one story; return the y just below it."""
    for line in wrap(draw, head, head_f, w):
        draw.text((x, y), line, font=head_f, fill=INK)
        y += 13
    y += 1
    for line in wrap(draw, body, body_f, w):
        draw.text((x, y), line, font=body_f, fill=(52, 49, 44))
        y += 11
    return y + 5


def section(draw, x, y, w, title, items):
    draw.rectangle([x, y, x + w, y + 18], fill=INK)
    draw.text((x + 6, y + 2), title, font=F_SEC, fill=PAPER)
    y += 24
    for head, body in items:
        y = story(draw, x, y, w, head, body)
    return y


def draw_map(draw, x, y, cell):
    land = set()
    for row, first, last in MAP_SPANS:
        for col in range(first, last + 1):
            land.add((row, col))
    r = max(1.6, cell * 0.30)
    for row, col in sorted(land):
        cx = x + col * cell + cell / 2
        cy = y + row * cell + cell / 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 96, 120))


def main():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(img)
    m = 26
    right = PAGE_W - m

    # Masthead
    d.line([m, 14, right, 14], fill=RULE, width=3)
    name = "The World Register"
    tw = d.textlength(name, font=F_NAME)
    d.text(((PAGE_W - tw) / 2, 20), name, font=F_NAME, fill=INK)
    d.line([m, 88, right, 88], fill=RULE, width=1)
    date = "FRIDAY 20 NOVEMBER 2026"
    tw = d.textlength(date, font=F_DATE)
    d.text(((PAGE_W - tw) / 2, 94), date, font=F_DATE, fill=ACCENT)
    sub = "The whole day in one page  ·  33 stories  ·  7 regions  ·  Vol. I — No. 20"
    tw = d.textlength(sub, font=F_SUB)
    d.text(((PAGE_W - tw) / 2, 130), sub, font=F_SUB, fill=FAINT)
    d.line([m, 150, right, 150], fill=RULE, width=3)

    # Lead story with the map beside it
    ly = 162
    d.text((m, ly), "THE LEAD — SHENZHEN SUMMIT", font=F_KICK, fill=ACCENT)
    y = ly + 18
    for line in wrap(d, LEAD_HEAD, F_LEAD_H, 618):
        d.text((m, y), line, font=F_LEAD_H, fill=INK)
        y += 30
    y += 2
    for line in wrap(d, LEAD_BODY, F_LEAD_B, 618):
        d.text((m, y), line, font=F_LEAD_B, fill=(52, 49, 44))
        y += 17
    draw_map(d, 672, 158, 5.5)
    cap = "One day, seven regions: Friday 20 November 2026."
    d.text((672, 158 + 24 * 5.5 + 5), "\n".join(wrap(d, cap, F_CAP, 326)),
           font=F_CAP, fill=FAINT)
    d.line([m, 308, right, 308], fill=RULE, width=1)

    # Three columns of regional sections
    col_w = 316
    xs = [m, m + col_w + 12, m + 2 * (col_w + 12)]
    ends = []
    for x, secs in zip(xs, (SECTIONS_LEFT, SECTIONS_MID, SECTIONS_RIGHT)):
        cy = 320
        for title, items in secs:
            cy = section(d, x, cy, col_w, title, items)
        ends.append(cy)
    col_bottom = max(ends)

    # Science, tech and culture strip
    sy = col_bottom + 2
    d.line([m, sy, right, sy], fill=RULE, width=3)
    d.text((m, sy + 6), "SCIENCE, TECH & CULTURE", font=F_SEC, fill=ACCENT)
    sy += 30
    cell_w = (right - m - 4 * 10) // 5
    for i, (head, body) in enumerate(STRIP):
        story(d, m + i * (cell_w + 10), sy, cell_w, head, body)

    # Footer
    d.line([m, PAGE_H - 34, right, PAGE_H - 34], fill=RULE, width=1)
    foot = "Compiled from the day's reporting — The World Register — Friday 20 November 2026"
    tw = d.textlength(foot, font=F_FOOT)
    d.text(((PAGE_W - tw) / 2, PAGE_H - 28), foot, font=F_FOOT, fill=FAINT)

    img.save("entry.png", optimize=True)
    print("columns end at", ends, "strip starts", col_bottom)


if __name__ == "__main__":
    main()
