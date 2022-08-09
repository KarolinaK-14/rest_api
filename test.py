import requests
BASE = 'http://127.0.0.1:5000/'


# data = [{'likes': 10, 'name': 'Tim', 'views': 50000},
#         {'likes': 89, 'name': 'how to make rest api', 'views': 100},
#         {'likes': 23, 'name': 'bill', 'views': 200000},
#         {'likes': 90, 'name': 'carol', 'views': 5}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + 'video/' + str(i), data[i])
#     print(response.json())
#input()
#response = requests.delete(BASE + 'video/0')
#print(response)
# input()
response = requests.patch(BASE + 'video/2', {})
print(response.json())
