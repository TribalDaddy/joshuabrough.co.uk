from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parent
styles = getSampleStyleSheet()
for name, size, leading, color in [('TitleJB',30,36,'#101b29'),('SubtitleJB',10,15,'#53606a'),('SectionJB',12,17,'#8b713f'),('RoleJB',10.5,15,'#101b29'),('BodyJB',9.3,13.7,'#35424d'),('MetaJB',8.5,12,'#53606a')]:
    styles.add(ParagraphStyle(name, fontName='Helvetica',fontSize=size,leading=leading,textColor=HexColor(color),spaceAfter=7))
story=[]
def p(text,style='BodyJB'): story.append(Paragraph(text,styles[style]))
def section(text): story.append(Spacer(1,10));p(text.upper(),'SectionJB')
def entry(title,meta,body):
    story.append(KeepTogether([Paragraph(title,styles['RoleJB']),Paragraph(meta,styles['MetaJB']),Paragraph(body,styles['BodyJB']),Spacer(1,8)]))
p('JOSHUA BROUGH','TitleJB')
p('<link href="mailto:Joshuabrough1@outlook.com">Joshuabrough1@outlook.com</link>  |  <link href="https://www.linkedin.com/in/joshua-brough">linkedin.com/in/joshua-brough</link>','MetaJB')
p('Aspiring finance professional with a strong analytical foundation and hands-on industry experience. PPE graduate from Lancaster University, starting an MSc in Accounting and Finance at LSE in September 2026. Interested in how people, markets and organisations make decisions.','SubtitleJB')
section('Education')
entry('<b>London School of Economics</b> | MSc Accounting and Finance','London, UK | September 2026 - June 2027 | Starting September 2026','Forthcoming postgraduate study in accounting and finance.')
entry('<b>Lancaster University</b> | BA (Hons) Philosophy, Politics and Economics, 2:1','Lancaster, UK | October 2023 - June 2026','Equity Analyst, Sell Side Institute (Finance &amp; Investment Society). Accounting Society and Tennis Society member. Morgan Stanley x AmplifyME trading simulation.')
entry('<b>Tanglin Trust School</b> | A-levels','Singapore | August 2021 - June 2023','Economics (A), Mathematics (C), Politics (B). Extended Project Qualification (A*).')
section('Industry experience')
entry('<b>North Standard</b> | Industry placement','Dublin, Ireland | September 2026','Gained exposure to a specialist insurance organisation, developing an understanding of liability protection and how shared financial structures support clients facing complex risks.')
entry('<b>Tigermar Insurance Brokers</b> | Industry placement','London, UK | July - August 2026','Observed the journey from client requirements through documentation to securing appropriate cover. Gained insight into client communication, professional relationships and specialist financial markets.')
entry('<b>QBE Insurance</b> | Market insight and professional shadowing','London, UK | July 2026','Shadowed a senior risk specialist, observing live risk assessment and commercial negotiation. Developed an appreciation of how geopolitical disruption informs decisions in a regulated financial environment.')
story.append(PageBreak())
p('JOSHUA BROUGH','RoleJB')
section('Industry experience continued')
entry('<b>Ocean Special Risks</b> | Industry placement and professional shadowing','London, UK | July 2026','Shadowed a senior specialist, gaining insight into complex risk evaluation, pricing decisions and portfolio management, and how individual decisions fit within a wider commercial picture.')
entry('<b>Food Bank Aid</b> | Business Strategy Intern','London, UK | August - September 2024','Collaborated directly with the CEO on operational strategy, analysed expenditure allocation and evaluated more than 20 suppliers through structured market research.')
section('Skills')
for text in ['<b>Quantitative analysis:</b> Data analysis, expenditure evaluation and structured research, supported by Economics and Mathematics.', '<b>Financial understanding:</b> Excel, financial modelling and foundational financial statement literacy, supported by equity analysis and financial learning.', '<b>Commercial awareness:</b> Understanding client requirements, risk and pricing in their wider business context.', '<b>Strategic reasoning:</b> Analysing incentives and competing perspectives through PPE, game theory and chess.', '<b>Relationships and communication:</b> Working with senior colleagues, observing client relationships and adapting communication across cultures.', '<b>Research and presentation:</b> Market research, PowerPoint and data visualisation.']:
    p(text)
section('Professional development')
p('<b>Yale University</b> - Financial Markets<br/><b>Duke University</b> - Behavioural Finance<br/><b>Goldman Sachs Skills for Business</b> - Excel, Financial Modelling and Data Visualisation')
section('Interests and community')
p('<b>Intellectual interests:</b> Military history, geopolitics, game theory and chess.<br/><b>Sport:</b> Football, rugby, tennis and running.')
p('<b>ItsRainingRaincoats</b> | Singapore, 2021<br/>Taught English to a Bangladeshi worker, adapting lessons despite having no shared language. Additional volunteering with the iNaturalist endangered species programme and a cat sanctuary.')
p('<b>Languages:</b> English (native); French (limited proficiency).')
def footer(c,doc):
    c.setFont('Helvetica',8);c.setFillColor(HexColor('#53606a'));c.drawString(44,27,'Joshua Brough | Curriculum vitae');c.drawRightString(A4[0]-44,27,str(doc.page))
SimpleDocTemplate(str(ROOT/'dist/Joshua-Brough-CV.pdf'),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=38,bottomMargin=44,title='Joshua Brough - Curriculum Vitae',author='Joshua Brough').build(story,onFirstPage=footer,onLaterPages=footer)
