from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# below imports our 3 objects existing in our database 'catalog.db':
from database_setup import Base, CategoryDBClass, ItemDBClass

engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Items for Category1:
category1 = CategoryDBClass(name="History and Etymology")
session.add(category1)
session.commit()
session.close()

Item1 = ItemDBClass(
    item_pin="12345", name="History of accounting",
    description='''The history of accounting is thousands of years \
    old and can \
    be traced to ancient civilizations. The early development of \
    accounting dates back to ancient Mesopotamia, and is closely \
    related to developments in writing, counting and money; there \
    is also evidence for early forms of bookkeeping in ancient \
    Iran, and early auditing systems by the ancient Egyptians \
    and Babylonians. By the time of the Emperor Augustus, the \
    Roman government had access to detailed financial information.

    Double-entry bookkeeping was pioneered in the Jewish community \
    of the early-medieval Middle East and further refined in \
    medieval Europe. With the development of joint-stock \
    companies, accounting split into financial accounting and \
    management accounting.

    The first work on a double-entry bookkeeping system was \
    published in Italy, by Luca Pacioli (Father of Accounting). \
    Accounting began to transition into an organized profession \
    in the nineteenth century, with local professional \
    bodies in England merging to form the Institute of Chartered \
    Accountants in England and Wales in 1880. ''',
    category_name=category1
    )
session.add(Item1)
session.commit()
session.close()

Item2 = ItemDBClass(
    item_pin="12345", name="Etymology",
    description='''Both the words accounting and accountancy were in use in \
    Great Britain by the mid-1800s, and are derived from the words accompting \
    and accountantship used in the 18th century. In Middle English \
    (used roughly between the 12th and the late 15th century) the verb \
    'to account' had the form accounten, which was derived from the Old \
    French word aconter, which is in turn related to the Vulgar Latin word \
    computare, meaning 'to reckon'. The base of computare is putare, which \
    'variously meant to prune, to purify, to correct an account, hence, to \
    count or calculate, as well as to think.' The word accountant is derived \
    from the French word compter, which is also derived from the Italian and \
    Latin word computare. The word was formerly written in English as \
    'accomptant', but in process of time the word, which was always \
    pronounced by dropping the 'p', became gradually changed both in \
    pronunciation and in orthography to its present form. ''',
    category_name=category1
    )
session.add(Item2)
session.commit()
session.close()

Item3 = ItemDBClass(
    item_pin="12345", name="Accounting and Accountancy",
    description='''Accounting has variously been defined as the keeping or \
    preparation of the financial records of an entity, the analysis, \
    verification and reporting of such records and 'the principles and \
    procedures of accounting'; it also refers to the job of being an \
    accountant. Accountancy refers to the occupation or profession of an \
    accountant, particularly in British English. ''', category_name=category1
    )
session.add(Item3)
session.commit()
session.close()


# Items for Category2:
category2 = CategoryDBClass(name="Topics")
session.add(category2)
session.commit()
session.close()


Item1 = ItemDBClass(
    item_pin="12345", name="Financial Accounting",
    description='''Financial accounting focuses on the reporting of an \
    organization's financial information to external users of the information,\
    such as investors, potential investors and creditors. It calculates and \
    records business transactions and prepares financial statements for the \
    external users in accordance with generally accepted accounting principles\
    (GAAP). GAAP, in turn, arises from the wide agreement between accounting \
    theory and practice, and change over time to meet the needs of \
    decision-makers. Financial accounting produces past-oriented reports -for \
    example the financial statements prepared in 2006 reports on performance \
    in 2005-on an annual or quarterly basis, generally about the organization \
    as a whole. This branch of accounting is also studied as part of the \
    board exams for qualifying as an actuary. These two types of \
    professionals, accountants and actuaries, have created a culture of \
    being archrivals. ''', category_name=category2
    )
session.add(Item1)
session.commit()
session.close()

