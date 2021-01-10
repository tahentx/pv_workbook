gh_key = '42bde48dc281bd9dc4e4cc3af34ead2a44574dd6'
headers = {'Authorization': 'token %s' % gh_key}
import requests

cohort {
    'wes_mckinney' : 'wesm',
    'nick_schrock' : 'schrockn',
    'rob_nishi' : 'robertnishihara',
    'itamar' : 'itamarst'
}

data = requests.get('https://api.github.com/users/wesm/events/public')
print(data.text)