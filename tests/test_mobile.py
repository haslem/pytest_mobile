import json
import pytest
from appium import webdriver

import locators_mobile

from appium.webdriver.common.touch_action import TouchAction

from screens.main_screen import MainScreen


@pytest.fixture(scope='session')
def desired_cap():
	with open('desired_cap.json') as config_file:
		data = json.load(config_file)
	return data	



@pytest.fixture
def mobile(desired_cap):
	desired_cap = desired_cap

	driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
	driver.implicitly_wait(10)
	yield driver
	driver.quit()



def test_menu_button(mobile):
	# main_screen = mobile

	# elem = mobile.find_element_by_id(locators_mobile.map_screen['menu']).click()



	# elem = mobile.find_element_by_id('cz.seznam.mapy:id/content')
	# TouchAction(mobile).long_press(elem).move_to(x=100, y=100).release().perform()
	main_screen = MainScreen(mobile)
	main_screen.menu_click()


	elements = mobile.find_elements_by_class_name('android.widget.Button')
	for i in elements:
		if i.get_attribute('text') == 'Offline maps':
			i.click()
			break