Item2 = ItemDBClass(
    item_pin="12345", name="Management Accounting",
    description='''Management accounting focuses on the measurement, analysis \
    and reporting of information that can help managers in making decisions \
    to fulfill the goals of an organization. In management accounting, \
    internal measures and reports are based on cost-benefit analysis, and \
    are not required to follow the generally accepted accounting principle \
    (GAAP). In 2014 CIMA created the Global Management Accounting Principles \
    (GMAPs). The result of research from across 20 countries in five \
    continents, the principles aim to guide best practice in the discipline. \
    Management accounting produces future-oriented reports - for example the \
    budget for 2006 is prepared in 2005 - and the time span of reports varies \
    widely. Such reports may include both financial and non financial \
    information, and may, for example, focus on specific products and \
    departments.''', category_name=category2
    )
session.add(Item2)
session.commit()
session.close()

Item3 = ItemDBClass(
    item_pin="12345", name="Auditing",
    description='''Auditing is the verification of assertions made by others \
    regarding a payoff, and in the context of accounting it is the 'unbiased \
    examination and evaluation of the financial statements of an \
    organization'. Audit is a professional service that is systematic and \
    conventional. An audit of financial statements aims to express or \
    disclaim an opinion on the financial statements. The auditor expresses \
    an opinion on the fairness with expression as target: pass which the \
    financial statements presents the financial position, results \
    of operations, and cash flows of an entity, in accordance with the \
    generally acceptable accounting principle (GAAP) and 'in all material \
    respects'. An auditor is also required to identify circumstances in \
    which the generally acceptable accounting principles (GAAP) has not \
    been consistently observed. ''', category_name=category2
    )
session.add(Item3)
session.commit()
session.close()

Item4 = ItemDBClass(
    item_pin="12345", name="Accounting Information Systems",
    description='''An accounting information system is a part of an \
    organization's information system that focuses on processing accounting \
    data. Many corporations use artificial intelligence-based information \
    systems. Banking and finance industry is using AI as fraud detection. \
    Retail industry is using AI for customer services. AI is also used in \
    cybersecurity industry. It involves computer hardware and software \
    systems and using statistics and modeling. ''', category_name=category2
    )
session.add(Item4)
session.commit()
session.close()

Item5 = ItemDBClass(
    item_pin="12345", name="Tax Accounting",
    description='''Tax accounting in the United States concentrates on the \
    preparation, analysis and presentation of tax payments and tax returns. \
    The U.S. tax system requires the use of specialised accounting \
    principles for tax purposes which can differ from the generally \
    accepted accounting principles (GAAP) for financial reporting. U.S. \
    tax law covers four basic forms of business ownership: sole \
    proprietorship, partnership, corporation, \
    and limited liability company. Corporate and personal income are taxed at \
    different rates, both varying according to income levels and including \
    varying marginal rates (taxed on each additional dollar of income) and \
    average rates (set as a percentage of overall income).''',
    category_name=category2
    )
session.add(Item5)
session.commit()
session.close()


# Items for Category3:
category3 = CategoryDBClass(name="Organizations")
session.add(category3)
session.commit()
session.close()


Item1 = ItemDBClass(
    item_pin="12345", name="Professional bodies",
    description='''Professional accounting bodies include the American \
    Institute of Certified Public Accountants (AICPA) and the other 179 \
    members of the International Federation of Accountants (IFAC), including \
    CPA Australia, Association of Chartered Certified Accountants (ACCA) \
    and Institute of Chartered Accountants in England and Wales (ICAEW). \
    Professional bodies for subfields of the accounting professions also \
    exist, for example the Chartered Institute of Management Accountants \
    (CIMA). Many of these professional bodies offer education and training \
    including qualification and administration for \
    various accounting designations, such as certified public accountant and \
    chartered accountant. ''', category_name=category3
    )
session.add(Item1)
session.commit()
session.close()

