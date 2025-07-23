import streamlit as st
import pandas as pd

# ---------- DATA ----------
course_data = {
    "Science": {
        "Medical": [
            {"course": "MBBS(Bachelor of medicine and Bachelor of Surgery)", "About the course": "MBBS is a 5.5-year undergraduate degree in medicine and surgery, and the primary qualification to become a doctor (physician) in India and many countries. It includes 4.5 years of academic study + 1 year of mandatory internship.","Eligibility": "10+2 with Physics, Chemistry, Biology (PCB) & Minimum 50% marks (40 percentage for reserved categories)", "duration": "5.5 years", "Core Subjects": "Anatomy, Physiology, Biochemistry, Pathology, Microbiology, Pharmacology, Forensic Medicine, Community Medicine, General Medicine, General Surgery, Pediatrics, Obstetrics and Gynecology, Ophthalmology, ENT, Psychiatry, Dermatology, Orthopedics, Anesthesiology","career": "Doctor", "entrance": "NEET"},
            {"course": "BDS(Bachelor of Dental Surgery)","About the course": "BDS is a 5-year undergraduate degree in dentistry, designed for students aspiring to become dentists or dental surgeons. It includes 4 years of academic study + 1 year of compulsory internship.","Eligibility": "10+2 with Physics, Chemistry, Biology (PCB) & Minimum 50% marks (40 percentage  for reserved categories)", "duration": "5 years","Core Subjects": "Anatomy, Physiology, Biochemistry, Dental Materials, Oral Pathology, Pharmacology, Microbiology, General Pathology, General Medicine, General Surgery, Oral Medicine and Radiology, Prosthodontics, Periodontics, Orthodontics, Oral and Maxillofacial Surgery, Conservative Dentistry, Pedodontics, Community Dentistry, Endodontics", "career": "Dentist", "entrance": "NEET"},
            {"course": "BAMS(Bachelor of Ayurvedic Medicine and Surgery)","About the course":"BAMS (Bachelor of Ayurvedic Medicine and Surgery) is an undergraduate degree program focused on Ayurvedic medicine, a traditional system of healing that originated in India.", "Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)" ,"duration": "5.5 years", "Core Subjects": "Sanskrit, Padartha Vigyan, Rachana Sharir, Kriya Sharir, Dravyaguna Vigyan, Rasashastra & Bhaishajya Kalpana, Agadtantra, Rog Nidan, Charaka Samhita, Rasa Shastra, Kayachikitsa, Shalya Tantra, Shalakya Tantra, Prasuti Tantra & Stri Roga, Kaumarbhritya, Panchakarma, Swasthavritta, Vikriti Vigyan","career": "Ayurvedic Doctor", "entrance": "NEET"},
            {"course": "BPT(Bachelor of Physiotherphy)","About the course": "BPT (Bachelor of Physiotherapy) is a 4.5-year undergraduate program focused on physical therapy techniques to treat physical impairments, injuries, and disabilities through movement, exercise, and manual therapy.", "Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)" ,"duration": "4.5 years","Core Subjects": "Human Anatomy, Human Physiology, Biochemistry, Psychology, Sociology, Exercise Therapy, Electrotherapy, Pathology, Microbiology, Pharmacology, Biomechanics, General Medicine, General Surgery, Orthopedics, Neurology, Physiotherapy in Orthopedics, Physiotherapy in Neurology, Physiotherapy in Cardiopulmonary Conditions, Community-Based Rehabilitation, Research Methodology & Biostatistics", "career": "Physiotherapist", "entrance": "NEET/State Entrance"},
            {"course": "BHMS(Bachelor of Hmoepathic Medicine and Surgery)","About the course": "BHMS (Bachelor of Homeopathic Medicine and Surgery) is an undergraduate degree in the field of homeopathy, a system of alternative medicine based on the principle of like cures like.", "Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)","duration": "5.5 years","Core Subjects": "Anatomy, Physiology, Biochemistry, Homeopathic Pharmacy, Homeopathic Materia Medica, Organon of Medicine, Pathology, Microbiology, Forensic Medicine, Surgery, Obstetrics & Gynecology, Practice of Medicine, Community Medicine, Repertory, Case Taking & Clinical Training, Homeopathic Therapeutics", "career": "Homeopathy Doctor", "entrance": "NEET"},
            {"course": "Bachelor of Pharmacy","About the course":"Bachelor of Pharmacy (B.Pharm) is a 4-year undergraduate degree focused on the study of pharmaceutical sciences, drug formulation, and safe medication usage.","Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)", "duration": "4 years", "Core Subjects": "Human Anatomy and Physiology, Pharmaceutical Analysis, Pharmaceutics, Pharmaceutical Chemistry, Pharmacognosy, Pharmacology, Biochemistry, Pathophysiology, Microbiology, Physical Pharmaceutics, Medicinal Chemistry, Pharmaceutical Jurisprudence, Hospital and Clinical Pharmacy, Industrial Pharmacy, Pharmaceutical Biotechnology, Quality Assurance, Herbal Drug Technology, Biopharmaceutics and Pharmacokinetics, Social and Preventive Pharmacy", "career": "Pharmacist", "entrance": "no"},
            {"course": "Bachelor of science Nursing","About the course":"B.Sc Nursing is a 4-year undergraduate program that trains students in theoretical and practical aspects of nursing to care for individuals, families, and communities in healthcare settings.","Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)", "duration": "4 years","Core Subjects": "Anatomy, Physiology, Biochemistry, Nutrition, Microbiology, Psychology, Sociology, Nursing Foundations, Pharmacology, Pathology, Genetics, Medical-Surgical Nursing, Community Health Nursing, Child Health Nursing (Pediatric), Mental Health Nursing (Psychiatric), Obstetric and Gynecological Nursing, Nursing Research and Statistics, Management of Nursing Services and Education", "career": "Nurse", "entrance": "no"},
            {"course": "Bachelor of science in(Biotechnology, Microbiology, Zoology, Botany)","About the course":"These B.Sc degrees are 3-year undergraduate science programs that focus on life sciences, each with its own specialization. Below is a breakdown of each course, along with its about info and core subjects.","Eligibility": "10+2 with Physics, Chemistry, Biology (PCB)","duration": "3 years", "career": "Researcher, Lab Technician", "entrance": "no"}
        ],
        "Non-Medical": [
            {"course": "B.Tech(Computer science engineering)", "About the course": "CSE (Computer Science and Engineering) is a 4-year undergraduate engineering course that focuses on computer systems, software, and applications. It combines principles of computer science and electrical engineering to develop computer hardware and software.", "Eligibility": "10+2 with Physics, Chemistry, Mathematics (PCM); minimum 50–60% marks", "duration": "4 years","Core Subjects": "Programming in C, Data Structures, Computer Organization, Discrete Mathematics, Object Oriented Programming (C++/Java), Operating Systems, Database Management Systems, Design and Analysis of Algorithms, Computer Networks, Software Engineering, Theory of Computation, Compiler Design, Web Technologies, Machine Learning, Artificial Intelligence, Cyber Security, Cloud Computing, Mobile App Development.", "career": "Engineer", "entrance": "JEE, State CET"},
            {"course": "B.Tech(Data science engineering)","About the course":"B.Tech in Data Science (DS) is a 4-year undergraduate program focused on extracting knowledge and insights from structured and unstructured data using scientific methods, algorithms, statistics, and systems. It blends computer science, statistics, and domain knowledge to build intelligent data-driven solutions.", "Eligibility":"10+2 with PCM (Physics, Chemistry, Mathematics); minimum 50–60% marks" ,"duration": "4 years","Core Subjects":"Programming in Python, Data Structures and Algorithms, Database Management Systems, Probability and Statistics, Linear Algebra, Machine Learning, Data Mining, Big Data Analytics, Artificial Intelligence, Deep Learning, Computer Vision, Natural Language Processing, Data Visualization, Cloud Computing, Operating Systems, Computer Networks, Software Engineering, Data Ethics and Privacy." ,"career": "Engineer", "entrance": "JEE, State CET"},
            {"course": "B.Tech(Mechanical engineering)","About the course":"Mechanical Engineering is a 4-year undergraduate engineering program focused on the design, development, analysis, and maintenance of mechanical systems. It is one of the oldest and broadest branches of engineering, involving principles of physics, mechanics, thermodynamics, and materials science.","Eligibility":"10+2 with PCM (Physics, Chemistry, Mathematics); minimum 50–60% marks","duration": "4 years","Core Subjects": "Engineering Mechanics, Thermodynamics, Strength of Materials, Fluid Mechanics, Heat and Mass Transfer, Machine Design, Theory of Machines, Manufacturing Technology, Dynamics of Machines, Engineering Materials, CAD/CAM, Mechanical Vibrations, Robotics, Automobile Engineering, Industrial Engineering, Mechatronics, Refrigeration and Air Conditioning.", "career": "Engineer", "entrance": "JEE, State CET"},
            {"course": "B.Tech(Civil engineering)","About the course": "Civil Engineering is a 4-year undergraduate engineering program that deals with the design, construction, and maintenance of infrastructure such as buildings, roads, bridges, dams, and water supply systems. It is essential for shaping the physical environment of modern civilization.","Eligibility":"10+2 with PCM (Physics, Chemistry, Mathematics); minimum 50–60% marks", "duration": "4 years", "Core Subjects":"Engineering Mechanics, Strength of Materials, Structural Analysis, Concrete Technology, Fluid Mechanics, Hydraulics and Hydraulic Machines, Surveying, Geotechnical Engineering, Transportation Engineering, Environmental Engineering, Water Resources Engineering, Design of Steel Structures, Design of Concrete Structures, Construction Management, Estimation and Costing, Remote Sensing & GIS, Building Materials and Construction.","career": "Engineer", "entrance": "JEE, State CET"},
            {"course": "B.Tech(Electronic engineering)","About the course": "Electronics Engineering (also known as Electronics and Communication Engineering – ECE) is a 4-year undergraduate program that focuses on the design, development, and testing of electronic circuits, devices, communication systems, and embedded systems. It combines principles from electrical engineering, computer science, and communication technology.","Eligibility":" 10+2 with PCM (Physics, Chemistry, Mathematics); minimum 50–60% marks" ,"duration": "4 years","Core Subjects":"Electronic Devices and Circuits, Digital Electronics, Signals and Systems, Analog Circuits, Communication Systems, Electromagnetic Fields, Microprocessors and Microcontrollers, VLSI Design, Control Systems, Embedded Systems, Antennas and Wave Propagation, Digital Signal Processing, Optical Communication, Wireless Communication, Network Theory, Power Electronics.", "career": "Engineer", "entrance": "JEE, State CET"},
            {"course": "B.Tech(Artificial and ML, IT engineering)","About the course":"A 4-year specialized engineering course that focuses on the development of intelligent machines, systems, and algorithms capable of learning and decision-making. It integrates computer science, data science, AI algorithms, and machine learning frameworks.& A 4-year undergraduate program focusing on the application of computing technology to real-world processes. IT engineers specialize in software development, networking, databases, cybersecurity, and information systems. ","Eligibility":"10+2 with PCM; 50–60% marks", "duration": "4 years","Core Subjects":"Python Programming, Data Structures and Algorithms, Probability and Statistics, Linear Algebra, Machine Learning, Deep Learning, Artificial Intelligence, Natural Language Processing, Data Mining, Computer Vision, Neural Networks, Reinforcement Learning, Big Data Analytics, Cloud Computing, Ethics in AI.", "career": "Engineer", "entrance": "JEE, State CET"}, 
            {"course": "B.Sc (Physics, Chemistry, Mathematics)","About the course":"Python Programming, Data Structures and Algorithms, Probability and Statistics, Linear Algebra, Machine Learning, Deep Learning, Artificial Intelligence, Natural Language Processing, Data Mining, Computer Vision, Neural Networks, Reinforcement Learning, Big Data Analytics, Cloud Computing, Ethics in AI.","Eligibility":"10+2 with PCM subjects; minimum 45–50% marks", "duration": "3 years","Core Subjects": "Physics, Chemistry, Mathematics, Classical Mechanics, Thermodynamics, Electricity and Magnetism, Organic Chemistry, Inorganic Chemistry, Physical Chemistry, Algebra, Calculus, Differential Equations, Quantum Mechanics, Waves and Optics, Solid State Physics, Linear Algebra, Real Analysis, Statistics.", "career": "Scientist, Govt jobs, Developer", "entrance": "Merit/University Entrance"},
            {"course": "B.Sc (Computer science / Data science)","About the course":"B.Sc in Computer Science is a 3-year undergraduate degree focusing on computing principles, programming, algorithms, and system-level concepts. It is ideal for students interested in software development, system administration, or further studies in computer applications & B.Sc in Data Science is a 3-year specialized program that combines computer science, statistics, and mathematics to teach data handling, analysis, and machine learning for insights and decision-making. ","Eligibilty": " 10+2 with Mathematics or Computer Science; minimum 45–50% marks", "duration": "3 years","Core Subjects":"Programming in C/C++, Data Structures, Computer Networks, Operating Systems, Database Management Systems, Software Engineering, Web Technologies, Java Programming, Python Programming, Computer Architecture, Algorithms, Data Analytics, Cloud Computing, Cybersecurity, Artificial Intelligence,Python Programming, Data Structures, Probability and Statistics, Linear Algebra, Data Mining, Machine Learning, Big Data Analytics, Data Visualization,", "career": "Scientist, Govt jobs, Developer", "entrance": "Merit/University Entrance"},
            {"course": "B.Sc (Statistics / Artificial Intelligence)","About the course":"B.Sc in Statistics is a 3-year undergraduate program focused on the collection, analysis, interpretation, and presentation of numerical data. It builds a strong foundation in mathematics, probability, and statistical methods used in research, data analysis, and forecasting & B.Sc in Artificial Intelligence is a 3-year undergraduate degree that focuses on AI concepts, machine learning, and data-driven systems. It includes programming, algorithms, and ethical aspects of AI technologies.","Eligibility":" 10+2 with Mathematics or Computer Science; minimum 50–60% marks", "duration": "3 years", "Core Subjects":"Descriptive Statistics, Probability Theory, Statistical Inference, Linear Algebra, Regression Analysis, Sampling Techniques, Time Series Analysis, Design of Experiments, Multivariate Analysis, Numerical Methods, Statistical Quality Control, Demography, Operations Research, Computer Programming (R/Python) & Python Programming, Data Structures, Probability and Statistics, Linear Algebra, Artificial Intelligence, Machine Learning, Deep Learning, Neural Networks, Natural Language Processing, Data Mining, Computer Vision, Reinforcement Learning, Ethics in AI, Robotics, Cloud Computing.","career": "Scientist, Govt jobs, Developer", "entrance": "Merit/University Entrance"},
            {"course": "NDA(National Defence Academy)","About the course":"NDA (National Defence Academy) is a premier training institute for candidates aspiring to join the Indian Armed Forces (Army, Navy, Air Force) as officers. Admission is granted through a national-level entrance exam conducted by the Union Public Service Commission (UPSC).","Eligibility": "Nationality: Indian citizen & Age: 16.5 to 19.5 years & Qualification: For Army: 10+2 pass (any stream) and For Navy & Air Force: 10+2 with Physics and Mathematics & Marital Status: Unmarried","duration": "3 years + training", "career": "Indian Armed Forces(Officiers in Army, Navy, Air force)", "entrance": "UPSC NDA Exam(twice a year)"},
            {"course": "BCA (Bachelor of computer application)","About the course":"BCA is a 3-year undergraduate degree course that focuses on computer application development and software skills. It is ideal for students interested in programming, software development, and IT careers. The course provides foundational and advanced knowledge in computing, databases, and programming languages, preparing students for roles like software developer, system analyst, or pursuing MCA/M.Sc CS or other tech careers.", "duration": "3 years","Core Subjects":"Fundamentals of Computers, Programming in C, Data Structures, Database Management Systems, Object Oriented Programming in C++, Operating Systems, Computer Networks, Web Technologies (HTML, CSS, JS), Software Engineering, Java Programming, Python Programming, Mobile App Development, Artificial Intelligence, Cloud Computing, Data Analytics, Mathematics for Computing, Computer Architecture.", "career": "Software tester, Web Developer, System analyst", "entrance": "Merit/University Entrance"},
            {"course": "B.Architecture","About the course":"B.Arch is a 5-year undergraduate professional degree that focuses on the art, science, and technology of designing and constructing buildings and other physical structures. It combines creativity with technical knowledge in architecture, urban planning, and environmental design. The course includes both theoretical studies and practical studio work. Graduates can work as architects, urban planners, interior designers, or pursue higher studies in architecture or design.","Eligibility":"10+2 with Physics, Chemistry, and Mathematics (PCM)","duration": "3 years","Core Subjects":"Architectural Design, Building Construction, Theory of Structures, History of Architecture, Climatology, Building Materials, Site Planning, Landscape Architecture, Environmental Studies, Structural Systems, Working Drawing, Urban Design, Building Services, Computer-Aided Design (CAD), Interior Design, Town Planning, Professional Practice, Estimating and Costing.", "career": "Architect, Urban Planner, Interior Designer", "entrance": "Merit/University Entrance  / NATA or JEE Main paper "},
            {"course": "Commercial Piolet Training","About the course":"Commercial Pilot Training prepares candidates to become licensed pilots capable of flying commercial aircraft. It includes extensive theoretical classes and flying training. After successful completion, the candidate receives a Commercial Pilot License (CPL) issued by the DGCA (in India) or the respective aviation authority in other countries.","Eligibility":" (10+2 with Physics and Mathematics)  &   (Age: Minimum 17–18 years)   &    (Medical: Class 1 Medical Fitness Certificate from DGCA-approved doctor)  &   (Language Proficiency: Must be able to read, speak, and understand English)   &   (Nationality: Open to both Indian and international students)","duration": "18-36 months", "Core Subjects":"Air Navigation, Air Regulations, Aviation Meteorology, Aircraft General Knowledge, Flight Performance and Planning, Airframes and Systems, Engines, Instruments, Radio Telephony, Human Performance and Limitations, Operational Procedures, Principles of Flight, Communication (VFR/IFR), Flight Simulator Training, Actual Flying Hours (Single and Multi-Engine)","career": "Airline piolet, Cargo piolet, Flight Instructor", "entrance": "DGCA entrance + flight school interview"},
        



            
            

      
            
      
     
        ]
    },
    "Commerce": [
        {"course": "B.Com", "About the course": "B.Com is the most popular undergraduate degree for commerce students, focusing on finance, bisiness, accounting and ecnomics.", "Eligibility": "12th Commerce with 40-50%", "duration": "3 years", "Core Subjects": "Financial Accounting, Business Law, Corporate Accounting, Cost Accounting, Business Mathematics, Income Tax Law and Practice, Economics, Auditing, Business Communication, Management Accounting, Financial Management, Marketing, Human Resource Management, E-Commerce, Banking and Insurance, Company Law, Entrepreneurship Development, Business Statistics.", "career": "Accountant, Banker", "entrance": "Merit/University Entrance"},
        {"course": "CMA(Cost & Management Accountant)", "About the course":"Focuses on cost accounting, financial analysis and strategic management.",  "Eligibility": "12th Commerce", "duration": "3-4 years","Core Subjects": "Economics, Management, Accounting, Laws, Ethics, Business Mathematics, Statistics, Taxation, Cost Accounting, Operations Management, Strategic Management, Financial Management, Company Accounts, Audit, Financial Reporting, Corporate Laws, Strategic Financial Management, Strategic Cost Management, International Taxation, Performance Management, Business Valuation, Risk Management, Internal Audit", "career": "Cost Accountant, Finance Officier", "entrance": "Merit/University Entrance"},
        {"course": "B.Com(Banking & Insurance)","About the course": "B.Com in Banking and Insurance is a specialized undergraduate program designed to equip students with comprehensive knowledge and skills in banking, financial systems, insurance services, risk management, and investment strategies. It combines elements of commerce with practical banking and insurance practices to prepare students for careers in the financial sector", "Eligibility": "12th Commerce with 40-50%", "duration": "3 years","Core Subjects": "Financial Accounting, Principles of Banking and Insurance, Business Communication, Microeconomics, Business Mathematics, Principles of Management, Cost Accounting, Banking Law, Insurance Law, Corporate Accounting, Organizational Behavior, Business Economics, Quantitative Techniques, Marketing of Financial Services, E-commerce, Risk Management, International Banking and Finance, Investment Management, Financial Services and Institutions, Auditing, Strategic Management, Research Methodology, Project Work/Internship.", "career": "Loan Officier, Banker", "entrance": "Merit/University Entrance"},
        {"course": "BBA(Bachelor of Business Administration)", "About the course": "BBA (Bachelor of Business Administration) is a 3-year undergraduate degree course that provides foundational knowledge in business and management principles. It is one of the most popular courses for students aspiring to pursue careers in business, management, finance, HR, or entrepreneurship.","Eligibility": "12th any stream with 40-50%", "duration": "3 years", "Core Subjects": "Principles of Management, Business Communication, Financial Accounting, Microeconomics, Business Law, Marketing Management, Business Statistics, Human Resource Management, Financial Management, Organizational Behaviour, Cost Accounting, Business Environment, E-Commerce, Management Information Systems (MIS), Strategic Management, Operations Management, Entrepreneurship Development, International Business, Project Work.", "career": "Manager, Entrepreneur", "entrance": "DU-JAT, IPMAT"},
        {"course": "CA(Chartered Accountancy)","About the course": "The CA course is a prestigious  program offered by The Institute of Chartered Accountants of India (ICAI). It prepares students for careers in accounting, auditing, taxation, finance, and corporate law.","Eligibility": "12th Commerce with 40-50%","Core Subjects": "Principles and Practices of Accounting, Business Laws and Business Correspondence, Business Mathematics and Logical Reasoning, Business Economics, Accounting, Corporate and Other Laws, Cost and Management Accounting, Taxation, Advanced Accounting, Auditing and Assurance, Enterprise Information Systems, Financial Management, Strategic Management, Financial Reporting, Strategic Financial Management, Advanced Auditing and Professional Ethics, Corporate and Economic Laws, Direct Tax Laws and International Taxation, Indirect Tax Laws.",  "duration": "5 years", "career": "Chartered Accountant", "entrance": "CA Foundation"},
        {"course": "CS(Company Secretary)", "About the course": "CS (Company Secretary) is a professional course governed by the Institute of Company Secretaries of India (ICSI). It prepares students for legal, corporate governance, secretarial, and compliance roles in companies.", "Eligibility": "12th Commerce with 40-50%", "duration": "3-5 years","Core Subjects": "Business Communication, Legal Aptitude and Logical Reasoning, Economic and Business Environment, Current Affairs, Company Law, Jurisprudence Interpretation and General Laws, Setting Up of Business Entities and Closure, Tax Laws, Corporate and Management Accounting, Securities Laws and Capital Markets, Economic Business and Commercial Laws, Financial and Strategic Management, Governance Risk Management Compliance and Ethics, Advanced Tax Laws, Drafting Pleadings and Appearances, Secretarial Audit, Corporate Restructuring, Resolution of Corporate Disputes, Multidisciplinary Case Studies.", "career": "Company Secretary", "entrance": "CS Foundation"},
        {"course": "B.Com/BBA/BA(Ecnomics/Statistics)",  "About the course": "BA Economics provides analytical and theoretical knowledge in economics. Ideal for those interested in data analysis, policy, and government sectors.BA Statistics focuses on mathematical and statistical analysis techniques used in research, data science, and forecasting","Eligibility": "12th any stream with 40-50 percentage background in economics and Statistics", "duration": "3 years","Core Subjects":"(Microeconomics, Macroeconomics, Econometrics, Development Economics, Public Economics)&( Probability, Statistical Methods, Sampling Techniques, Data Analysis, Regression, Time Series)",  "career": "Finance , Govt jobs, UPSC, MBA, CA", "entrance": "Merit/University Entrance"},
        {"course": "BCA (Bachelor of computer application)", "About the course": "BCA is an undergraduate program focused on computer applications and software development. It is ideal for students aiming for a career in the IT industry, especially in software development, web design, or data science.",  "Eligibility": "10+2 in any stream (preferably with Mathematics or Computer Science); minimum 45–50% marks", "duration": "3 years", "Core Subjects": "Programming in C/C++, Java, Data Structures, Database Management, Web Development, Operating Systems, Networking, Software Engineering", "career": "Software tester, Web Developer, System analyst", "entrance": "Merit/University Entrance"},
        {"course": "BHM/B.Sc Hotal management","About the course": "Both are undergraduate courses focused on hospitality, hotel administration, and tourism management, but with slight differences in approach (BHM is more managerial; B.Sc is more technical/scientific).",  "Eligibility": "	10+2 in any stream (Arts/Commerce/Science); 45–50% ", "duration": "4 years(degree) , 2 years(diploma)", "Core  Subjects": "Food Production, Front Office Management, Housekeeping, Food & Beverage Service, Hospitality Marketing, Hotel Accounting, Event Management, Travel & Tourism, Communication Skills, Hygiene & Nutrition","career": "Chef, Hotel Manager, Cruise Line, Hospitality", "entrance": "no"},
        {"course": "Bachelor of Law (BA LLB / BBA LLB)", "About the course": "BA LLB and BBA LLB are 5-year integrated law programs combining a bachelor’s degree (Arts or Business Administration) with Bachelor of Laws (LLB). These are ideal for students who want to pursue a legal career right after 12th.", "Eligibility": "10+2 in any stream (Arts/Commerce/Science) 45–50% ","duration": "5 years","Core Subjects": "Constitutional Law, Criminal Law, Civil Law, Contract Law, Family Law, Environmental Law, Company Law, IPC, CPC, Law of Evidence, Human Rights" ,"career": "Lawyer, Legal advisor, Judge(via PCS-J)", "entrance": "CLAT , LSAT"},
        {"course": "Bachelor in Foriegn Trade (BFT)","About the course": "BFT (Bachelor in Foreign Trade) is a 3-year undergraduate program focused on international trade, export-import management, global economics, and international business practices. It prepares students for careers in global commerce, trade regulation, logistics, and international marketing.","Eligibility": "12th Commerce with 40-50%", "duration": "3 years","Core Subjects": "International Trade Theory, Export-Import Management, International Marketing, Global Business Environment, Trade Documentation, Foreign Exchange Management, Logistics & Supply Chain, International Business Law, Customs Procedures, E-commerce", "career": "Export Manager, Trade Analyst", "entrance": "CUET,Merit/University Entrance"},
        {"course": "Finance & Stock Market courses", "About the course": "Courses in Finance & Stock Market focus on financial planning, investment strategies, stock trading, capital markets, and risk management. These can be pursued as degree programs, diplomas, or certifications, depending on your academic level and career goal.", "Eligibility":"10+2 in any stream (Commerce preferred); 45–50% minimum marks","duration": "6 month - 2 year", "Core Subjects": "Financial Accounting, Corporate Finance, Investment Analysis, Stock Market Operations, Derivatives and Futures, Technical Analysis, Fundamental Analysis, Risk Management, Portfolio Management, Capital Markets, Mutual Funds, Financial Planning, Wealth Management", "career": "Equity Analyst, Stock Broker", "entrance": "NISM, NSE exams"},
        {"course": "Digital Marketing courses","About the course": "Digital Marketing courses teach how to promote products/services using digital platforms like search engines, social media, email, and websites. These courses are available as certificates, diplomas, UG/PG degrees, and are suitable for students, job seekers, and entrepreneurs.", "Eligibility":"10+2 in any stream", "duration": "6 month - 1 year", "Core Subjects": "SEO (Search Engine Optimization), SEM (Google Ads), Social Media Marketing (SMM), Email Marketing, Content Marketing, Web Analytics (Google Analytics), Affiliate Marketing, Influencer Marketing, E-commerce Marketing, Video Marketing (YouTube), Mobile Marketing, Online Reputation Management (ORM), Marketing Automation","career": " SEO Analyst, Social Media Marketer", "entrance": "No entrance"},
        {"course": "B.Design courses","About the course":"B.Design (Bachelor of Design) is a 4-year undergraduate program focused on creativity, aesthetics, design thinking, and technical skills in fields like fashion, graphic, product, interior, and UI/UX design. It's ideal for students interested in art, innovation, and practical design solutions.", "Eligibility":"10+2 in any stream", "duration": "4 year","Core Subjects": "Design Fundamentals, Visual Communication, Elements of Design, Computer-Aided Design (CAD), Typography, Material Studies, Design Thinking, Color Theory, Human-Centered Design, Fashion/Textile Illustration, 3D Modeling, Portfolio Development", "career": "Fashion Designer, UI/UX, Animator", "entrance": "NID, UCEED, NIFT exams"},
        {"course": "Travel & Tourism Management","About the course":"Travel & Tourism Management is a course that prepares students for careers in the hospitality, travel, aviation, and tourism sectors. It focuses on travel operations, customer service, itinerary planning, tourism marketing, and international business practices.","Eligibility":"10+2 in any stream","duration": "3 years","Core Subjects": "Principles of Tourism, Travel Agency & Tour Operations, Geography of Tourism, Air Ticketing & CRS (GDS), Tourism Marketing, Hospitality Management, Customer Relationship Management, Tourism Laws & Ethics, Event Management, Sustainable Tourism", "career": "Travel Consultant, Event Manager", "entrance": "No Entrance"},
        
        


    
       
       

          
          
            
            
    ],
    "Arts": [
        {"course": "BA(Bachelor of Arts)","About the course":"BA is a 3-year undergraduate program in the Arts & Humanities stream.It offers a wide range of specializations like English, History, Political Science, Sociology, Psychology, Economics, and more.","Eligibility":"10+2 in any stream (Arts, Commerce, or Science) from a recognized board", "duration": "3 years","Core Subjects":"English, History, Political Science, Sociology, Psychology, Economics, Geography, Philosophy, Hindi, Public Administration, Journalism, Anthropology, Education, Fine Arts", "career": "Writer, Teacher, UPSC", "entrance": "Merit"},
        {"course": "BFA(Bachelor of Fine arts)","About the course":"BFA (Bachelor of Fine Arts) is a 4-year undergraduate degree for students interested in visual and performing arts.It includes both practical training and theoretical knowledge in fields like painting, sculpture, photography, applied arts, animation, design, and more.","Eligibility":"10+2 pass (any stream) from a recognized board with minimum 50% ", "duration": "3-4 years", "Core Subjects":"Drawing & Painting, Art History, Graphic Design, Illustration, Printmaking, Clay Modeling, Life Drawing, Applied Arts, Digital Art, Sculpture, Aesthetics, Composition, Visual Communication","career": "Artist, Designer", "entrance": "University Entrance"},
        {"course": "BJMC(Journalism & Mass)","About the course":"BJMS stands for Bachelor of Journalism and Mass Communication/Studies – a 3-year undergraduate degree in media, journalism, and communication.The course is ideal for students who want to pursue careers in news reporting, anchoring, advertising, PR, digital media, film, and communication strategy.","Eligibility":"10+2 pass (any stream) with 45% – 50%", "duration": "3 years","Core Subjects":"Introduction to Journalism, Mass Communication Theories, News Writing and Reporting, Media Laws and Ethics, Television and Radio Journalism, Public Relations, Advertising, Development Communication, Photojournalism, Digital Media, Media Research, Editing and Design, Communication Skills, Script Writing", "career": "Journalist, Media", "entrance": "University Exam"},
        {"course": "Law (BA LLB)","About the course":"BA LLB is a 5-year integrated undergraduate law program that combines Arts (BA) and Law (LLB) subjects.The course provides both legal knowledge and a foundation in social sciences like Political Science, Sociology, History, and Economics.","Eligibility":"10+2 pass (any stream) with 45% – 50% marks", "duration": "5 years", "Core Subjects":"Political Science, Sociology, History, Economics, English, Constitutional Law, Contract Law, Criminal Law (IPC), Family Law, Property Law, Tort Law, Administrative Law, Labour Law, Company Law, Environmental Law, Public International Law, Human Rights Law, Jurisprudence, Civil Procedure Code (CPC), Criminal Procedure Code (CrPC), Evidence Law, Arbitration & ADR","career": "Lawyer, Judge", "entrance": "CLAT"},
        {"course": "BA(Hons.)in English, History etc","About the course":"BA (Hons.) or Bachelor of Arts Honours is a 3-year undergraduate degree that focuses deeply on a specific subject or discipline from the arts and humanities stream.,This course is preferred by those aiming for academic careers, civil services (UPSC), law, journalism, social work, or teaching.","Eligibility":"10+2 (Any Stream) with minimum 45%–50% marks (varies by university and subject)", "duration": "3 years", "Core Subjects":"English(English Literature, Literary Theory, Poetry, Drama, Fiction, Indian Writing in English, Linguistics, American Literature, Postcolonial Literature)& History(Ancient Indian History, Medieval Indian History, Modern Indian History, World History, Indian National Movement, Historical Methods, Art & Architecture) etc","career": "Writer,Researcher, Teacher, UPSC", "entrance": "Merit"},
        {"course": "BBA(Bachelor of Business Admin)", "About the course":"BBA stands for Bachelor of Business Administration, a 3-year undergraduate degree in business and management.BBA is ideal for students aiming for careers in management, banking, finance, sales, consulting, digital marketing, or pursuing an MBA or entrepreneurship later","Eligibility":"10+2 pass (any stream) with 50% marks (varies by university). English and Math may be preferred by some institutes.","duration": "3 years", "Core Subjects":"Principles of Management, Financial Accounting, Business Communication, Business Economics, Business Law, Organizational Behaviour, Marketing Management, Financial Management, Human Resource Management, Operations Management, Business Statistics, Entrepreneurship Development, Strategic Management, Business Ethics, International Business","career": "Manager, Business Analyst, MBA", "entrance": "Merit"},
        {"course": "BSW(Bachelor of Social works)","About the course":"BSW stands for Bachelor of Social Work, a 3-year undergraduate degree that prepares students for professional work in the field of social welfare and development.BSW focuses on building skills in community development, casework, group work, social policies, counselling, and human rights advocacy.","Eligibility":"10+2 pass (any stream) from a recognized board with minimum 45%–50% marks ", "duration": "3 years","Core Subjects":"Introduction to Social Work, Social Case Work, Social Group Work, Community Organization, Human Growth and Development, Social Work Research, Social Policy and Legislation, Field Work Practicum, Rural and Urban Community Development, Sociology for Social Work, Psychology for Social Work, Communication Skills, Human Rights and Social Justice", "career": "NGO worker, Social Reformer, Counselor", "entrance": "Merit"},
        {"course": "Psychology(BA/B.Sc)", "About the course":"Psychology is the scientific study of the mind and behavior, offered as both BA (Bachelor of Arts) and B.Sc (Bachelor of Science) depending on the university.It is a 3-year undergraduate degree designed to develop understanding in areas like mental health, human behavior, cognition, emotion, personality, and social dynamics.","Eligibility":"10+2 pass (Arts or Science stream) with minimum 50% marks. Some colleges may prefer Science background for B.Sc Psychology.","duration": "3 years", "Core Subjects":"Introduction to Psychology, Developmental Psychology, Social Psychology, Cognitive Psychology, Biological Psychology, Abnormal Psychology, Psychological Testing, Research Methodology, Counseling Psychology, Statistics in Psychology, Experimental Psychology, Health Psychology, Industrial/Organizational Psychology, Positive Psychology, Personality Psychology","career": "Psychologist, Therapist, Counselor", "entrance": "Merit"},
        {"course": "Acting/Drama Courses(BPA)", "About the course":"BPA in Drama/Theatre/Acting is a 3- to 4-year undergraduate degree that focuses on the theatrical arts such as acting, direction, stagecraft, playwriting, movement, and voice training.The course combines practical training with theoretical knowledge of acting techniques, theatre history, literature, and modern performance arts.","Eligibility":"10+2 pass (any stream) with minimum 45%–50% marks","duration": "3-4 years", "Core Subjects":"Acting Theory, Voice and Speech, Body Movement, History of Indian Theatre, Western Theatre, Acting Techniques (Stanislavski, Method Acting, etc.), Stagecraft and Design, Play Production, Script Analysis, Improvisation, Direction, Mime and Physical Theatre, Theatre Music, Makeup and Costume Design, Camera Acting (in advanced years)","career": "Actor, Theatre, Artist, Director", "entrance": "Merit"},
        {"course": "Foreign Language Courses","About the course":"A Foreign Language Course is a certificate, diploma, or degree program that teaches students to read, write, speak, and understand a foreign language like French, German, Spanish, Japanese, Chinese, Korean, Russian, etc.These courses focus on linguistic skills, cultural understanding, translation, interpretation, and international communication.","Eligibility":"10+2 pass (any stream)", "duration": "1-3 years", "Core Subjects":"Grammar and Vocabulary, Spoken and Written Communication, Translation Techniques, Phonetics and Pronunciation, Listening and Comprehension, Reading and Writing Skills, Culture and Civilization of the Country, Language for Business/Media/Tourism, Literature and Text Analysis, Language Lab Practice","Core Subjects":"","career": "Translator, Interpreter, Embassy Staff", "entrance": "Institute level test"},
        {"course": "B.Ed(Integrated BA+B.Ed)","About the course":"B.Ed is a 2-year professional degree required for those who want to become school teachers in India (especially at primary, secondary, and senior secondary levels).After completing B.Ed, candidates are eligible to teach in government and private schools, and appear for exams like CTET, TET, KVS, NVS, DSSSB, etc.","Eligibility":"Bachelor’s degree (BA / B.Sc / B.Com or equivalent) with minimum 50% marks", "duration": "4 years","Core Subjects":"Philosophical and Sociological Foundations of Education, Learning and Teaching, Educational Psychology, Curriculum and Instruction, Assessment and Evaluation, Guidance and Counselling, Educational Technology and ICT, Pedagogy of School Subjects (e.g., Math, Science, Social Science, English, Hindi), Inclusive Education, Contemporary India and Education, Language Across the Curriculum, School Internship/Teaching Practice", "career": "Education officer, Teacher, UPSC", "entrance": "Merit"},
        {"course": "BHM/B.Sc Hotal management","About the course":"BHM (Bachelor of Hotel Management) or B.Sc in Hotel Management is a 3 to 4-year undergraduate program that trains students in hospitality services, hotel operations, and guest management.It also develops soft skills like communication, customer service, grooming, leadership, and problem-solving.","Eligibility":"10+2 pass (any stream) with minimum 45%–50% marks","duration": "4 years(degree) , 2 years(diploma)","Core Subjects":"Food Production, Food and Beverage Service, Front Office Operations, Housekeeping Operations, Hotel Accountancy, Hospitality Marketing, Human Resource Management, Tourism Management, Event Management, Nutrition and Food Science, Hotel Engineering, Communication Skills, Hospitality Law, Entrepreneurship Development, Industrial Training/Internship", "career": "Chef, Hotel Manager, Cruise Line, Hospitality", "entrance": "no"},
        {"course": "B.Design courses","About the course":"B.Design (B.Des) is a 4-year undergraduate degree that focuses on creative fields like Fashion Design, Interior Design, Product Design, Graphic Design, UI/UX Design, Animation, and more.Students are trained in design tools, digital software, visual aesthetics, materials, user behavior, and market trends.","Eligibility":"10+2 pass (any stream: Arts/Commerce/Science) with minimum 50% marks", "duration": "4 year","Core Subjects":"Design Fundamentals, Elements & Principles of Design, Visual Communication, Colour Theory, Computer-Aided Design (CAD), Materials and Processes, Drawing and Illustration, Typography, History of Design, Design Thinking & Research, Studio Work, Branding & Advertising, 3D Design, Portfolio Development, Internship/Industrial Project", "career": "Fashion Designer, UI/UX, Animator", "entrance": "NID, UCEED, NIFT exams"},
        {"course": "Travel & Tourism Management","About the course":"A Travel and Tourism course is a 3-year undergraduate program (like BBA/B.Sc/BA in Tourism Management) that prepares students for careers in the travel, tourism, aviation, hospitality, and event sectors.It covers areas like tour operations, ticketing, tourism marketing, travel agency management, global destinations, and customer service.","Eligibility":"10+2 pass (any stream), minimum 45%–50% marks.", "duration": "3 years","Core Subjects":"Principles of Tourism, Tourism Geography, Travel Agency & Tour Operations, Tourism Marketing, Airline & Airport Management, Foreign Language, Customer Service, Cultural Tourism, Travel Documentation & Ticketing, Hospitality Management, Eco-Tourism, Tourism Planning & Policy, Event Management, Entrepreneurship in Tourism, Internship/Project", "career": "Travel Consultant, Event Manager", "entrance": "No Entrance"},
        
        
       
        
        
        
        
    ]
}

