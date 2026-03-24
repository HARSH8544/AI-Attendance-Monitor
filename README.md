# AI-Attendance-Monitor
🚀 AI Productivity & Attendance Monitor
An automated, contactless, and highly accurate attendance tracking system powered by Computer Vision (OpenCV) and Flask. This project eliminates proxy attendance using real-time face recognition and provides a live web dashboard for administration.

✨ Key Features
Real-time Face Recognition: Uses LBPH (Local Binary Patterns Histograms) for high-speed detection.

Anti-Spam Logic: Intelligent cooldown system to prevent duplicate database entries.

Live Web Dashboard: A clean, responsive Flask interface to monitor logs instantly.

Automated Logging: Captures User ID, Name, Date, and precise Timestamp in an SQLite database.

Contactless & Secure: Perfect for modern workplaces and educational institutions.

🛠️ Tech Stack
Language: Python 3.11+

AI/ML: OpenCV, Haar Cascade Classifiers

Backend: Flask (Python Web Framework)

Database: SQLite3

Frontend: HTML5, CSS3, Jinja2

📁 Project Structure
Plaintext
├── templates/          # HTML files for Web Dashboard
├── app.py              # Flask Web Server
├── main.py             # Core AI Face Recognition Engine
├── database.py         # Database Connectivity & Logging Logic
├── view_logs.py        # Utility script to view logs in terminal
└── requirements.txt    # Project Dependencies
🚀 How to Run Locally
Clone the project:

Bash
git clone https://github.com/HARSH8544/AI-Attendance-Monitor.git
cd AI-Attendance-Monitor
Install Dependencies:

Bash
pip install -r requirements.txt
Run the AI Camera:

Bash
python main.py
Start the Web Dashboard:

Bash
python app.py
Navigate to http://127.0.0.1:5000/ in your browser.

📸 Screenshots
(Add your project screenshots here to make it look even better!)

👨‍💻 Developed By
Harsh Singh BCA Student | Python & AI Enthusiast
