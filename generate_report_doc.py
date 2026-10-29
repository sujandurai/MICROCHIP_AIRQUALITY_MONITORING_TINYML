from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# Page margins
section = doc.sections[0]
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3.0)
section.right_margin = Cm(2.5)

def set_cell_bg(cell, color_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tcPr.append(shd)

def add_heading(doc, text, level=1, color='1B3A6B'):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if level == 0 else WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.color.rgb = RGBColor.from_string(color)
    sizes = {0: 16, 1: 14, 2: 13, 3: 12}
    run.font.size = Pt(sizes.get(level, 12))
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    return p

def add_para(doc, text, bold=False, italic=False, size=12, indent=False, color=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.left_indent = Cm(0.5)
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    return p

# ===== TITLE PAGE =====
doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('S5 MINI PROJECT I')
run.bold = True
run.font.name = 'Times New Roman'
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(27, 58, 107)

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run('PROJECT REPORT GUIDELINES')
run2.bold = True
run2.font.name = 'Times New Roman'
run2.font.size = Pt(18)
run2.font.color.rgb = RGBColor(27, 58, 107)

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
run3 = p3.add_run('Complete Rules, Regulations & Submission Instructions')
run3.bold = False
run3.italic = True
run3.font.name = 'Times New Roman'
run3.font.size = Pt(14)
run3.font.color.rgb = RGBColor(80, 80, 80)

doc.add_paragraph()

p_line = doc.add_paragraph()
p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_line = p_line.add_run('=' * 60)
run_line.font.color.rgb = RGBColor(27, 58, 107)
run_line.font.size = Pt(10)

doc.add_paragraph()

p4 = doc.add_paragraph()
p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
run4 = p4.add_run('Hard Copy Submission Deadline: 22.10.2026 by 04:00 PM')
run4.bold = True
run4.font.name = 'Times New Roman'
run4.font.size = Pt(13)
run4.font.color.rgb = RGBColor(180, 30, 30)

doc.add_page_break()

# ===== SECTION 1: SUBMISSION INSTRUCTIONS =====
add_heading(doc, '1. SUBMISSION INSTRUCTIONS', level=1)

doc.add_paragraph()

add_heading(doc, '1.1 Soft Copy Submission', level=2)
items = [
    'Students must submit the soft copy of their project report to their respective project guides.',
    'Any corrections or suggestions provided by the guide must be incorporated promptly.',
]
for item in items:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    run = p.add_run(f'•  {item}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    p.paragraph_format.space_after = Pt(3)

add_heading(doc, '1.2 Hard Copy Submission', level=2)
items2 = [
    'After receiving final approval from the guide, students must prepare the hard copy of the project report.',
    'The completed and duly signed hard copy should be prepared on or before 22.10.2026 by 04:00 PM.',
    'Kindly submit the duly signed hard copy during the Semester End Viva Voce to the Examiners.',
]
for item in items2:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    run = p.add_run(f'•  {item}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    p.paragraph_format.space_after = Pt(3)

add_heading(doc, '1.3 Number of Copies', level=2)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.8)
run = p.add_run('•  Refer to the Guidelines for Number of Hard Copy Submission document for specific details regarding the number of copies to be submitted.')
run.font.name = 'Times New Roman'
run.font.size = Pt(12)

doc.add_paragraph()

# ===== SECTION 2: REPORT STRUCTURE =====
add_heading(doc, '2. REPORT STRUCTURE — TABLE OF CONTENTS', level=1)
doc.add_paragraph()

add_para(doc, 'The project report must follow the sequence of contents listed below:')

contents = [
    'Cover Page',
    'Inner Title Page (Same as cover page)',
    'Bonafide Certificate',
    'Bonafide Certificate from Industry (If applicable)',
    'Declaration',
    'Acknowledgement',
    'Abstract',
    'Table of Contents',
    'List of Tables',
    'List of Figures',
    'Abbreviations and Nomenclature (If any)',
    'Chapter 1 - Introduction',
    'Chapter 2 - Literature Survey',
    'Chapter 3 - Methodology (Research Design & Methods)',
    'Chapter 4 - Results & Discussion',
    'Chapter 5 - Conclusions & Suggestions for Future Work',
    'References',
    'Appendices (If any)',
    'Publication',
    'Publication Proof',
    'Plagiarism Report',
]
for i, item in enumerate(contents, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1)
    run = p.add_run(f'{i}.  {item}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)

doc.add_paragraph()
p_pg = doc.add_paragraph()
run_pg = p_pg.add_run('TOTAL REPORT LENGTH: Minimum 45 pages -- Maximum 75 pages')
run_pg.bold = True
run_pg.font.name = 'Times New Roman'
run_pg.font.size = Pt(12)
run_pg.font.color.rgb = RGBColor(180, 30, 30)

doc.add_page_break()

# ===== SECTION 3: CHAPTER-WISE GUIDELINES =====
add_heading(doc, '3. CHAPTER-WISE CONTENT GUIDELINES', level=1)
doc.add_paragraph()

chapters = [
    {
        'title': 'Chapter 1 - Introduction',
        'pages': 'Min 5 - Max 8 pages',
        'contents': [
            'Brief introduction about this chapter without section numbering.',
            '1.1 Background of the proposed work',
            '1.2 Motivation',
            '1.3 Problem Identification and Objectives',
            '1.4 Application areas',
            '1.5 Scope of the project',
            '1.6 Organization of the report (brief description of chapters that follow)',
            'Should summarize the contents of this chapter without section numbering.',
        ],
        'dos': [
            'Discuss the problem identification clearly.',
            'The scope and limitations must be stated clearly.',
        ],
        'donts': [
            'Do not include literature survey in this chapter.',
            "Don't give solutions in this chapter.",
        ],
        'citation': True,
    },
    {
        'title': 'Chapter 2 - Literature Survey',
        'pages': 'Min 10 - Max 15 pages',
        'contents': [
            'Brief introduction about the survey carried out without section numbering.',
            'Existing works for the proposed problem statement need to be explained with separate section numbering as and when required.',
            'Recent years literatures have to be used (preferably last five years).',
            'Constructive criticism and gap identification shall be written clearly.',
            'Should summarize the challenges and the details of the proposed solution without section numbering.',
            'Summary of gap identification and problem statement shall be clearly defined.',
        ],
        'dos': [],
        'donts': [
            "Don't include surveys without citations.",
            'Follow any one citation format throughout the entire report.',
            'The content of literature survey must be written in own words and should not be copied from the internet.',
        ],
        'citation': True,
    },
    {
        'title': 'Chapter 3 - Objectives and Methodology',
        'pages': 'Min 15 - Max 20 pages',
        'contents': [
            'Brief introduction about this chapter without section numbering.',
            '3.1. Objectives of the proposed work (Based on findings from Literature survey, objectives to be stated clearly)',
            '      Note: If 3 students are in a batch - minimum 3 objectives should be stated; individual contribution should be based on the objectives.',
            '3.2 Synthetic procedure / flow diagram of the proposed work (brief explanation of each block in flow diagram should be present)',
            '3.3. Describe the selection of components or tools / data collection / techniques / procedures / testing methods / standards',
            'Should summarize the contents of this chapter without section numbering.',
        ],
        'dos': ['Specific introduction related to methodology should be given.'],
        'donts': ['General introduction should be avoided.'],
        'citation': True,
    },
    {
        'title': 'Chapter 4 - Proposed Work Modules',
        'pages': '(Chapter name can be based on the work)',
        'contents': [
            'Brief introduction about this chapter without section numbering.',
            '4.1 / 5.1 / 6.1 ... Proposed work (Subheadings can be based on the work)',
            '4.2 / 5.2 / 6.2 ... Methodology of the proposed work (detailed explanation with methodology and findings)',
            'Should summarize the contents of this chapter without section numbering.',
        ],
        'dos': [],
        'donts': [],
        'citation': True,
    },
    {
        'title': 'Chapter 5 - Results and Discussion',
        'pages': 'Min 5 - Max 10 pages',
        'contents': [
            'Brief introduction about the findings without section numbering.',
            '7.1 Results',
            '    - Arrange the results (pictures, graphs, tables) as per the methodology followed.',
            '    - Discussion of important findings (results) in simple to complex order with numbering.',
            '    - Comparison of results with other related published works.',
            '7.2 Significance, Strengths and Limitations of the proposed work.',
            '7.3 Cost Benefit Analysis',
            'Should summarize the contents of this chapter without section numbering.',
        ],
        'dos': [
            'Represent the results clearly and precisely.',
            'Provide solid evidence and sufficient supporting arguments to reinforce your findings.',
        ],
        'donts': [
            'Do not misrepresent the results.',
            "Don't include anything that leads to any new conclusion about your work.",
            "Don't reveal any incomplete data.",
            "Don't make too many generalizations.",
        ],
        'citation': True,
    },
    {
        'title': 'Chapter 6 - Conclusions & Suggestions for Future Work',
        'pages': 'Min 1 - Max 2 pages',
        'contents': [
            'Brief introduction about the findings without section numbering.',
            '8.1 Conclusion (Consolidated report of the proposed work and its findings with statistics)',
            '8.2 Suggestions for Future Work (The possibility of extending the work in future, stating points not considered now that are essential for fine tuning the work)',
            'Should summarize the contents of this chapter without section numbering.',
        ],
        'dos': [
            'Honestly expose the factors which are not considered, however they can affect the results.',
        ],
        'donts': [
            "Don't repeat the sentences from Introduction.",
            "Don't give too many technical information here.",
            "Don't state the finding with high degree of confirmation.",
        ],
        'citation': False,
    },
]

citation_note = "Citation Format Inside Contents:\n  1 author:   Bedford, 2017\n  2 authors:  Bedford & Caulfield, 2012\n  3+ authors: Davis et al., 2015"

for ch in chapters:
    add_heading(doc, ch['title'], level=2)

    p_pg2 = doc.add_paragraph()
    run_pg2 = p_pg2.add_run(f"Page Count: {ch['pages']}")
    run_pg2.bold = True
    run_pg2.italic = True
    run_pg2.font.name = 'Times New Roman'
    run_pg2.font.size = Pt(11)
    run_pg2.font.color.rgb = RGBColor(27, 58, 107)

    add_heading(doc, 'Contents to Include:', level=3)
    for line in ch['contents']:
        if line:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            run = p.add_run(line)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)

    if ch['dos']:
        add_heading(doc, "Do's:", level=3, color='006400')
        for d in ch['dos']:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            run = p.add_run(f'[YES]  {d}')
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(0, 100, 0)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)

    if ch['donts']:
        add_heading(doc, "Don'ts:", level=3, color='8B0000')
        for d in ch['donts']:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            run = p.add_run(f'[NO]  {d}')
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(139, 0, 0)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)

    if ch['citation']:
        p_cit = doc.add_paragraph()
        p_cit.paragraph_format.left_indent = Cm(0.8)
        run_cit = p_cit.add_run(citation_note)
        run_cit.italic = True
        run_cit.font.name = 'Times New Roman'
        run_cit.font.size = Pt(11)
        run_cit.font.color.rgb = RGBColor(70, 70, 130)

    doc.add_paragraph()

doc.add_page_break()

# ===== SECTION 4: REFERENCES =====
add_heading(doc, '4. REFERENCES GUIDELINES', level=1)
doc.add_paragraph()

add_para(doc, 'Page Count: Minimum 2 - Maximum 4 pages', bold=True)
doc.add_paragraph()

ref_rules = [
    'Number all the references.',
    'Use a chronological bibliography.',
    'Each listed reference in the bibliography must be cited in the text of the report.',
    'For a book: give the name(s) of author(s), title of book, edition, chapter number, page numbers, publisher, location and year of publication.',
    'Every report should have a maximum of 15-20 references.',
    'APA format is the preferable format for references.',
    'Include more Journal, book and conference references rather than website link references.',
]
add_heading(doc, 'Rules:', level=2)
for i, rule in enumerate(ref_rules, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1)
    run = p.add_run(f'{i}.  {rule}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)

doc.add_paragraph()
add_heading(doc, 'APA Reference Structure:', level=2)
add_para(doc, 'Author Last name, First initial. Middle initial. (Year Published). Title of article. Title of Periodical, Volume(Issue), page range. https://doi.org/xxxx or URL', italic=True, indent=True)

doc.add_paragraph()
add_heading(doc, 'Example:', level=3)
add_para(doc, "[1] Burnell, K. J., Coleman, P. G., & Hunt, N. (2010). Coping with traumatic memories: Second World War veterans' experiences of social support in relation to the narrative coherence of war memories. Ageing and Society, 30(1), 57-78. https://doi.org/10.1017/S0144686X0999016X", italic=True, indent=True, size=11)

doc.add_paragraph()
add_heading(doc, "Don't:", level=3, color='8B0000')
add_para(doc, "[NO]  Don't include references which are not used in any chapter of your report.", indent=True, color='8B0000')

doc.add_page_break()

# ===== SECTION 5: APPENDICES =====
add_heading(doc, '5. APPENDICES', level=1)
doc.add_paragraph()

appendices = [
    ('I', 'Bill of Materials'),
    ('II', 'Coding (If applicable)'),
    ('III', 'Standard tables/graphs that are not mentioned in the report'),
    ('IV', 'Publication Certificate\n(Note: Online Conference Presentation Certificate Proofs will NOT be accepted)'),
    ('V', 'Publication Proof (First page of Journal publication / Conference publication)'),
    ('VI', 'Work Contribution'),
    ('VII', 'Plagiarism Report\n(Note: Student name and title of the project should be present in the plagiarism report)'),
]

table = doc.add_table(rows=1, cols=2)
table.style = 'Table Grid'
table.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr_cells = table.rows[0].cells
for i, hdr in enumerate(['Appendix No.', 'Content']):
    set_cell_bg(hdr_cells[i], '1B3A6B')
    p = hdr_cells[i].paragraphs[0]
    run = p.add_run(hdr)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

for i, (num, content) in enumerate(appendices):
    row_cells = table.add_row().cells
    bg = 'EEF2F7' if i % 2 == 0 else 'FFFFFF'
    set_cell_bg(row_cells[0], bg)
    set_cell_bg(row_cells[1], bg)

    p0 = row_cells[0].paragraphs[0]
    r0 = p0.add_run(num)
    r0.bold = True
    r0.font.name = 'Times New Roman'
    r0.font.size = Pt(12)
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p1 = row_cells[1].paragraphs[0]
    r1 = p1.add_run(content)
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)

doc.add_paragraph()
doc.add_page_break()

# ===== SECTION 6: TYPING & FORMATTING =====
add_heading(doc, '6. TYPING & FORMATTING INSTRUCTIONS', level=1)
doc.add_paragraph()

fmt_rules = [
    ('Font Style', 'Times New Roman'),
    ('Font Size (General Text)', '13 pt'),
    ('Heading - Chapter Title', 'Times New Roman, 14 pt, CAPITAL LETTERS, Bold, Centre aligned'),
    ('Heading - Subheading (e.g., 1.1)', 'Times New Roman, 14 pt, CAPITAL LETTERS, Bold, Left aligned'),
    ('Heading - Sub-subheading (e.g., 1.1.1)', 'Times New Roman, 14 pt, Bold, Left aligned, Sentence Case'),
    ('Line Spacing', '1.5 (One and a half spacing)'),
    ('Paragraph Alignment', 'Justify'),
    ('Figure Reference', 'All Figure Nos. must be cited within the report text'),
    ('Table Reference', 'All Table Nos. must be cited within the report text'),
    ('Internet Images', 'Avoid images from the internet. If necessary, place only in Chapter 1 or 2'),
    ('Redundant Pictures', 'Avoid including redundant or unnecessary pictures'),
]

table2 = doc.add_table(rows=1, cols=2)
table2.style = 'Table Grid'
table2.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr2 = table2.rows[0].cells
for i, hdr in enumerate(['Parameter', 'Specification']):
    set_cell_bg(hdr2[i], '1B3A6B')
    p = hdr2[i].paragraphs[0]
    run = p.add_run(hdr)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

for i, (param, spec) in enumerate(fmt_rules):
    row_cells = table2.add_row().cells
    bg = 'EEF2F7' if i % 2 == 0 else 'FFFFFF'
    set_cell_bg(row_cells[0], bg)
    set_cell_bg(row_cells[1], bg)

    p0 = row_cells[0].paragraphs[0]
    r0 = p0.add_run(param)
    r0.bold = True
    r0.font.name = 'Times New Roman'
    r0.font.size = Pt(12)

    p1 = row_cells[1].paragraphs[0]
    r1 = p1.add_run(spec)
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)

