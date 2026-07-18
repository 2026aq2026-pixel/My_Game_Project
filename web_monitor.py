from flask import Flask, render_template
import os

app = Flask(__name__)
# التأكد من اسم الملف الصحيح
SCAN_FILE = "scan_results-01.csv"

@app.route('/')
def home():
    if os.path.exists(SCAN_FILE):
        with open(SCAN_FILE, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return render_template('index.html', data=content)
    return "جاري انتظار البيانات من أداة المراقبة..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
