from services.market import get_markets
from services.crypto import get_crypto
from services.news_service import get_macro_news

from jinja2 import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

markets = get_markets()
crypto = get_crypto()
news = get_macro_news()

template = Template(open("templates/email.html").read())

html = template.render(
    markets=markets,
    crypto=crypto,
    news=news
)

msg = MIMEMultipart("alternative")
msg["Subject"] = "Daily Market Recap"
msg["From"] = os.environ["SMTP_USER"]
msg["To"] = os.environ["EMAIL_TO"]

msg.attach(MIMEText(html, "html"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
server.send_message(msg)
server.quit()
