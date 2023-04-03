from atlassian import Jira
import json

jira = Jira(url='https://johndeerejira.atlassian.net', username='gianottovictors@johndeere.com', password='=29E42851', cloud=True)

# JQL method
#jql_request = "project = SAPX AND issuetype = Task"
#issue = jira.jql(jql_request)

project_key = "FS"
issue_key = "SAPX-753"

key = jira.issue(issue_key)
comments = jira.issue_get_comments(issue_key)

# dumps: Python to JSON
dump = json.dumps(comments, sort_keys=True, indent=4, separators=(",", ": "))
#print(dump)

print("Key: {}".format(key['key']))
print("Summary: {}".format(key['fields']['summary']))
print("Description: {}".format(key['fields']['description']))
print("Assignee: {}".format(key['fields']['assignee']['displayName']))
print("Status: {}".format(key['fields']['status']['name']))
for c in comments['comments']:
    print("Comment from {}: {}".format(c['author']['displayName'], c['body']))

# Change issue status
#print(jira.get_issue_status(issue_key))
#jira.set_issue_status(issue_key, "NEW")
#print(jira.get_issue_status(issue_key))

# Create new Issue
fields = dict(project= dict(key=project_key), 
                summary= "Test #2",
                issuetype = dict(name='Task'),
                description="This is a test to create new card using Python ans Jira module REST api.\nMake sure to delete this card.")
i = json.dumps(fields)

jira.create_issue(fields)