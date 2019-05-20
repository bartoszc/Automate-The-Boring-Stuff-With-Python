stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
# {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
