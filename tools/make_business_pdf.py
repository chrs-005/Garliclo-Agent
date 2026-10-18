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
    "Garliclo, also known as Nader Garlic, is a Lebanese garlic supplier founded in 1980 by Joseph Nader. "
    "It specializes in one product: air-peeled garlic for businesses. From our main factory in Sin El Fil (Metn), "
    "we supply clean, whole, ready-to-cook garlic cloves to restaurants, industrial kitchens, butcheries, "
    "supermarkets and food businesses all over Lebanon. Our promise: you don't peel, we peel for you. "
    "No chopping. No peeling. No mess."
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
    ("Peeled & trimmed, large cloves", "Chinese garlic, air-peeled and trimmed in our Sin El Fil factory (premium)", "$4.00"),
    ("Peeled, untrimmed", "Chinese garlic, air-peeled in our Sin El Fil factory, root end left on", "$3.35"),
    ("Peeled, untrimmed (imported)", "Arrives already peeled from China", "$3.20"),
    ("Peeled, trimmed, frozen (imported)", "Arrives already peeled, trimmed and frozen from China; long storage", "$3.00"),
]

PROCESS = [
    ("Selection", "We source firm, mature Chinese-variety garlic bulbs and sort out damaged or sprouting heads."),
    ("Breaking", "Bulbs are gently broken into individual cloves."),
    ("Air peeling", "Bursts of compressed air lift the skin off each clove: air-peeled, not water-peeled. No knives, no soaking, no chemicals."),
    ("Inspection", "Cloves are checked by hand; bruised or imperfect cloves are removed."),
    ("Trimming", "For our trimmed range, the hard root end is cut off so the clove is 100% usable."),
    ("Packing", "Cloves are vacuum-sealed in the quantity each customer needs and kept cold until delivery."),
]

CUSTOMERS = [
    "Restaurants, including shawarma and grill shops (toum, marinades, sauces)",
    "Industrial and central kitchens",
    "Butcheries",
    "Supermarkets",
    "Caterers and hotels",
    "Food manufacturers (sauces, pickles, ready meals)",
    "New food and beverage businesses: Garliclo is a must when opening one",
    "Business customers only: we do not sell small quantities to households.",
]

PACKAGING = [
    "We pack to order, in whatever quantity the customer needs.",
    "Fresh garlic: vacuum-sealed bags of 1 kg, 5 kg or 10 kg, or custom quantities for bulk orders.",
    "Frozen garlic: 1 kg bags packed in 10 kg cartons.",
]

STORAGE = [
    "Fresh air-peeled garlic: keep refrigerated at 0-4 C. Stays fresh for up to 3 weeks unopened; use within 3-5 days once opened.",
    "Frozen peeled garlic: keep frozen at -18 C, for up to 12 months. Thaw in the fridge and do not refreeze.",
    "Fresh garlic is best for raw uses such as toum; frozen garlic is ideal for cooking, sauces and marinades.",
]

# (zone, areas, fee per order)
DELIVERY = [
    ("Zone 1: Greater Beirut", "Beirut, Sin El Fil, Dekwaneh, Bourj Hammoud, Dora, Jdeideh, Hazmieh, Baabda", "$3"),
    ("Zone 2: Metn, Keserwan & Aley", "Antelias, Zalka, Jounieh, Kaslik, Broummana, Beit Mery, Aley, Choueifat, Khalde", "$5"),
    ("Zone 3: Jbeil, Batroun & Chouf", "Jbeil, Amchit, Batroun, Damour, Deir el Qamar, Beiteddine", "$7"),
    ("Zone 4: North, Bekaa & Saida", "Tripoli, Koura, Zgharta, Zahle, Chtaura, Saida", "$10"),
    ("Zone 5: Far areas", "Akkar, Baalbek-Hermel, Tyre, Nabatieh, Marjayoun", "$15"),
]

ORDERING = [
    "Order by WhatsApp or phone on our main business number +961 70 546 473, or call +961 3 793 752, email garliclo.lb@gmail.com, or send an Instagram DM (@garliclo.lb).",
    "Customers can also leave their name and email (plus optional phone number, area, product and weekly quantity) with our virtual assistant, and the Garliclo team gets back to them personally.",
    "The team confirms the quantity, final price and delivery day for every order. Volume discounts for large or recurring orders are quoted case by case.",
    "Payment: we accept all forms of payment: cash (USD or LBP), bank transfer, card, Whish Money and OMT.",
]