doc.add_paragraph()
doc.add_page_break()

# ===== SECTION 7: SAMPLE TABLE OF CONTENTS =====
add_heading(doc, '7. SAMPLE TABLE OF CONTENTS (Reference)', level=1)
doc.add_paragraph()

add_para(doc, 'Below is a sample Table of Contents structure extracted from the reference document:', italic=True)
doc.add_paragraph()

toc_entries = [
    ('', 'ACKNOWLEDGEMENT', ''),
    ('', 'ABSTRACT', '1'),
    ('', 'TABLE OF CONTENTS', '2'),
    ('', 'LIST OF FIGURES', '3'),
    ('1', 'INTRODUCTION', '5'),
    ('1.1', 'OBJECTIVE', '8'),
    ('1.2', 'PROBLEM IDENTIFICATION', '8'),
    ('1.3', 'OUTCOME', '8'),
    ('2', 'LITERATURE SURVEY', '9'),
    ('3', 'METHODOLOGY', '12'),
    ('3.1', 'ALGORITHM', '12'),
    ('3.2', 'PROPOSED METHODOLOGY', '13'),
    ('3.3', 'NOZZLE GEOMETRY', '13'),
    ('3.4', 'MODELLING AND SETUP', '14'),
    ('3.4.1', 'DOMAIN CREATION', '14'),
    ('3.4.2', 'MESHING', '15'),
    ('3.4.3', 'GRID INDEPENDENCE STUDY', '16'),
    ('3.4.4', 'INFLATION LAYER', '23'),
    ('3.4.5', 'SOLVER SETUP', '23'),
    ('3.4.6', 'POST-PROCESSING', '25'),
    ('4', 'RESULTS AND DISCUSSION', '26'),
    ('4.1', 'COMPARISON OF TWO NOZZLE DESIGNS', '26'),
    ('5', 'CONCLUSION', '31'),
    ('6', 'REFERENCES', '32'),
    ('7', 'INDIVIDUAL CONTRIBUTION', '33'),
    ('8', 'ORIGINALITY SCORE', '34'),
    ('9', 'PUBLICATION PROOF', '35'),
]

