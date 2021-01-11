gh_key = '42bde48dc281bd9dc4e4cc3af34ead2a44574dd6'
headers = {'Authorization': 'token %s' % gh_key}
import requests
import json
from collections import Counter
# cohort {
#     'wes_mckinney' : 'wesm',
#     'nick_schrock' : 'schrockn',
#     'rob_nishi' : 'robertnishihara',
#     'itamar' : 'itamarst'
# }

data = requests.get('https://api.github.com/users/wesm/events/public')
raw_output = json.loads(data.text)
comments = []
for event in raw_output:
    if event['type'] == 'IssueCommentEvent':
        comments.append(event)
    elif event['type'] == 'PullRequestReviewCommentEvent':
        comments.append(event)
    else:
        pass
actual_text = []
for comment in comments:
    actual_text.append(comment['payload']['issue']['body'])
print(actual_text)