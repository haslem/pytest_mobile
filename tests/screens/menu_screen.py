
import locators_mobile
from appium.webdriver.common.touch_action import TouchAction

class MenuScreen(object):
	"""docstring for MenuScreen"""
	def __init__(self, mobile):
		self.mobile = mobile 

	def offline_maps(self):
		elements = self.mobile.find_elements_by_class_name('android.widget.Button')
		for i in elements:
			if i.get_attribute('text') == 'Offline maps':
				i.click()
				break
		