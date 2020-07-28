import random

from locustio.common_utils import init_logger, jira_measure
from locustio.jira.requests_params import jira_datasets

jira_dataset = jira_datasets()

logger = init_logger(app_type='jira')


@jira_measure
def app_specific_action_board(locust):
    scrum_board_id = random.choice(jira_dataset["scrum_boards"])[0]

    response = locust.client.get(f'/rest/com.dsplugins.estimator/1.0/calculate/board/{scrum_board_id}', catch_response=True)
    assert response.status_code == 200

    issue_id = random.choice(jira_dataset['issues'])[1]

    response = locust.client.put(f'/rest/com.dsplugins.estimator/1.0/estimate/estimated/{issue_id}', "3", catch_response=True)
    assert response.status_code == 200


@jira_measure
def app_specific_action_sprint(locust):
    sprint = random.choice(jira_dataset["sprints"])
    sprint_id = sprint[0]

    response = locust.client.get(f'/rest/com.dsplugins.estimator/1.0/calculate/sprint/{sprint_id}', catch_response=True)
    assert response.status_code == 200

    issue_id = random.choice(jira_dataset['issues'])[1]

    response = locust.client.put(f'/rest/com.dsplugins.estimator/1.0/estimate/estimated/{issue_id}', "3", catch_response=True)
    assert response.status_code == 200
