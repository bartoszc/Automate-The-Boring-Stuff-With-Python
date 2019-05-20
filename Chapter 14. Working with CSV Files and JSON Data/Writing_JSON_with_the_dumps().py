pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
# '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
