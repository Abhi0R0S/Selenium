from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#
driver = webdriver.Chrome(executable_path="C:\\Users\\dell\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.spicejet.com/")
driver.implicitly_wait(10000)
time.sleep(10)

global a ## Variable for Arrival_city_list(Multicity Trip Option)
a = 1
global b ## Variable for Depart_Dates_Button(Multicity Trip Option)
b = 1
global c ## Variable for Departure_City_Button(Multicity Trip Option)
c = 1
global d ## Variable Departure_city_list(Multicity Trip Option)
d = 1
global t2 ## Variable for Testcase2 - DepartCityCheck
t2 = 1
global t3 ## Variable for Testcase3 - ArrivalCityCheck
t3 = 1
global t4 ## Variable for Testcase4 -Depart Date(Return Date For Return Trip)
t4 = 1

class SpiceJet():

    def Type_of_Trip(self): ## (Select Type Of Trip and Spell Check)
        global Type_of_trip_Input
        Type_of_trip_Input = input("Please Enter Type of Trip(One Way/Round Trip/Multicity): ")
        global Trips
        Type_Of_Triplist = ['One Way', 'Round Trip', 'Multicity']
        for lst in Type_Of_Triplist:
            if Type_of_trip_Input == lst:
                Trips = True
                break
        else:
            Trips = False
            while Trips == False:
                print("Type same as shown in bracket...")
                Type_of_trip_Input = input("Please Enter Type of Trip(One Way/Round Trip/Multicity): ")
                for lst in Type_Of_Triplist:
                    if Type_of_trip_Input == lst:
                        Trips = True
                        break

    def Click_On_Trip(self): ## (Click On Trip Button)
        Type_of_trip_List = driver.find_elements_by_css_selector('table label')
        for t in Type_of_trip_List:
            if Type_of_trip_Input == t.text:
                t.click()

    def Multicity_PopUp(self): ## (Click On Multicity Trip Popup)
        pop_up = driver.find_element_by_id("MultiCityModelAlert")
        pop_up.click()

    def Departure_City_Btn(self): ## (Click on Departure City Button)
        DC_Button = driver.find_element_by_id('ctl00_mainContent_ddl_originStation{}'.format(c) + '_CTXTaction')
        DC_Button.click()

    def Departure_city_Input(self): ## (Departure City Input)
            input_city = input("Please Enter City Name(Departure): ").capitalize()
            return input_city

    def Arrival_city_Input(self): ## (Arrival City Input)
            input_city = input("Please Enter City Name(Arrival): ").capitalize()
            return input_city

    def Departure_City_Name(self,city_name_Input): ## (Click On Departure City)
        Departure_city_list = driver.find_elements_by_css_selector(
            'div[id="ctl00_mainContent_ddl_originStation{}'.format(d) + '_CTNR"] div[class="dropdownDiv"] a')
        def Select_City(city_name_Input):
            for city in Departure_city_list:
                if city_name_Input in city.text:
                    city.click()
                    break
            else:
                print("Please Enter a 'Valid City Name' or 'Not available'(Departure)... ")
                city_name_Input = input("Please Enter City Name(Departure): ").capitalize()
                Select_City(city_name_Input)

        Select_City(city_name_Input)

    def Arrival_City_Name(self,city_name_Input):## (Click On Arrival City)
        Arrival_city_list = driver.find_elements_by_css_selector(
            'div[id="ctl00_mainContent_ddl_destinationStation{}'.format(a) + '_CTNR"] div[class="dropdownDiv"] a')
        def Select_City(city_name_Input):
            for city in Arrival_city_list:
                if city_name_Input in city.text:
                    city.click()
                    break
            else:
                print("Please Enter a 'Valid City Name' or 'Not available'(Arrival)... ")
                city_name_Input = input("Please Enter City Name(Arrival): ").capitalize()
                Select_City(city_name_Input)

        Select_City(city_name_Input)

    def Depart_Date_Btn(self): ## (Click On Depart Date Button)
        Depart_Dates_Btns = driver.find_element_by_css_selector(
            'input[name="ctl00$mainContent$view_date{}'.format(b) + '"]')
        Depart_Dates_Btns.click()

    def Return_Date_Btn(self):## (Click On Return Date Button)
        return_date = driver.find_element_by_css_selector('input[name="ctl00$mainContent$view_date2"]')
        return_date.click()

    def Month_Input_Check(self):##( Month Input Spell Check)
        def Month_Input():
            global input_select_month
            input_select_month = input("Please Enter a Month Name: ").capitalize()
            Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']
            if input_select_month not in Months:
                print("Please Enter Month Name Correct...")
                Month_Input()
        Month_Input()

    def Select_Month_Date(self):##(Select Month and Date)
        for i in range(11):
            first_month = driver.find_element_by_css_selector(
                'div[class="ui-datepicker-group ui-datepicker-group-first"] span[class="ui-datepicker-month"]')
            first = first_month.text
            if first != input_select_month:
                slide = driver.find_element_by_css_selector('a[title="Next"]')
                slide.click()
            else:
                def Date_Number():##(Input For Date Number)
                    input_date = input("Please Enter a Date Number: ")
                    date_list = driver.find_elements_by_css_selector(
                        'div[class="ui-datepicker-group ui-datepicker-group-first"] [href="#"]')

                    def Date_Selector(month_day_number):##(Click on Date)
                        for date in date_list:
                            if month_day_number == date.text:
                                date.click()
                                break
                        else:
                            print("Entered date number is not available...")
                            Date_Number()

                    Date_Selector(input_date)

                Date_Number()
                break

    def Select_Passenger(self):
        passenger = driver.find_element_by_css_selector('div[class="paxinfo"]')
        passenger.click()
        select_adult = Select(driver.find_element_by_id('ctl00_mainContent_ddl_Adult'))
        no_of_adult = input("Please enter number of adults from 1 to 9 = ")
        select_adult.select_by_value(no_of_adult)

    def Select_Currency(self):
        currency = Select(driver.find_element_by_id('ctl00_mainContent_DropDownListCurrency'))
        global select_currency
        select_currency = input("Please enter type of currency(INR or AED or USD): ").upper()
        currency.select_by_value(select_currency)

    def Search_Flight(self):
        Search_Flight = driver.find_element_by_css_selector('span input[type="submit"]')
        Search_Flight.click()


