# week3-task-kusai

1. Library Management System (OOP + File Handling)

Approach: Book class with title, author, isbn, available. Data stored in books.json. Supports Add, Borrow/Return, List.
Run: python library.py
Example I/O:

Added: Harry Potter
Borrowed: Harry Potter
Returned: Harry Potter

Challenge: Data persistence and availability updates.


---

2. Weather Dashboard (API + JSON + History)

Approach: Fetch weather using OpenWeatherMap API, save last 5 searches in history.json, menu-based options.
Run: python weather.py
Example I/O:

Enter city: London
London: 22°C, clear sky
Last 5 Searches: London, Paris, Delhi

Challenge: Invalid city handling and API key usage.


---

3. Student Grades Analyzer (CSV + Pandas)

Approach: Load students.csv, calculate per-subject avg/high/low, show top 3 students, add Pass/Fail column (≥40%).
Run: python grades.py
Example I/O:

Math: Avg=60.5, High=90, Low=30
Top 3: Sara(85), Ali(65), John(40)

Challenge: Applying calculations across multiple subjects.


---

4. Simple Password Manager (File + Encoding)

Approach: Store site logins in passwords.json, passwords Base64 encoded, menu with Add/View/Exit.
Run: python password_manager.py
Example I/O:

gmail.com | ali | mypass123

Challenge: Encoding/decoding for secure storage.