# ---------- UI ----------
st.set_page_config(page_title="Courses After 12th", layout="centered")
st.title("🎓 Courses After 12th - Career Finder")
st.image("https://thumbs.dreamstime.com/b/courses-colorful-abstract-shapes-horizontal-text-written-over-background-146912591.jpg", width=600)
st.write("Choose your stream and find the best career options for your future!")

# Stream Selection
stream = st.selectbox("Select Your Stream After 12th", options=["Science", "Commerce", "Arts"])

st.image("https://youthincmag.com/wp-content/uploads/2019/06/science-arts-commerce-IndiaEducationnet.jpeg", width= 600)

# Science Sub-stream if applicable
if stream == "Science":
    sub_stream = st.radio("Choose Your Interest", ["Medical", "Non-Medical"])
    selected_courses = course_data["Science"][sub_stream]
else:
    selected_courses = course_data[stream]

# ---------- DISPLAY COURSES ----------
st.subheader("🔍 Recommended Courses:")

for course in selected_courses:
    with st.expander(f"{course['course']}"):
        st.write(f"**About the course:** {course.get('About the course', 'Not specified')}")
        st.write(f"**Eligibility:** {course.get('Eligibility', 'Not specified')}")
        st.write(f"**Duration:** {course['duration']}")
        st.write(f"**Core Subjects:** {course.get('Core Subjects', 'Not specified')}")
        st.write(f"**Career Options:** {course['career']}")
        st.write(f"**Entrance Exam:** {course['entrance']}")
        