TEAM = [
    ("Joseph Nader", "Founder",
     "Joseph founded Nader Garlic in 1980 and built it into Garliclo, the air-peeled garlic brand. Four decades in "
     "the garlic trade shape how he sources, checks and delivers every order to restaurant and kitchen partners."),
    ("Production team", "Sin El Fil factory",
     "Runs the air-peeling, inspection, trimming and packing line, with a focus on hygiene and consistency."),
    ("Delivery & customer care", "Orders and follow-up",
     "Confirms orders, schedules deliveries all over Lebanon, and follows up on every question or piece of feedback."),
]

UVP = [
    ("Air-peeled, not water-peeled", "Whole, firm, unbruised cloves with natural flavor, no chemicals and no added water."),
    ("Zero prep", "Trimmed cloves are 100% usable straight out of the pack."),
    ("Hours saved every week", "A busy shawarma shop can peel several kilos a day; we do it for them."),
    ("Consistent, all year long", "Chefs trust Garliclo to keep recipes consistent plate after plate, every season."),
    ("Experience since 1980", "Four decades of know-how in sourcing and handling garlic."),
    ("Choice at every budget", "Garlic air-peeled in our factory, or lower-cost imported options, including frozen."),
    ("Delivery all over Lebanon", "Clear per-zone delivery fees, and free delivery from 50 kg in Zones 1 to 3."),
]

FAQ = [
    ("What is the difference between trimmed and untrimmed?",
     "Trimmed (muqamma') cloves have the hard root end cut off, so they are ready to use with zero waste. "
     "Untrimmed cloves still have the root end and cost a little less."),
    ("What is the difference between your own garlic and the imported options?",
     "Products 1 and 2 are air-peeled in our Sin El Fil factory, so they are fresher and firmer. Products 3 and 4 "
     "arrive already peeled from China, which makes them more affordable."),
    ("What does 'air-peeled, not water-peeled' mean?",
     "Our machines peel with compressed air only. Water-peeled garlic absorbs moisture, which softens it and shortens "
     "its life; air-peeled cloves stay dry, firm and full of flavor."),
    ("Do you sell to households?",
     "No. Garliclo supplies businesses only: restaurants, kitchens, butcheries, supermarkets and other food businesses."),
    ("Do you sell garlic paste, toum, or whole garlic bulbs?",
     "Not at the moment. Our current range is peeled garlic cloves only, but we love hearing what customers would like next."),
    ("Is there free delivery?",
     "Yes: orders of 50 kg or more get free delivery in Zones 1 to 3. Otherwise the fee depends on the delivery zone."),
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
        story.append(Image(str(LOGO), width=46 * mm, height=46 * mm * 561 / 587))
    story += [Paragraph("GARLICLO", H1),
              Paragraph("Air-peeled, not water-peeled. Since 1980. No chopping. No peeling. No mess.", TAG)]

    story += section("1. Company Overview", Paragraph(OVERVIEW, BODY))
    story += section("2. Mission & Vision",
                     Paragraph(f"<b>Mission.</b> {MISSION}", BODY), Spacer(1, 4),
                     Paragraph(f"<b>Vision.</b> {VISION}", BODY))
    story += section("3. Products & Prices (New prices, USD per kg)",
                     kv_table(PRODUCTS, [W * 0.33, W * 0.52, W * 0.15],
                              header=["Product", "Origin & process", "Price / kg"]),
                     Spacer(1, 4),
                     Paragraph("All products are Chinese-variety garlic. Volume discounts are quoted by the team.", SMALL))
    story += section("4. How Air Peeling Works",
                     kv_table([(f"{i + 1}. {a}", b) for i, (a, b) in enumerate(PROCESS)], [W * 0.25, W * 0.75]))
    story += section("5. Who We Serve", *bullets(CUSTOMERS))
    story += section("6. Our Unique Value Proposition", kv_table(UVP, [W * 0.3, W * 0.7]))
    story += section("7. Packaging", *bullets(PACKAGING))
    story += section("8. Storage & Shelf Life", *bullets(STORAGE))
    story += section("9. Delivery Fees (all over Lebanon, from our Sin El Fil factory)",
                     kv_table(DELIVERY, [W * 0.3, W * 0.58, W * 0.12], header=["Zone", "Areas", "Fee / order"]),
                     Spacer(1, 4),
                     Paragraph("Orders of 50 kg or more get free delivery in Zones 1 to 3. For areas not listed, "
                               "the team confirms the fee.", SMALL))
    story += section("10. Ordering & Payment", *bullets(ORDERING))
    story += section("11. Our Team",
                     kv_table([(f"{n}<br/><font size=8.5 color='#3A2733'>{r}</font>", b) for n, r, b in TEAM],
                              [W * 0.28, W * 0.72]))
    story += section("12. Frequently Asked Questions",
                     *[p for q, a in FAQ for p in (Paragraph(f"<b>Q. {q}</b>", BODY),
                                                   Paragraph(a, BODY), Spacer(1, 5))])
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
