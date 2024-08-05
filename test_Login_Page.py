import pytest
from openpyxl.styles import PatternFill
from datetime import datetime
from page.Home_Page import Home_Page
from page.Login_Page import Login_Page
from configuration.config import BasePage
from Utilfile.XLUtilfile import XLU

file = r"C:\Users\admin\PycharmProjects\pythonProject1\task27.xlsx"
sheetName = "data"


@pytest.mark.usefixtures("chrome_driver")
class Test_Login:
    def test_login(self):
        row = XLU.getRowCount(file, sheetName)
        for r in range(2,row+1):
            username = XLU.readData(file, sheetName, r, 2)
            passcode = XLU.readData(file, sheetName, r, 3)

            # obj of Login_Page
            l = Login_Page(self.driver)
            home_page = l.click_login(username, passcode)

            # adding the current date to excel
            run_date = datetime.now().strftime('%Y-%m-%d')
            XLU.writeData(file, sheetName, r, 4, run_date)

            # adding the current time to excel
            run_time = datetime.now().time().strftime('%H:%M:%S')
            XLU.writeData(file, sheetName, r, 5, run_time)

            try:
                assert home_page.entering_the_home_page().is_displayed()
                XLU.writeData(file, sheetName, r, 6, 'Sandhya')
                XLU.writeData(file, sheetName, r, 8, 'TEST PASSED')

                # fillGreen is fill the color of Green to excel cell
                XLU.fillGreenColor(file, sheetName, r, 8)
                home_page.do_logout()
            except:
                XLU.writeData(file, sheetName, r, 6, 'Sandhya')
                XLU.writeData(file, sheetName, r, 8, 'TEST FAILED')

                # fillRed is fill the color of Red to excel cell
                XLU.fillRedColor(file,sheetName,r, 8)
                home_page.refresh()

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v"])