class Testcases():
    Selected_Trip_Btn = driver.find_elements_by_css_selector('table[id="ctl00_mainContent_rbtnl_Trip"] input')

    def Testcase1(self):## (Check Which Trip Option is Selected)
        if self.Selected_Trip_Btn[0].is_selected():
            print("Testcase1: 'One Way' is selected")
        elif self.Selected_Trip_Btn[1].is_selected():
            print("Testcase1: 'Round Trip' is selected")
        elif self.Selected_Trip_Btn[2].is_selected() :
            print("Testcase1: 'Multicity' is selected")

    def Testcase2(self):## (Check Which Deaparture City is Selected)
        DepartCityCheck = driver.find_element_by_css_selector(
            'input[id="ctl00_mainContent_ddl_originStation{}'.format(t2) + '_CTXT"]').get_attribute('selectedtext')
        print("Testcase2: {} selected".format(DepartCityCheck))

    def Testcase3(self):## (Check Which Arrival City is Selected)
        ArrivalCityCheck = driver.find_element_by_css_selector(
            'input[id="ctl00_mainContent_ddl_destinationStation{}'.format(t3)+'_CTXT"]').get_attribute('selectedtext')
        print("Testcase3: {} selected".format(ArrivalCityCheck))

    def Testcase4(self):## (Check Which Depart Date(Return Date For Return Trip) is Selected )
        if t4 == 2:
            dd = driver.find_element_by_css_selector('span[id="view_fulldate_id_2"]').text
            print("Testcase4A: {} is selected".format(dd))
        else:
            dd = driver.find_element_by_css_selector('span[id="view_fulldate_id_{}'.format(t4) + '"]').text
            print("Testcase4: {} is selected".format(dd))

    def Testcase5(self):## (Check Number Of Adults is Selected)
        NumberOfAdults = driver.find_element_by_css_selector('div[id="divpaxinfo"]').text
        print("Testcase5: {} selected".format(NumberOfAdults))

    def Testcase6(self):## (Check Type Of Currency is Selected)
        curr = driver.find_element_by_css_selector(
            'select[id="ctl00_mainContent_DropDownListCurrency"] option[value="{}'.format(select_currency) + '"]')
        currDisplay = curr.is_selected()
        if currDisplay == True:
            print("Testcase6: {} is selected".format(curr.text))

    def Testcase7(self):## (Check Your Trip Details)
        print("Testcase7:")
        print("Your trip details >>>>>>>>")
        if Type_of_trip_Input == 'Multicity':
            Details = driver.find_elements_by_css_selector('div[class="trip-detrails-multi"] span')
            Dates = driver.find_elements_by_css_selector('div[class="trip-dates-multi"] span')
            n = 0
            for i in Details:
                print(Details[n].text + ':' + Dates[n].text)
                n = n + 1
        elif Type_of_trip_Input == 'Round Trip':
            Details = driver.find_elements_by_css_selector('div[class="trip-detrails"] span')
            Dates = driver.find_elements_by_css_selector('div[class="trip-dates"] span')
            print(Details[0].text + ' : ' + Details[1].text)
            print(Dates[0].text + ' : ' + Dates[1].text)
            print(Dates[2].text + ' : ' + Dates[3].text)
        elif Type_of_trip_Input == 'One Way':
            Details0 = driver.find_element_by_css_selector('div[class="trip-detrails"] span[class="trip-label"]')
            Details1 = driver.find_elements_by_css_selector('div[class="trip-detrails"] span')
            Dates = driver.find_elements_by_css_selector('div[class="trip-dates"] span')
            print(Details0.text + ' : ' + Details1[1].text)
            print(Dates[0].text + ' : ' + Dates[1].text)

        pas = driver.find_elements_by_css_selector('div[class="trip-passengers"] span')
        cur = driver.find_elements_by_css_selector('div[class="trip-currency"] span')
        print(pas[0].text + ' : ' + pas[1].text)
        print(cur[0].text + ' : ' + cur[1].text)
        print("Happy Journey.......")

