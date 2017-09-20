#### Parse string into time object and calculate the interval (in seconds)
```
import time
from datetime import datetime

fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
time1_obj = datetime.strptime(time1, fmt)
time2_obj = datetime.strptime(time2, fmt)
time_interval = int(time.mktime(time2_obj.timetuple()) - time.mktime(time1_obj.timetuple()))
```
#### Call shell command in Python script
```
import subprocess
subprocess.call(["ls", "-l"], cwd=".")
```

#### Read xml from file_path
```
import xml.etree.ElementTree as ET
tree = ET.parse("test.xml")
root = tree.getroot()
# apply dom operations on root
```
