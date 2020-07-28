import random

from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def view_sprint_estimator(webdriver, datasets):
    sprint = random.choice(datasets["sprints"])
    sprint_id = sprint[0]

    sprint_page = BasePage(webdriver)

    @print_timing("selenium_view_sprint_estimator")
    def measure():
        webdriver.get(f"{JIRA_SETTINGS.server_url}/secure/EstimatorAction!sprint.jspa?sprintId={sprint_id}")
        sprint_page.wait_until_present((By.ID, "estimation-table"))

    measure()


def view_board_estimator(webdriver, datasets):
    sprint = random.choice(datasets["sprints"])
    board_id = sprint[1]

    board_page = BasePage(webdriver)

    @print_timing("selenium_view_board_estimator")
    def measure():
        webdriver.get(f"{JIRA_SETTINGS.server_url}/secure/EstimatorAction!backlog.jspa?rapidBoardId={board_id}")
        board_page.wait_until_present((By.ID, "estimation-table"))

    measure()


def view_estimator_settings(webdriver, datasets):
    sprint = random.choice(datasets["sprints"])
    board_id = sprint[1]

    settings_page = BasePage(webdriver)

    @print_timing("selenium_view_estimator_board_settings")
    def measure():
        webdriver.get(f"{JIRA_SETTINGS.server_url}/secure/SettingsAction!settings.jspa?rapidBoardId={board_id}")
        settings_page.wait_until_present((By.ID, "cols-selector"))

    measure()