Item2 = ItemDBClass(
    item_pin="12345", name="Accounting firms",
    description='''Depending on its size, a company may be legally required \
    to have their financial statements audited by a qualified auditor, and \
    audits are usually carried out by accounting firms. Accounting firms \
    grew in the United States and Europe in the late nineteenth and early \
    twentieth century, and through several mergers there were large \
    international accounting firms by the mid-twentieth century. Further \
    large mergers in the late twentieth century led to the dominance of the \
    auditing market by the 'Big Five' accounting\
    firms: Arthur Andersen, Deloitte, Ernst and Young, KPMG and \
    PricewaterhouseCoopers. The demise of Arthur Andersen following the Enron \
    scandal reduced the Big Five to the Big Four. ''',
    category_name=category3
    )
session.add(Item2)
session.commit()
session.close()

Item3 = ItemDBClass(
    item_pin="12345", name="Standard-setters",
    description='''Generally accepted accounting principles (GAAP) are \
    accounting standards issued by national regulatory bodies. In addition, \
    the International Accounting Standards Board (IASB) issues the \
    International Financial Reporting Standards (IFRS) implemented by 147 \
    countries. While standards for international audit and assurance, ethics, \
    education, and public sector accounting are all set by independent \
    standard settings boards supported by IFAC. The International Auditing \
    and Assurance Standards Board sets international standards for \
    auditing, assurance, and quality control; \
    the International Ethics Standards Board for Accountants (IESBA) sets the \
    internationally appropriate principles- based Code of Ethics for \
    Professional Accounts the International Accounting Education Standards \
    Board (IAESB) sets professional accounting education standards; \
    International Public Sector Accounting Standards Board (IPSASB) sets \
    accrual-based international public sector accounting standards \
    Organizations in individual countries may issue accounting standards \
    unique to the countries. For example, in the United States the \
    Financial Accounting Standards Board (FASB) issues the Statements \
    of Financial Accounting Standards, which form the basis of US GAAP, \
    and in the United Kingdom the Financial Reporting Council (FRC) sets \
    accounting standards. However, as of 2012 'all major economies' have \
    plans to converge towards or adopt the IFRS.''', category_name=category3
    )
session.add(Item3)
session.commit()
session.close()


# Items for Category4:
category4 = CategoryDBClass(name="Education and qualifications")
session.add(category4)
session.commit()
session.close()


Item1 = ItemDBClass(
    item_pin="12345", name="Accounting degrees",
    description='''At least a bachelor's degree in accounting or a related \
    field is required for most accountant and auditor job positions, and \
    some employers prefer applicants with a master's degree. A degree in \
    accounting may also be equired for, or may be used to fulfill the \
    requirements for, membership to professional accounting bodies. \
    For example, the education during an \
    accounting degree can be used to fulfill the American Institute of CPA's \
    (AICPA) 150 semester hour requirement, and associate membership with the \
    Certified Public Accountants Association of the UK is available after \
    gaining a degree in finance or accounting. A doctorate is required \
    in order to pursue a career in accounting academia, for example to work \
    as a university professor in accounting. The Doctor of Philosophy (PhD) \
    and the Doctor of Business Administration (DBA) are the most popular \
    degrees. The PhD is the most common degree for those wishing to pursue \
    a career in academia, while DBA programs generally focus on equipping \
    business executives for business or public careers requiring research \
    skills and qualifications. ''', category_name=category4
    )
session.add(Item1)
session.commit()
session.close()

Item2 = ItemDBClass(
    item_pin="12345", name="Professional qualifications",
    description='''Professional accounting qualifications include the \
    Chartered Accountant designations and other qualifications including \
    certificates and diplomas. In the United Kingdom, chartered accountants \
    of the ICAEW undergo annual training, and are bound by the ICAEW's code \
    of ethics and subject to its disciplinary procedures. In the United \
    States, the requirements for joining the AICPA as a Certified Public \
    Accountant are set by the Board of Accountancy of each state, and \
    members agree to abide by the AICPA's Code of Professional Conduct and \
    Bylaws. In India the Apex Accounting body constituted by parliament \
    of India is 'Institute of Chartered Accountants of India' \
    (ICAI) was known for its rigorous training and study methodology \
    for granting the Qualification. The ACCA is the largest global \
    accountancy body with over 320,000 members and the organisation \
    provides an -IFRS stream- and a -UK stream-. Students must pass a \
    total of 14 exams, which are arranged across three papers. ''',
    category_name=category4
    )
