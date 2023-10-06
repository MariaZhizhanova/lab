```python
import datetime
import time

start_time = datetime.datetime.now()

while (datetime.datetime.now() - start_time).seconds < 5:
    current_time = datetime.datetime.now()
    print(current_time.strftime("%d-%m-%Y %H:%M:%S"))
    time.sleep(1)
```