class MY_Trip(SpiceJet,Testcases):
    pass

Travel = MY_Trip()
Travel.Type_of_Trip()
Travel.Click_On_Trip()

if Type_of_trip_Input == 'Multicity':
    Travel.Multicity_PopUp()

Travel.Testcase1()
Travel.Departure_City_Btn()
Travel.Departure_City_Name(Travel.Departure_city_Input())
Travel.Testcase2()
Travel.Arrival_City_Name(Travel.Arrival_city_Input())
Travel.Testcase3()
Travel.Depart_Date_Btn()
print("(Departure)")
Travel.Month_Input_Check()
Travel.Select_Month_Date()
Travel.Testcase4()

if Type_of_trip_Input == 'Round Trip':
    Travel.Return_Date_Btn()
    print("(Return)")
    Travel.Month_Input_Check()
    Travel.Select_Month_Date()
    t4 = 2
    Travel.Testcase4()

if Type_of_trip_Input == 'Multicity':
    for i in range(5):
        No_of_trip = input("U want to add next trip..(Y/N): ")
        if No_of_trip.upper() == 'Y':
            c = c + 1
            if c == 4:
                Add_More = driver.find_element_by_css_selector('input[type="button"][id="btnAddMore1"]').click()
            if c == 5:
                Add_More = driver.find_element_by_css_selector('input[type="button"][id="btnAddMore2"]').click()
            Travel.Departure_City_Btn()
            d = d + 1
            Travel.Departure_City_Name(Travel.Departure_city_Input())
            t2 = t2 + 1
            Travel.Testcase2()
            a = a + 1
            Travel.Arrival_City_Name(Travel.Arrival_city_Input())
            t3 = t3 + 1
            Travel.Testcase3()
            b = b + 1
            if b == 2:
                b = 3
            Travel.Depart_Date_Btn()
            print("(Departure)")
            Travel.Month_Input_Check()
            Travel.Select_Month_Date()
            t4 = t4 + 1
            if t4 == 2:
                t4 = 3
            Travel.Testcase4()
            if c == 5:
                break
        else:
            break

Travel.Select_Passenger()
Travel.Testcase5()
Travel.Select_Currency()
Travel.Search_Flight()
Travel.Testcase7()