session.add(Item2)
session.commit()
session.close()


# Items for Category5:
category5 = CategoryDBClass(name="Other")
session.add(category5)
session.commit()
session.close()


Item1 = ItemDBClass(
    item_pin="12345", name="Accounting research",
    description='''Accounting research is research in the effects of economic \
    events on the process of accounting, and the effects of reported \
    information on economic events. It encompasses a broad range of research \
    areas including financial accounting, management accounting, auditing \
    and taxation. Accounting research is carried out both by academic \
    researchers and practicing accountants. Methodologies in academic \
    accounting research can be classified into archival research, which \
    examines 'objective data collected from repositories'; experimental \
    research, which examines data 'the researcher gathered by administering \
    treatments to subjects'; and analytical research, which is 'based on \
    the act of formally modeling theories or substantiating \
    ideas in mathematical terms'. This classification is not exhaustive;other \
    possible methodologies include the use of case studies, computer \
    simulations and field research. Empirical studies document that \
    leading accounting journals publish in total fewer research articles \
    than comparable journals in economics and other business disciplines, \
    and consequently, accounting scholars are relatively less successful in \
    academic publishing than their business school peers. Due to different \
    publication rates between accounting and other business disciplines, \
    a recent study based on academic author rankings concludes that the \
    competitive value of a single publication in a top-ranked journal is \
    highest in accounting and lowest in marketing. ''',
    category_name=category5
    )
session.add(Item1)
session.commit()
session.close()

Item2 = ItemDBClass(
    item_pin="12345", name="Accounting information system",
    description='''Many accounting practices have been simplified with the \
    help of accounting computer-based software. An Enterprise resource \
    planning (ERP) system is commonly used for a large organisation and \
    it provides a comprehensive, centralized, integrated source of \
    information that companies can use to manage all major business \
    processes, from purchasing to manufacturing to human resources. \
    Accounting information systems have reduced the cost of accumulating, \
    storing, and reporting managerial accounting information and have made \
    it possible to produce a more detailed account of all data that is \
    entered into any given system. ''', category_name=category5
    )
session.add(Item2)
session.commit()
session.close()

Item3 = ItemDBClass(
    item_pin="12345", name="Accounting scandals",
    description='''The year 2001 witnessed a series of financial information \
    frauds involving Enron, auditing firm Arthur Andersen, the \
    telecommunications company WorldCom, Qwest and Sunbeam, among other \
    well-known corporations. These problems highlighted the need to review \
    the effectiveness of accounting standards, auditing regulations and \
    corporate governance principles. In some cases, management manipulated \
    the figures shown in financial reports to indicate a better economic \
    performance. In others, tax and regulatory incentives encouraged \
    over-leveraging of companies and decisions to bear extraordinary and \
    unjustified risk. The Enron scandal deeply influenced the \
    development of new regulations to improve the reliability of financial \
    reporting, and increased public awareness about the importance of having \
    accounting standards that show the financial reality of companies and the \
    objectivity and independence of auditing firms. In addition to being the \
    largest bankruptcy reorganization in American history, the Enron scandal \
    undoubtedly is the biggest audit failure. It involved a financial \
    scandal of Enron Corporation and their auditors Arthur Andersen, which \
    was revealed in late 2001. The scandal caused the dissolution of Arthur \
    Andersen, which at the time was one of the five largest accounting firms \
    in the world. After a series of revelations involving irregular \
    accounting procedures conducted throughout the 1990s, Enron filed for \
    Chapter 11 bankruptcy protection in December 2001. One consequence of \
    these events was the passage of Sarbanes-Oxley Act in the United States \
    2002, as a result of the first admissions of fraudulent behavior made \
    by Enron. The act significantly raises criminal penalties for securities \
    fraud, for destroying, altering or fabricating records in federal \
    investigations or any scheme or attempt to defraud shareholders. ''',
    category_name=category5
    )
session.add(Item3)
session.commit()
session.close()


print ("added Accounting catalog items!")
