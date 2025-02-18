from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

BROWSER_LOCATION = 'C:\\Users\\mclea\\chromedriver\\chromedriver.exe'
URL = 'https://play2048.co/'
SLEEP_RATE = .1


class Game:
    def __init__(self):
        self.browser = webdriver.Chrome(BROWSER_LOCATION)
        self.url = URL
        self.window = None
        self.score = 0
        self.results = {}

    def run(self, count=10):
        self.open_game()
        for i in range(count):
            self.play_game()
            print(f'{i + 1}: {self.score}')
            self.results[i] = self.score
            self.restart_game()
        self.print_results()
        quit()

    def open_game(self):
        self.browser.get(self.url)
        self.window = self.browser.find_element_by_tag_name('html')

    def play_game(self):
        while self.is_game_active():
            self.bot_strategy_b()
            sleep(SLEEP_RATE)
        self.score = self.browser.find_element_by_class_name('score-container').text
    def convert_score_to_int(self):
        try:
            self.score = int(self.score)
        except:
            try: 
                self.score = int(self.score[:4])
            except:
                self.score = 0
            

    def restart_game(self):
        self.browser.find_element_by_class_name('restart-button').click()

    def is_game_active(self):
        try:
            self.browser.find_element_by_class_name('game-over')
            return False
        except NoSuchElementException:
            return True

    def bot_strategy_a(self):
        self.window.send_keys(Keys.ARROW_DOWN)
        self.window.send_keys(Keys.ARROW_RIGHT)
        self.window.send_keys(Keys.ARROW_UP)
        self.window.send_keys(Keys.ARROW_LEFT)

    def bot_strategy_b(self):
        for _ in range(10):
            self.window.send_keys(Keys.ARROW_RIGHT)
            self.window.send_keys(Keys.ARROW_UP)
            self.window.send_keys(Keys.ARROW_LEFT)
        self.window.send_keys(Keys.ARROW_DOWN)

    def bot_strategy_c(self):
        pass

    def print_results(self):
        print('\n-----2048 RESULTS------')
        for round_, score in self.results.items():
            print(f'Round {round_}: {score}')
       # print('-----------------------')
       # print(f'Best: {max(value for value in self.results.values())}')
       # print('-----------------------\n')
       # print(f'Average: {sum(value for value in self.results.values()) / len(self.results)}')


game = Game()

game.run(count=10)
