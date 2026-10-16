"""Generates me/about_business.pdf — the Garliclo business profile.

Edit the CONTENT section below and re-run:
    python tools/make_business_pdf.py
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (Image, KeepTogether, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "me" / "about_business.pdf"
LOGO = ROOT / "assets" / "logo.png"

PLUM = colors.HexColor("#3A2733")
OLIVE = colors.HexColor("#3E422C")
CREAM = colors.HexColor("#F1EEE7")
SAND = colors.HexColor("#DCD7CB")

# ----------------------------------------------------------------------------- CONTENT

OVERVIEW = (
    "Garliclo, also known as Nader Garlic, is a Lebanese restaurant supply business based in Sin El Fil (Metn), "
    "led by Joseph Nader and part of a family name in garlic since 1980. It specializes in one product: air-peeled "
    "garlic. We supply clean, whole, ready-to-cook garlic cloves to restaurants, industrial kitchens, and "
    "butcheries. Our promise: you don't peel, we peel for you. No chopping. No peeling. No mess."
)

MISSION = (
    "To save Lebanese kitchens hours of tedious peeling every week, while keeping garlic quality, hygiene, "
    "and taste consistent, at honest and transparent prices."
)

VISION = (
    "To become the first name Lebanese kitchens think of for ready-to-use garlic, and to grow from peeled "
    "cloves into a full range of convenient garlic products."
)

# (product, origin / process, price per kg)
PRODUCTS = [
    ("Peeled & trimmed, large cloves", "Chinese garlic, air-peeled and trimmed by Garliclo (premium)", "$4.00"),
    ("Peeled, untrimmed", "Chinese garlic, air-peeled by Garliclo, root end left on", "$3.35"),
    ("Peeled, untrimmed (imported)", "Peeled in and imported from China", "$3.20"),
    ("Peeled, trimmed, frozen (imported)", "Peeled, trimmed and frozen in China; long storage", "$3.00"),
]

PROCESS = [
    ("Selection", "We source firm, mature Chinese-variety garlic bulbs and sort out damaged or sprouting heads."),
    ("Breaking", "Bulbs are gently broken into individual cloves."),
    ("Air peeling", "Bursts of compressed air lift the skin off each clove: no knives, no soaking, no chemicals, no added water."),
    ("Inspection", "Cloves are checked by hand; bruised or imperfect cloves are removed."),
    ("Trimming", "For our trimmed range, the hard root end is cut off so the clove is 100% usable."),
    ("Packing", "Cloves are packed hygienically and kept cold until delivery."),
]

CUSTOMERS = [
    "Restaurants, including shawarma and grill shops (toum, marinades, sauces)",
    "Industrial and central kitchens",
    "Butcheries",
    "New food and beverage businesses: Garliclo is a must when opening one",
]

STORAGE = [
    "Fresh peeled garlic: keep refrigerated at 0-4 C. Best used within 2-3 weeks unopened, and within a few days once opened.",
    "Frozen peeled garlic: keep frozen at -18 C, for up to 12 months. Thaw in the fridge and do not refreeze.",
    "Fresh air-peeled garlic is recommended for raw uses such as toum; frozen garlic is ideal for cooking, sauces and marinades.",
]

ORDERING = [
    "Order by WhatsApp or phone at +961 70 546 473, by phone at +961 3 793 752, by email at garliclo.lb@gmail.com, or by Instagram DM (@garliclo.lb).",
    "Customers can also leave their name and email (plus optional phone number, area, product and weekly quantity) with our virtual assistant, and the Garliclo team gets back to them personally.",
    "We deliver along the coast from Beirut to Batroun, including the areas in between (Metn, Jounieh, Jbeil); other areas across Lebanon can be arranged with the team.",
    "The team confirms the quantity, final price, delivery day, delivery fee and payment method for every order.",
    "Bulk, wholesale and recurring weekly orders for businesses are welcome; volume pricing is quoted case by case.",
]

TEAM = [
    ("Joseph Nader", "Owner",
     "Joseph leads Garliclo, carrying on the Nader family's experience in garlic since 1980. He oversees "
     "sourcing, quality control, and relationships with restaurant and kitchen partners."),
    ("Production team", "Air-peeling line",
     "Runs the peeling, inspection, trimming and packing line, with a focus on hygiene and consistency."),
    ("Delivery & customer care", "Orders and follow-up",
     "Confirms orders, schedules deliveries, and follows up on every customer question or piece of feedback."),
]

UVP = [
    ("Air-peeled, never soaked", "Whole, firm, unbruised cloves with natural flavor and no chemicals or added water."),
    ("Zero prep", "Trimmed cloves are 100% usable straight out of the pack."),
    ("Hours saved every week", "A busy shawarma shop can peel several kilos a day; we do it for them."),
    ("Consistent, all year long", "Chefs trust Garliclo to keep recipes consistent plate after plate, every season."),
    ("Experience since 1980", "Decades of family know-how in sourcing and handling garlic."),
    ("Choice at every budget", "Locally air-peeled premium garlic or lower-cost imported options, including frozen."),
    ("Honest, published prices", "A clear per-kilo price list, and a real person who confirms every order."),
]

FAQ = [
    ("What is the difference between trimmed and untrimmed?",
     "Trimmed (muqamma') cloves have the hard root end cut off, so they are ready to use with zero waste. "
     "Untrimmed cloves still have the root end and cost a little less."),
    ("What is the difference between your own garlic and the imported options?",
     "Products 1 and 2 are air-peeled by Garliclo, so they are fresher and firmer. Products 3 and 4 are peeled in "
     "China and imported, which makes them more affordable."),
    ("Do you use chemicals or water to peel?",
     "No. Our own line peels with compressed air only."),
    ("Do you sell garlic paste, toum, or whole garlic bulbs?",
     "Not at the moment. Our current range is peeled garlic cloves only, but we love hearing what customers would like next."),
    ("Where do you deliver?",
     "Along the coast from Beirut to Batroun, including Metn, Jounieh and Jbeil. Other areas across Lebanon can be arranged; contact the team to check."),
    ("Is there a minimum order or a delivery fee?",
     "These depend on the area and quantity, so the team confirms them with each customer."),
]

# ----------------------------------------------------------------------------- LAYOUT

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=26,
                    textColor=OLIVE, leading=32, spaceBefore=4, spaceAfter=6, alignment=TA_CENTER)
TAG = ParagraphStyle("Tag", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=11.5,
                     textColor=PLUM, alignment=TA_CENTER, spaceAfter=10)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13.5,
                    textColor=colors.white, backColor=PLUM, borderPadding=(4, 6, 4, 6),
                    spaceBefore=12, spaceAfter=8, leading=17)
BODY = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.2,
                      leading=14.5, textColor=colors.HexColor("#2B2228"))
SMALL = ParagraphStyle("Small", parent=BODY, fontSize=9.4, leading=13)
BOLD = ParagraphStyle("Bold", parent=BODY, fontName="Helvetica-Bold")
CELL_H = ParagraphStyle("CellH", parent=BODY, fontName="Helvetica-Bold", textColor=colors.white)


def section(title, *flowables):
    return [KeepTogether([Paragraph(title, H2), *flowables[:1]]), *flowables[1:]]


def bullets(items):
    return [Paragraph(f"&bull;&nbsp; {i}", BODY) for i in items]


def kv_table(rows, col_widths, header=None):
    data = [[Paragraph(h, CELL_H) for h in header]] if header else []
    data += [[Paragraph(str(c), BOLD if j == 0 else BODY) for j, c in enumerate(r)] for r in rows]
    t = Table(data, colWidths=col_widths, hAlign="LEFT")
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [CREAM, colors.white]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, SAND),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), OLIVE))
    t.setStyle(TableStyle(style))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(SAND)
    canvas.rect(0, 0, A4[0], 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(PLUM)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawString(18 * mm, 4.5 * mm, "Garliclo | Nader Garlic  |  @garliclo.lb  |  +961 70 546 473")
    canvas.drawRightString(A4[0] - 18 * mm, 4.5 * mm, f"Business profile  |  page {doc.page}")
    canvas.restoreState()


def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=14 * mm, bottomMargin=18 * mm,
                            title="Garliclo - Business Profile", author="Garliclo")
    W = A4[0] - 36 * mm
    story = []
    if LOGO.exists():
        story.append(Image(str(LOGO), width=46 * mm, height=37.7 * mm))
    story += [Paragraph("GARLICLO", H1),
              Paragraph("Air-peeled garlic since 1980. No chopping. No peeling. No mess.", TAG)]

    story += section("1. Company Overview", Paragraph(OVERVIEW, BODY))
    story += section("2. Mission & Vision",
                     Paragraph(f"<b>Mission.</b> {MISSION}", BODY), Spacer(1, 4),
                     Paragraph(f"<b>Vision.</b> {VISION}", BODY))
    story += section("3. Products & Prices (New prices, USD per kg)",
                     kv_table(PRODUCTS, [W * 0.33, W * 0.52, W * 0.15],
                              header=["Product", "Origin & process", "Price / kg"]),
                     Spacer(1, 4),
                     Paragraph("All products are Chinese-variety garlic. Delivery fees and volume discounts are "
                               "confirmed by the team for each order.", SMALL))
    story += section("4. How Air Peeling Works",
                     kv_table([(f"{i + 1}. {a}", b) for i, (a, b) in enumerate(PROCESS)], [W * 0.25, W * 0.75]))
    story += section("5. Who We Serve", *bullets(CUSTOMERS))
    story += section("6. Our Unique Value Proposition", kv_table(UVP, [W * 0.3, W * 0.7]))
    story += section("7. Storage & Shelf Life", *bullets(STORAGE))
    story += section("8. Ordering & Delivery", *bullets(ORDERING))
    story += section("9. Our Team",
                     kv_table([(f"{n}<br/><font size=8.5 color='#3A2733'>{r}</font>", b) for n, r, b in TEAM],
                              [W * 0.28, W * 0.72]))
    story += section("10. Frequently Asked Questions",
                     *[p for q, a in FAQ for p in (Paragraph(f"<b>Q. {q}</b>", BODY),
                                                   Paragraph(a, BODY), Spacer(1, 5))])
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
