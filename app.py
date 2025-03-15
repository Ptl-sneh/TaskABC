import time
import gradio as gr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from transformers import pipeline

# Load Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

# Start Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def login_instagram(username, password):
    """Logs into Instagram and navigates to the Explore page."""
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  

        user_input = driver.find_element(By.NAME, "username")
        pass_input = driver.find_element(By.NAME, "password")

        user_input.send_keys(username)
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(7)  
        driver.get("https://www.instagram.com/explore/tags/python")
        return "✅ Logged in! Browse posts and copy a link."
    
    except Exception as e:
        return f"❌ Login failed: {str(e)}"

def get_caption(post_url):
    """Extracts the caption from an Instagram post."""
    try:
        driver.get(post_url)
        time.sleep(5)

        caption_element = driver.find_element(By.TAG_NAME, "span")
        return caption_element.text
    except:
        return "No caption found."

def analyze_post(post_url):
    """Fetches the caption and analyzes its sentiment."""
    caption = get_caption(post_url)
    if caption == "No caption found.":
        return caption, "N/A"
    
    sentiment = sentiment_pipeline(caption)[0]
    return caption, f"{sentiment['label']} ({sentiment['score']:.2f})"

def close_driver():
    """Closes the WebDriver."""
    driver.quit()
    return "✅ WebDriver closed successfully!"

# Gradio UI using Blocks
with gr.Blocks() as app:
    gr.Markdown("# Instagram Sentiment Analysis 📊")

    # Explanation of Steps
    gr.Markdown("""
    ## 🔹 How This Works?
    1. **Login to Instagram**  
       - Enter your username and password to authenticate.
       - After logging in, browse Instagram and copy a post URL.
    
    2. **Analyze Instagram Post**  
       - Paste the Instagram post URL.
       - The caption will be extracted automatically.
       - Sentiment analysis is performed on the caption.
    
    3. **Close WebDriver**  
       - Once done, click 'Close Browser' to properly shut down the session.
    
    🚀 **Now, you can analyze any Instagram post easily!**
    """)

    with gr.Tab("Login"):
        gr.Markdown("### 🔑 Login to Instagram")
        username = gr.Textbox(label="Instagram Username")
        password = gr.Textbox(label="Instagram Password", type="password")
        login_button = gr.Button("Login")
        status = gr.Textbox(label="Login Status")
        login_button.click(login_instagram, inputs=[username, password], outputs=status)

    with gr.Tab("Analyze Post"):
        gr.Markdown("### 📌 Analyze Instagram Post Sentiment")
        post_url = gr.Textbox(label="Paste Instagram Post URL")
        analyze_button = gr.Button("Analyze")
        caption = gr.Textbox(label="Caption")
        sentiment = gr.Textbox(label="Sentiment")
        analyze_button.click(analyze_post, inputs=[post_url], outputs=[caption, sentiment])

    with gr.Tab("Close Browser"):
        gr.Markdown("### ❌ Close WebDriver")
        close_button = gr.Button("Close Browser")
        close_status = gr.Textbox(label="Status")
        close_button.click(close_driver, inputs=None, outputs=close_status)

# Run the app
app.launch()
