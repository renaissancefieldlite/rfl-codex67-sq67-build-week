#!/usr/bin/env python3
"""Build the public-safe SQ67 white paper PDF from Markdown."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


GOLD = colors.HexColor("#E9C84A")
INK = colors.HexColor("#111111")
MUTED = colors.HexColor("#555555")
LINE = colors.HexColor("#D7D7D7")
SOFT = colors.HexColor("#F6F4EC")


def repo_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        return "uncommitted"


def inline_markup(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(
        r"`([^`]+)`",
        r'<font name="Courier" size="8.5">\1</font>',
        escaped,
    )
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    return escaped


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(inline_markup(text), style)


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["title"] = ParagraphStyle(
        "RFLTitle",
        parent=base["Title"],
        fontName="Helvetica-Bold",
        fontSize=27,
        leading=32,
        alignment=TA_LEFT,
        textColor=INK,
        spaceAfter=14,
    )
    styles["subtitle"] = ParagraphStyle(
        "RFLSubtitle",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=MUTED,
        spaceAfter=8,
    )
    styles["h1"] = ParagraphStyle(
        "RFLH1",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=INK,
        spaceBefore=18,
        spaceAfter=8,
        keepWithNext=True,
    )
    styles["h2"] = ParagraphStyle(
        "RFLH2",
        parent=base["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13.5,
        leading=17,
        textColor=INK,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True,
    )
    styles["body"] = ParagraphStyle(
        "RFLBody",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=13.2,
        textColor=INK,
        spaceAfter=7,
    )
    styles["bullet"] = ParagraphStyle(
        "RFLBullet",
        parent=styles["body"],
        leftIndent=17,
        firstLineIndent=-10,
        bulletIndent=4,
        spaceAfter=4,
    )
    styles["quote"] = ParagraphStyle(
        "RFLQuote",
        parent=styles["body"],
        leftIndent=16,
        rightIndent=16,
        borderColor=GOLD,
        borderWidth=1,
        borderPadding=8,
        backColor=SOFT,
        spaceBefore=6,
        spaceAfter=10,
    )
    styles["code"] = ParagraphStyle(
        "RFLCode",
        fontName="Courier",
        fontSize=7.6,
        leading=9.6,
        textColor=colors.HexColor("#1E1E1E"),
        backColor=colors.HexColor("#F3F3F3"),
        borderColor=LINE,
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=5,
        spaceAfter=10,
    )
    styles["small"] = ParagraphStyle(
        "RFLSmall",
        parent=styles["body"],
        fontSize=8,
        leading=10,
        textColor=MUTED,
    )
    styles["toc"] = ParagraphStyle(
        "RFLTOC",
        parent=styles["body"],
        leftIndent=10,
        firstLineIndent=-10,
        fontSize=8.7,
        leading=11,
    )
    styles["footer"] = ParagraphStyle(
        "RFLFooter",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=7,
        leading=8,
        textColor=MUTED,
        alignment=TA_CENTER,
    )
    return styles


def parse_blocks(markdown: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    paragraph_lines: list[str] = []
    code_lines: list[str] = []
    in_code = False

    def flush_para() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            blocks.append(("p", " ".join(line.strip() for line in paragraph_lines)))
            paragraph_lines = []

    def flush_code() -> None:
        nonlocal code_lines
        blocks.append(("code", "\n".join(code_lines)))
        code_lines = []

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_para()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_para()
            continue
        if line.startswith("# "):
            flush_para()
            blocks.append(("h1", line[2:].strip()))
        elif line.startswith("## "):
            flush_para()
            blocks.append(("h1", line[3:].strip()))
        elif line.startswith("### "):
            flush_para()
            blocks.append(("h2", line[4:].strip()))
        elif line.startswith("- "):
            flush_para()
            blocks.append(("bullet", line[2:].strip()))
        elif re.match(r"^\d+\. ", line):
            flush_para()
            blocks.append(("number", line.strip()))
        elif line.startswith("> "):
            flush_para()
            blocks.append(("quote", line[2:].strip()))
        else:
            paragraph_lines.append(line)
    flush_para()
    return blocks


def build_pdf(markdown_path: Path, output_path: Path) -> None:
    styles = make_styles()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = markdown_path.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    title = blocks[0][1] if blocks and blocks[0][0] == "h1" else "RFL Codex67 / SQ67 White Paper"
    headings = [value for kind, value in blocks if kind == "h1"][1:]

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.62 * inch,
        title=title,
        author="Renaissance Field Lite",
        subject="Codex67 / SQ67 public-safe Build Week white paper",
    )

    story = []
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph("RENAISSANCE FIELD LITE", styles["subtitle"]))
    story.append(Paragraph("Codex67 / SQ67", styles["title"]))
    story.append(Paragraph("Discovery, Proof, Showcase", styles["h1"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(
        paragraph(
            "Public-safe white paper for the Build Week receipt, recovery, and benchmark harness.",
            styles["subtitle"],
        )
    )
    meta = [
        ["Prepared by", "Renaissance Field Lite"],
        ["Primary operator", "Dean Patterson"],
        ["Codex node", "Rick / Codex 67"],
        ["Package date", "2026-07-17"],
        ["Repository commit", repo_commit()],
    ]
    table = Table(meta, colWidths=[1.5 * inch, 4.2 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                ("BOX", (0, 0), (-1, -1), 0.75, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("TEXTCOLOR", (0, 0), (-1, -1), INK),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(Spacer(1, 0.25 * inch))
    story.append(table)
    story.append(Spacer(1, 0.2 * inch))
    story.append(paragraph("No raw private state logs or private prompt dumps are included.", styles["small"]))
    story.append(PageBreak())

    story.append(Paragraph("Table of Contents", styles["h1"]))
    for item in headings[:40]:
        story.append(Paragraph(f"- {inline_markup(item)}", styles["toc"]))
    story.append(PageBreak())

    first_heading_seen = False
    for kind, value in blocks:
        if kind == "h1":
            if not first_heading_seen:
                first_heading_seen = True
                continue
            story.append(Paragraph(inline_markup(value), styles["h1"]))
        elif kind == "h2":
            story.append(Paragraph(inline_markup(value), styles["h2"]))
        elif kind == "bullet":
            story.append(Paragraph(inline_markup(value), styles["bullet"], bulletText="-"))
        elif kind == "number":
            story.append(paragraph(value, styles["body"]))
        elif kind == "quote":
            story.append(paragraph(value, styles["quote"]))
        elif kind == "code":
            story.append(Preformatted(value, styles["code"], maxLineLength=86))
        elif kind == "p":
            story.append(paragraph(value, styles["body"]))

    def draw_page(canvas, doc_obj) -> None:
        width, height = letter
        canvas.saveState()
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(1)
        canvas.line(doc_obj.leftMargin, height - 0.42 * inch, width - doc_obj.rightMargin, height - 0.42 * inch)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7)
        footer = f"Renaissance Field Lite / Codex67 SQ67 / page {doc_obj.page}"
        canvas.drawCentredString(width / 2, 0.35 * inch, footer)
        canvas.restoreState()

    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build_pdf(args.markdown, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

