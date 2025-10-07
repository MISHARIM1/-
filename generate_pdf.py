"""Generate the Sara Song Studio sheet as a PDF document.

This script uses ReportLab to produce a formatted PDF file that captures the
lyrics, arrangement notes, and performance directions for the song "Sara".
"""

from pathlib import Path

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def build_sara_song_sheet(output_path: Path) -> None:
    """Create the Sara song performance sheet as a PDF at ``output_path``."""
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CenterTitle",
            alignment=TA_CENTER,
            fontSize=16,
            spaceAfter=20,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubHeading",
            fontSize=12,
            spaceAfter=10,
            textColor="gray",
        )
    )
    styles.add(ParagraphStyle(name="Body", fontSize=11, leading=18))

    content = []

    content.append(Paragraph("🎵 الأغنية: سـارا", styles["CenterTitle"]))
    content.append(
        Paragraph(
            "المقام: بيات على ري (D) — الإيقاع: 4/4 خليجي بطيء – 74 BPM — المدة: تقريبًا 4:45 دقيقة",
            styles["SubHeading"],
        )
    )

    sections = [
        (
            "المقدمة الموسيقية (00:00 – 00:25)",
            "عود منفرد على نغمة D–F–G–A (جملتين). دخول الكمنجة بعد 10 ثوانٍ. دف خفيف قبل الكوبليه. أداء هادئ بنفس عميق.",
        ),
        (
            "الكوبليه الأول (00:26 – 01:20)",
            "يا سـارا، يا أغلى إنسانه بعمري، والله إنك شي ثمين<br/>من يوم ضعت وأنا صغير، وانتي الحنان والسكينه<br/>مدّيتي يدك، وانتِ ما قلتي ثمين ولا رهين<br/>رجّعتيني لأهلي بطيبك، وانتي عيونٍ أمينه<br/><br/><b>التعليمات:</b> أداء ناعم، بدون كورال. الآلات: عود + كمنجة خفيفة.",
        ),
        (
            "القرار الأول (01:21 – 02:00)",
            "سـارا، إنتِ اللي علّمتيني وش معنى الحياه<br/>وانتي سبب كل الفرح بعد العناه<br/>كل ما طحت، كنتي دايم معاي<br/>يا سـارا، يا ظلّي ودفاي<br/><br/><b>التعليمات:</b> رفع إحساس، دخول كمنجات وبيانو.",
        ),
        (
            "الكوبليه الثاني (02:01 – 02:45)",
            "حتى وأنا مسجون، كنتي لي الوطن والبيت<br/>دخلتي السجن بين العسكر، ولا خفتي العيب<br/>يا سـارا، يا نبض قلبي، يا أصدق إحساس<br/>وجودك يكفيني عن الدنيا، وعن كل الناس<br/><br/><b>التعليمات:</b> أداء دافئ بشجن، خفف السرعة آخر سطر.",
        ),
        (
            "القرار الثاني (02:46 – 03:25)",
            "سـارا، إنتِ اللي علّمتيني وش معنى الحياه<br/>وانتي سبب كل الفرح بعد العناه<br/>كل ما طحت، كنتي دايم معاي<br/>يا سـارا، يا ظلّي ودفاي<br/><br/><b>التعليمات:</b> أداء قوي عاطفي، ارتفاع نصف درجة. دخول كامل للآلات.",
        ),
        (
            "الخاتمة (03:26 – 04:45)",
            "يا سـارا، يا حبٍ ما انتهى<br/>تبقين نبضي، وذكري ودعاي<br/>لو يسألون الحب، أقولها بصدق<br/>سـارا هي اللي علّمتني أعيش الحياة<br/><br/><b>التعليمات:</b> تهدئة تدريجية، خروج الآلات واحدة تلو الأخرى. آخر كلمة (الحياة) تُمد ويُترك صدى طويل.",
        ),
    ]

    for title, text in sections:
        content.append(Paragraph(f"<b>{title}</b>", styles["SubHeading"]))
        content.append(Paragraph(text, styles["Body"]))
        content.append(Spacer(1, 12))

    doc.build(content)


if __name__ == "__main__":
    build_sara_song_sheet(Path("Sara_Song_Studio_Sheet.pdf"))
