from selenium import webdriver as wd


class Bot(object):
	def __init__(self):
		self.driver = wd.Firefox()
		self.navigate()


	def navigate(self, url):
		self.driver.get(url)


def main():
	bot = Bot()



if __name__ == '__main__':
    main()

