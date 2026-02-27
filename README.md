🎓 Engineering Role-Based Doubt Solver
A professional full-stack web application designed to help engineering students get instant, targeted explanations for their academic doubts using rule-based AI logic.

✨ Features
10 Computer Science Subjects with comprehensive coverage
60 Sample Questions (6 per subject) ready to explore
Smart Keyword Matching - Different questions get different answers
Structured Responses - Every explanation includes:
Definition of the concept
Real-world examples
Industry applications
Important keywords and terminology
Quick summary for review
Interactive UI - Two-column responsive design
No External APIs - Pure rule-based logic, works offline
Mobile-Friendly - Responsive layout for all screen sizes
🏗️ Tech Stack
Component	Technology
Backend	Python 3.13 + Flask 2.0+
Frontend	HTML5, CSS3
Data Handling	In-memory dictionaries
Logic	Rule-based keyword matching
📚 Subjects Covered
Computer Science (10 Subjects)
Algorithms - Sorting, Dynamic Programming, Binary Search, Divide & Conquer, Backtracking
Computer Networks - TCP/UDP, OSI Model, DNS, IP Routing, Protocol Stacks
Data Structures - Trees, Graphs, Stacks, Queues, Linked Lists, Heaps, Hash Tables
Operating Systems - Processes, Threads, Page Replacement, IPC, Synchronization, Scheduling
Database Management Systems - ACID Properties, Normalization, Primary Keys, Joins, Indexing
Web Development - Frontend/Backend, REST APIs, Cookies/Sessions, MVC, CORS, HTTP
Artificial Intelligence - Machine Learning, Supervised/Unsupervised Learning, Neural Networks, Clustering, Overfitting
Software Engineering - SDLC, Design Patterns, Agile, Version Control, Unit Testing, CI/CD
Compiler Design - Lexical Analysis, Parsing, Code Generation, Symbol Tables
Discrete Mathematics - Sets, Graphs, Boolean Algebra, Logic Gates, Mathematical Induction, Combinatorics
🚀 Quick Start
Prerequisites
Python 3.7 or higher
pip (Python package manager)
Modern web browser
Installation
Clone or download the project

cd "c:\Users\DELL\OneDrive\Desktop\student ai chatbot"
Install dependencies

pip install -r requirements.txt
Run the application

python app.py
💻 Usage Guide
Step 1: Select Branch
Currently set to Computer Science (fixed branch)
Dropdown displays the selected branch
Step 2: Choose Subject
Select any of the 10 CS subjects from the Subject dropdown
The dropdown populates automatically when the page loads
Step 3: Enter Your Doubt (Choose One Method)
Method A: Click Sample Questions
Sample question chips appear below the subject dropdown
6 example questions are provided for each subject
Click any chip to auto-fill the question box and get instant answer
Method B: Type Your Own Question
Click in the "Ask your doubt..." text area
Type your question about the selected subject
The system will detect keywords and provide a targeted response
Step 4: Get Your Answer
Click the "Get Explanation" button
Response displays on the right side with:
Your Question (echoed back for clarity)
Introduction from your "professor"
Definition of the concept
Real-world Examples (2-3 practical scenarios)
Industry Application (how professionals use this)
Important Keywords (key terms to remember)
Summary (quick takeaway)
Step 5: Ask More Questions
Click "Clear Question" to reset the form
Select a new subject or type another question
Repeat the process as needed
📁 Project Structure
student ai chatbot/
├── app.py                    # Flask backend + logic
├── requirements.txt          # Dependencies
├── README.md                 # This file
└── templates/ + static/      # Frontend files
🔧 How It Works
Backend: Python Flask with rule-based keyword matching
Frontend: HTML/CSS/JS with dynamic UI
Core Logic: get_response() analyzes keywords and returns HTML explanations
Response Format: Structured answers with definition, examples, keywords, industry use, summary
📊 Coverage: 60+ Targeted Responses
Each sample question maps to specific keyword handlers across all 10 subjects for intelligent, personalized answers.

📝 Requirements
Python 3.7+ with Flask>=2.0

🔐 Privacy & Security
No external APIs
No database
No data collection
Safe HTML rendering
XSS protected
🎯 Key Features
10 Computer Science subjects
60 sample questions (6 per subject)
Smart keyword-based responses
Responsive two-column UI
Works offline
📱 Browser Support
Fully compatible with Chrome, Firefox, Safari, Edge, and mobile browsers.

👨‍💻 Technology
Backend: Python 3.13 + Flask 2.0+
Frontend: HTML5 + CSS3 + JavaScript
Logic: Rule-based if/elif keyword matching
Storage: In-memory dictionaries (no database)
📞 Getting Help
Check the Troubleshooting section or verify your install with python app.py

📄 License
Educational use - modify and extend freely!

✅ Setup Checklist
 Python 3.7+ installed
 Dependencies installed (pip install -r requirements.txt)
 App running (python app.py)
 All subjects working
 Sample questions visible
 Responses displaying correctly
🎓 Happy Learning! Your Engineering Doubt Solver is ready to help you master Computer Science concepts!# Engineering-Role-Based-Doubt-Solver
Developed a full-stack rule-based academic assistant supporting 10 Computer Science subjects with 60+ structured concept explanations.