table3 = doc.add_table(rows=1, cols=3)
table3.style = 'Table Grid'
table3.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr3 = table3.rows[0].cells
for i, hdr in enumerate(['Chapter No.', 'Title', 'Page No.']):
    set_cell_bg(hdr3[i], '2C5282')
    p = hdr3[i].paragraphs[0]
    run = p.add_run(hdr)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

for i, (num, title, pg) in enumerate(toc_entries):
    row_cells = table3.add_row().cells
    bg = 'EEF2F7' if i % 2 == 0 else 'FFFFFF'
    is_main = len(num) <= 1
    for j, (c, val) in enumerate([(row_cells[0], num), (row_cells[1], title), (row_cells[2], pg)]):
        set_cell_bg(c, bg)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.bold = is_main
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12 if is_main else 11)
        if j == 0 or j == 2:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()
doc.add_page_break()

# ===== SECTION 8: GENERAL CHECKLIST =====
add_heading(doc, '8. GENERAL CHECKLIST BEFORE SUBMISSION', level=1)
doc.add_paragraph()

checklist = [
    'Report follows the required sequence of contents (Cover Page to Plagiarism Report).',
    'Total page count is within the range of 45-75 pages.',
    'Font: Times New Roman, 13 pt, 1.5 line spacing, Justify alignment throughout.',
    'All chapter and subheading titles are formatted correctly (size, case, alignment).',
    'All figures and tables are numbered and cited within the text.',
    'No redundant or internet-sourced images included unnecessarily.',
    'Literature survey contains only cited surveys (min. last 5 years preferred).',
    'References are in APA format, numbered 1-20 max (15-20 references).',
    'Plagiarism report includes student name and project title.',
    'Publication Certificate is physical (online conference certificate proofs NOT accepted).',
    'Work Contribution section (Appendix VI) is included.',
    'Bill of Materials (Appendix I) is included.',
    'Individual contribution for each batch member is clearly stated under objectives.',
    'Bonafide Certificate is signed by the guide.',
    'Declaration is signed by student(s).',
    'Hard copy is duly signed and submitted on or before 22.10.2026 by 04:00 PM.',
]

for item in checklist:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    run = p.add_run(f'[ ]  {item}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)

doc.add_paragraph()

# Footer note
p_foot = doc.add_paragraph()
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_foot = p_foot.add_run('--- End of Guidelines Document ---')
run_foot.bold = True
run_foot.italic = True
run_foot.font.name = 'Times New Roman'
run_foot.font.size = Pt(12)
run_foot.font.color.rgb = RGBColor(27, 58, 107)

# Save
out_path = r'C:\FullyCompleted\S5_MiniProject_Report_Guidelines.docx'
doc.save(out_path)
print(f'Document saved successfully: {out_path}')