# Website Title
st.set_page_config(page_title="Government Jobs ", layout="wide")
st.title("📘 Government Jobs ")
st.image("https://www.factsmostly.com/wp-content/uploads/2024/08/Government-Jobs.webp", width=600)
st.markdown("Explore various government job opportunities available after 12th and graduation across different departments in India.")

# Sample Job Data
jobs_data = [
    {
        "Job Title": "Indian Army (GD, Clerk, Tradesman)",
        "About the Job": "Join Indian Army as a soldier in various trades. Roles include General Duty, Clerk, Tradesman, etc.",
        "Posts": "GD, Clerk, Tradesman",
        "Age": "17.5 to 21 years",
        "Qualification": "10th/12th pass (varies by post)",
        "Marital Status": "Unmarried",
        "Selection Process": "Physical Test, Medical Test, Written Exam",
        "Salary": "₹21,700 – ₹69,100 per month",
        "Website": "https://joinindianarmy.nic.in"
    },
    {
        "Job Title": "SSC CHSL (Staff Selection Commission - 10+2)",
        "About the Job": "Recruitment for postal assistants, sorting assistants, DEOs, and LDCs in various government departments.",
        "Posts": "LDC, DEO, Postal Assistant",
        "Age": "18 to 27 years",
        "Qualification": "12th pass",
        "Marital Status": "No restriction",
        "Selection Process": "Tier 1, Tier 2 CBT + Typing Test",
        "Salary": "₹19,900 – ₹63,200 per month",
        "Website": "https://ssc.nic.in"
    },
    {
        "Job Title": "Indian Navy (SSR & AA)",
        "About the Job": "Serve in the Indian Navy as Senior Secondary Recruit or Artificer Apprentice.",
        "Posts": "SSR, AA",
        "Age": "17.5 to 21 years",
        "Qualification": "12th pass with Physics and Math",
        "Marital Status": "Unmarried",
        "Selection Process": "Written Test, Physical Fitness Test, Medical Exam",
        "Salary": "₹21,700 – ₹69,100 per month",
        "Website": "https://www.joinindiannavy.gov.in"
    },
    {
        "Job Title": "Railway RRB Group D",
        "About the Job": "Work in Indian Railways in positions like track maintainer, assistant pointsman, helper, etc.",
        "Posts": "Track Maintainer, Helper, Pointsman",
        "Age": "18 to 33 years",
        "Qualification": "10th pass or ITI from NCVT/SCVT",
        "Marital Status": "No restriction",
        "Selection Process": "CBT, PET, Medical Test",
        "Salary": "₹18,000 – ₹56,900 per month",
        "Website": "https://www.rrbcdg.gov.in"
    },
    {
        "Job Title": "State Police Constable",
        "About the Job": "Serve in state police forces as a constable.",
        "Posts": "Constable",
        "Age": "18 to 25 years",
        "Qualification": "10th/12th pass (depends on state)",
        "Marital Status": "Varies by state",
        "Selection Process": "Physical Test, Written Test, Medical Exam",
        "Salary": "₹21,700 – ₹69,100 per month",
        "Website": "Visit state police website"
    },
    {
        "Job Title": "UPSC(IAS, IPS, IFS)",
        "About the Job": "All India Service",
        "Posts": "IAS, IPS, IFS",
        "Age": "21 to 32 years",
        "Qualification": "Graduate",
        "Marital Status": "Any",
        "Selection Process": "Prelims + Mains + Interview",
        "Salary": "₹56,100 – ₹2,50,000 per month",
        "Website": "upsc.gov.in"    
    },
    {
        "Job Title": "SSC CGL",
        "About the Job": "Central govt graduate jobs",
        "Posts": "Auditor, Assistant, ITI",
        "Age": "18 to 32 years",
        "Qualification": "Graduate",
        "Marital Status": "Any",
        "Selection Process": "Tier I–IV",
        "Salary": "₹35,000 – ₹80,000 per month",
        "Website": "ssc.nic.in"     
    },
    {
        "Job Title": "Air Force X/Y Group",
        "About the Job": "Airman recruitment",
        "Posts": "Group X (Tech), Y (Non-Tech)",
        "Age": "17 to 21 years",
        "Qualification": "12th with PCM (X), any stream (Y)",
        "Marital Status": "no",
        "Selection Process": "Online + Physical + Medical",
        "Salary": "₹26,000 – ₹40,000 per month",
        "Website": "agnipathvayu.cdac.in"  
    },
    {
         "Job Title": "Forest Guard",
        "About the Job": "Wildlife & forest duties",
        "Posts": "Vanrakshak",
        "Age": "18 to 27 years",
        "Qualification": "12th any stream ",
        "Marital Status": "Any",
        "Selection Process": "PET + Written",
        "Salary": "₹21,000 – ₹40,000 per month",
        "Website": "Respective State PSC"  
    },
    {
         "Job Title": "	Indian Coast Guard (Navik)",
        "About the Job": "Maritime duties",
        "Posts": "Navik GD,DB",
        "Age": "18 to 22 years",
        "Qualification": "12th any stream ",
        "Marital Status": "No",
        "Selection Process": "CBT + Physical + Medical",
        "Salary": "₹21,000 – ₹47,000 per month",
        "Website": "joinindiancoastguard.cdac.in" 
    },
    {
          "Job Title": "IBPS PO/Clerk",
        "About the Job": "PSU bank jobs",
        "Posts": "PO,Clerk",
        "Age": "20 to 30 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Prelims + Mains + Interview",
        "Salary": "₹29,000 – ₹55,000 per month",
        "Website": "ibps.in" 
    },
    {
     
        "Job Title": "ISRO Assistant",
        "About the Job": "Clerical/scientific support",
        "Posts": "Assistant UDC",
        "Age": "18 to 28 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "CBL + Skill Test",
        "Salary": "₹25,500 – ₹81,100 per month",
        "Website": "isro.gov.in"    
    },
    {
        "Job Title": "RBI Assistant",
        "About the Job": "Clerical jobs in RBI",
        "Posts": "Assistant ",
        "Age": "20 to 28 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Prelims + Mains + LPT",
        "Salary": "₹40,000 – ₹60,000 per month",
        "Website": "rbi.org.in"    
    },
    {
         "Job Title": "CDS(UPSC)",
        "About the Job": "Officier recruitment in defense",
        "Posts": "IMA, AFA, OTA ",
        "Age": "19 to 25 years",
        "Qualification": "Graduate ",
        "Marital Status": "No",
        "Selection Process": "Written + SSB + Medical",
        "Salary": "₹56,000 to 2,00,000 per month",
        "Website": "upsc.gov.in"    
    },
    {
         "Job Title": "State PCS",
        "About the Job": "State level admin services",
        "Posts": "SDM, DSP, BDO ",
        "Age": "21 to 40 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Prelims + Mains + Interview",
        "Salary": "₹50,000 to 1,50,000 per month",
        "Website": "State PSC sites"   
    },
    {
       
         "Job Title": "LIC AAO",
        "About the Job": "Life insurance corp.jobs",
        "Posts": "AAO ",
        "Age": "21 to 30 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Prelims + Mains + Interview",
        "Salary": "₹37,795 to 60,000 per month",
        "Website": "licindia.in"    
    },
    {
          "Job Title": "FCI Manager",
        "About the Job": "Food supply admin jobs",
        "Posts": "Manager Asst. ",
        "Age": "21 to 28 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Online Test + Intreview",
        "Salary": "₹40,000 to 1,40,000 per month",
        "Website": "fci.gov.in" 
    },
    {
         "Job Title": "State Police Driver",
        "About the Job": "Transport police dept.",
        "Posts": "Constable driver",
        "Age": "18 to 27 years",
        "Qualification": "12th any stream + Driving License ",
        "Marital Status": "Any",
        "Selection Process": "Driving Test + Physical + Written",
        "Salary": "₹21,000 – 30,000 per month",
        "Website": "Respective State Police" 
    },
    {
          "Job Title": "SSC MTS",
        "About the Job": "Multitasking roles",
        "Posts": "Peon, Clerk, Watchman",
        "Age": "18 to 27 years",
        "Qualification": "12th any stream or 10th pass ",
        "Marital Status": "Any",
        "Selection Process": "CBT  + PET",
        "Salary": "₹18,000 – 22,000 per month",
        "Website": "ssc.nic.in"

    },
    {
        
          "Job Title": "RPF Constable",
        "About the Job": "Railway Police  Force",
        "Posts": "Constable (RPF)",
        "Age": "18 to 25 years",
        "Qualification": "12th any stream or 10th pass ",
        "Marital Status": "Any",
        "Selection Process": "Written + PET + Medical",
        "Salary": "₹21,000 – 69,000 per month",
        "Website": "rpf.indianrailways.gov.in"

    },
    {
        "Job Title": "Anganwadi Worker",
        "About the Job": "Child welfare roles",
        "Posts": "Supervisor, Worker",
        "Age": "18 to 35 years",
        "Qualification": "12th any stream or 10th pass ",
        "Marital Status": "Any",
        "Selection Process": "Merit/Interview",
        "Salary": "₹8,000 – 25,000 per month",
        "Website": "State Govt Sites / wcd.nic.in"  
    },
    {
          "Job Title": "UPSC EPFO/APFC",
        "About the Job": "Enforcement officier",
        "Posts": "EO, APFC ",
        "Age": "21 to 30 years",
        "Qualification": "Graduate ",
        "Marital Status": "Any",
        "Selection Process": "Online Test + Intreview",
        "Salary": "₹47,000 to 1,51,000 per month",
        "Website": "upsc.gov.in" 
    }
]

# Display Jobs in Streamlit
for job in jobs_data:
    with st.expander(f"🧾 {job['Job Title']}"):
        st.markdown(f"**About the Job:** {job['About the Job']}")
        st.markdown(f"**Posts Available:** {job['Posts']}")
        st.markdown(f"**Age Limit:** {job['Age']}")
        st.markdown(f"**Qualification:** {job['Qualification']}")
        st.markdown(f"**Marital Status Requirement:** {job['Marital Status']}")
        st.markdown(f"**Selection Process:** {job['Selection Process']}")
        st.markdown(f"**Salary:** {job['Salary']}")
        st.markdown(f"**Official Website:** [Visit Website]({job['Website']})")

# Footer
st.markdown("---")
st.markdown("ℹ️ Data is based on recent trends and may vary by year or region. Always refer to the official website for the latest information.")
st.write("Thanks for visit my website Gurpreet heer")
                             






 




