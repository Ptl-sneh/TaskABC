# Instagram Sentiment Analysis

## Project Description
This project allows users to perform **sentiment analysis** on Instagram post captions using a pre-trained **Hugging Face transformer model**. The project uses **Selenium** to automate login and caption extraction from Instagram posts and **Gradio** to provide an interactive UI.

### 🔹 Features:
- **Login to Instagram** using credentials.
- **Extract captions** from Instagram posts.
- **Perform sentiment analysis** on captions (Positive/Negative/Neutral).
- **Close WebDriver** to properly shut down the session.

---

##  Dependencies
Ensure you have the following dependencies installed before running the project:

```
pip install time gradio selenium webdriver-manager transformers torch
```

### Additional Requirements:
- **Google Chrome** browser should be installed.
- **ChromeDriver** is managed automatically using `webdriver-manager`.

---

## Steps to Run the Project

### 1️ Clone the Repository (If using Git)
```
git clone https://github.com/your-repo/instagram-sentiment.git
cd instagram-sentiment
```

### 2️ Install Dependencies
```
pip install -r requirements.txt
```
*(If a `requirements.txt` file is created, else install dependencies manually as listed above.)*

### 3️ Run the Python Script
```
python script.py
```

*(Replace `script.py` with your actual filename.)*

### 4️ Open the Gradio Interface
- The application will launch in a browser window.
- Follow the steps on the UI:
  1. Enter Instagram login credentials.
  2. Browse Instagram and copy a post URL.
  3. Paste the post URL and analyze sentiment.
  4. Close the WebDriver after use.

### 5️ Closing the WebDriver (Important)
- Click **'Close Browser'** in the UI or manually terminate the script.

---

##  Important Notes
- This project **requires an active Instagram account**.
- Frequent automated logins may result in **temporary account restrictions**.
- **Use responsibly** to avoid violating Instagram's terms of service.

---


