
import xlrd

from Methods import Methods_List


class Test_VerifyCreateOpportunity():
    def test_createopp(self):
        workbook = xlrd.open_workbook("C:\\Users\\MEGHANA\\Desktop\\TestData.xlsx")
        sheet = workbook.sheet_by_name("Sheet2")
        rowCount = sheet.nrows
        mtd = Methods_List()

        for i in range(1, rowCount):
            keyword = sheet.cell_value(i,3)
            if(keyword == "openApp"):
                mtd.openApplication(sheet.cell_value(i,6))
            if(keyword == "enterInTextBox"):
                mtd.enterInTextBox(sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6))
            if(keyword == "clickButton"):
                mtd.clickAButton(sheet.cell_value(i,5))
            if(keyword == "clickLink"):
                mtd.clickALink(sheet.cell_value(i,5))
            if(keyword == "clickElement"):
                mtd.clickWebElement(sheet.cell_value(i,5))
            if(keyword == "pressKey"):
                mtd.hitKeyboardButton(sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6))
            if(keyword == "SelectFromDropdown"):
                mtd.selectValueFromDropdown(sheet.cell_value(i,5),sheet.cell_value(i,6))
            if(keyword == "scrolldown"):
                mtd.scrollDown()
            if(keyword == "verifyText"):
                actualText = mtd.getText(sheet.cell_value(i,5))
                expectedText = sheet.cell_value(i,6)
                assert actualText == expectedText

            if(keyword == "closeAPP"):
                mtd.closeApplication()






