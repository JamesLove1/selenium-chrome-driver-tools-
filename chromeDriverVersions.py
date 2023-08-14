# %%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Status: Working 
# Manual way

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.python.org")

input("Press enter to leave: \n>>")
driver.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Status: Works
# pipenv install chromedriver-py==115.0.5790.170
# https://pypi.org/project/chromedriver-py/
# Notes: uses uptodate driver

from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable

print(binary_path)

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)
driver.get("http://www.python.org")

input("Press enter to leave: \n>>")
driver.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Status: Works
# pip install webdriver-manager
# https://pypi.org/project/webdriver-manager/
# Notes: uses an outdated driver

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

print(ChromeDriverManager().install())

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.python.org")

input("Press enter to leave: \n>>")
driver.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Status: Not working
# pipenv install chromedriver-autoinstaller
# https://pypi.org/project/chromedriver-autoinstaller/
import chromedriver_autoinstaller
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.get("http://www.python.org")

input("Press enter to leave: \n>>")

driver.close()
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Status: Not Working
# pipenv install get-chrome-driver
# https://pypi.org/project/get-chrome-driver/
# Notes: Buggy opens up mutiple uncalled for windows 

# Part 1
from get_chrome_driver import GetChromeDriver
from selenium import webdriver

# Install the driver:
# Downloads ChromeDriver for the installed Chrome version on the machine
# Adds the downloaded ChromeDriver to path
get_driver = GetChromeDriver()
get_driver.install()

# Use the installed ChromeDriver with Selenium
driver = webdriver.Chrome()

driver.get("http://www.python.org")

input("Press enter to leave: \n>>")

driver.close()
# %%
# part 2 
from get_chrome_driver import GetChromeDriver

get_driver = GetChromeDriver()

# Print the stable version
print(get_driver.stable_version())

# Print the stable version download link
print(get_driver.stable_version_url())

# Print the download link of a specific version
print(get_driver.version_url('115.0.5790.170'))

# Auto download ChromeDriver for the installed Chrome version
# Optional: use output_path= to specify where to download the driver
# Optional: use extract=True to extract the file
get_driver.auto_download(extract=True)

# Download the stable driver version
# Optional: use output_path= to specify where to download the driver
# Optional: use extract=True to extract the zip file
get_driver.download_stable_version(extract=True)

# Download a specific driver version
# Optional: use output_path= to specify where to download the driver
# Optional: use extract=True to extract the file
get_driver.download_version('115.0.5790.170', extract=True)

print(get_driver._output_path("115.0.5790.170"))

# %%
