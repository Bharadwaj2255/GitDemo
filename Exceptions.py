from selenium import webdriver
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome("E:\\chromedriver-win64\\chromedriver")
# driver.get("https://www.expressoqa.com/Logon.aspx")



items = 0

# if items != 2:
#     raise Exception ("Products didn't added to the cart")
#     pass

try:
    # driver.find_element(By.ID, "enter").click()
    div = 10/0
    print(div)

except Exception as e:
    # raise Exception("divide with 0 is not possible")
    print(e)

finally:
    print ("finally block executed")