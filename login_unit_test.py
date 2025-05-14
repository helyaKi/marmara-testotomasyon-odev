from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome tarayısıcı otomatik açılır ve login sayfasına yönlendirilir
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
# <input type="text"> ve <input type="password"> etiketleri bulur ve belirlenen key'leri input olarak bu alanlara yazar
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("usernameDeneme")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("sifreDeneme" + Keys.RETURN)

# Hata Mesajı Denetimi
try:
    # 3 saniye boyunca <div id="flash"> etiketinin görünür olmasını bekler. 
    errMsg = WebDriverWait(driver, 3).until( EC.visibility_of_element_located((By.ID, "flash")) ).text
    # Hata mesajında "invalid" kelimesi varsa print'i çalıştırır
    assert "invalid" in errMsg.lower() 
    print("Test Başarılı: Hatalı giriş mesajı göründü.")
except:
    print("Test Başarısız: Hata mesajı bulunamadı.")
finally:
    time.sleep(1)
    driver.quit()
