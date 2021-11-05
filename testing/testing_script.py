from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
report = Report()
driver = webdriver.Chrome(executable_path="F:\\Python program\\BPMS\\testing\\driver\\chromedriver.exe")
driver.maximize_window()


report.setup(
	report_folder=r'F:\Python program\BPMS\testing\reports',
	module_name='Report',
	release_name='Release 1',
	selenium_driver=driver
)

driver.get('http://127.0.0.1:8000/')
time.sleep(4)

#Test case 1
try:
    report.write_step(
    	'Go to Donor Login Page for testing functionality',
    	status=report.status.Start,
    	test_number="18201043_1"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Donor')]").click()
    time.sleep(4)

    report.write_step(
    	'Entered Donor Login Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 2
try:
    report.write_step(
    	'Testing Donor Login Page functionality',
    	status=report.status.Start,
    	test_number="18201043_2"
    )
    driver.find_element_by_name("username").send_keys("liton123")
    print("Username writted")
    time.sleep(2)

    driver.find_element_by_name("password").send_keys("uapcse12")
    print("Password writted")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(5)
    report.write_step(
    	'Logged in',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 3
try:
    report.write_step(
    	'Go to Donate Blood page and testing Donate Blood Page functionality',
    	status=report.status.Start,
    	test_number="18201043_3"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Donate Blood')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    report.write_step(
    	'Entered Donate Blood Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 4
try:
    report.write_step(
    	'Go to Donation History Page and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_4"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Donation History')]").click()
    time.sleep(4)
    report.write_step(
    	'Entered Donation History Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 5
try:
    report.write_step(
    	'Go to Donor Blood Request Page and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_5"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Blood Request')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    report.write_step(
    	'Blood Request Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 6
try:
    report.write_step(
    	'Go to Donor Request History and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_6"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Request History')]").click()
    time.sleep(4)
    report.write_step(
    	'Request History Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 7
try:
    report.write_step(
    	'Go to Patient specific blood Request History and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_7"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Patient Request History')]").click()
    time.sleep(4)
    report.write_step(
    	'Patient Request History page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 8
try:
    report.write_step(
    	'Go to donor profile page for testing functionality',
    	status=report.status.Start,
    	test_number="18201043_8"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Profile')]").click()
    time.sleep(4)
    report.write_step(
    	'profile page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 9
try:
    report.write_step(
    	'Testing Log out functionality',
    	status=report.status.Start,
    	test_number="18201043_9"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
    time.sleep(4)
    report.write_step(
    	'Log out',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test case 10
try:
    report.write_step(
    	'Go to Patient Login Page for testing functionality',
    	status=report.status.Start,
    	test_number="18201043_10"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Patient')]").click()
    time.sleep(4)

    report.write_step(
    	'Entered Patient Login Page',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

# Test 11
try:
    report.write_step(
    	'Testing Patient Login Page functionality',
    	status=report.status.Start,
    	test_number="18201043_11"
    )
    driver.find_element_by_name("username").send_keys("shawon43")
    print("Username writted")
    time.sleep(3)

    driver.find_element_by_name("password").send_keys("uapcse123")
    print("Password writted")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(4)
    report.write_step(
    	'Logged in',
    	status=report.status.Pass,
    	screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 12
try:
    report.write_step(
    	'Go to patient Make Request page and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_12"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Make Request')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    report.write_step(
    	'Log out',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 13
try:
    report.write_step(
    	'Go to Patient Request History page and testing functionality',
    	status=report.status.Start,
    	test_number="18201043_13"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Request History')]").click()
    time.sleep(4)
    report.write_step(
    	'Patient Request History page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 14
try:
    report.write_step(
    	'Testing Log out functionality',
    	status=report.status.Start,
    	test_number="18201043_14"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
    time.sleep(4)
    report.write_step(
    	'Logout page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 15
try:
    report.write_step(
    	'Go to Available Donor page for testing functionality',
    	status=report.status.Start,
    	test_number="18201043_15"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(text(),'Available donor')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    report.write_step(
    	'Donor available page page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 16
try:
    report.write_step(
    	'Testing About us functionality',
    	status=report.status.Start,
    	test_number="18201043_16"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'About Us')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    report.write_step(
    	'entered about us page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 17
try:
    report.write_step(
    	'Testing search functionality',
    	status=report.status.Start,
    	test_number="18201043_17"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
    time.sleep(4)
    driver.find_element_by_name("bloodgroup").send_keys("AB+")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    report.write_step(
    	'search page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

#Test 18
try:
    report.write_step(
    	'Testing Contact us functionality',
    	status=report.status.Start,
    	test_number="18201043_18"
    )
    driver.find_element(By.XPATH, "//a[contains(text(),'Connect Us')]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    report.write_step(
    	'entered about us page',
    	status=report.status.Pass,
    	screenshot=True
    )

except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()

