from requests import get
from bs4 import BeautifulSoup
import smtplib as sm
import tkinter.messagebox as popup

url = 'https://www.amazon.com.br/Logitech-Silencioso-Ambidestro-Conex%C3%A3o-Bluetooth/dp/B0B8LBH55N/ref=sr_1_2?adgrpid=109533179216&gclid=Cj0KCQiAtvSdBhD0ARIsAPf8oNlUTAE8WAnLKJO-VSQu7QM27leHDxbaek84GH7rnb9bRLRu1P0NECEaAo58EALw_wcB&hvadid=599141263322&hvdev=c&hvlocphy=1001715&hvnetw=g&hvqmt=b&hvrand=5891680900584562239&hvtargid=kwd-295502257576&hydadcr=5267_13230654&keywords=mouse+logitech+bluetooth&qid=1673373020&refinements=p_36%3A-20000%2Cp_85%3A19171728011&rnid=19171727011&rps=1&s=computers&sr=1-2&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept-language': 'en-GB,en;q=0.9,pt;q=0.8'
}
receiver = 'elderpbfilho@gmail.com'
smtp, gmail, pwd2 = 'smtp.gmail.com', 'elder.estuda.voce.recebe.email@gmail.com', 'ndwhhxioybtizozb'

data = get(url=url, headers=header).text
soup = BeautifulSoup(data, 'html.parser')
price = int(soup.select_one('.a-price-whole').text.replace(',', ''))
if price <= 105:
    msg = f'Price achieved! Product at R$ {price}'
    with sm.SMTP(smtp, port=587) as mail:
        msg = (f'Subject: Price Achieved\n\n{msg}')
        mail.starttls()
        mail.login(user=gmail, password=pwd2)
        mail.sendmail(from_addr=gmail, to_addrs=receiver, msg=msg)
        popup.showinfo(title='Price reached!', message=msg)
else:
    popup.showinfo(title='Price not reached', message=f'Product at R$ {price}')


