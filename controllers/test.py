# image path = '/app/uploads/image'
import json

data = [
  {
    "x": 0,
    "y": 0,
    "z": 0
  },
  {
    "x": 0,
    "y": 1,
    "z": 1
  },
  {
    "x": 1,
    "y": 0,
    "z": 0
  },
    {
    "x": 1,
    "y": 1,
    "z": 1
  }
]
print(json.dumps(data))