# bcferries-trips

## Purpose
This script produces a new trips.txt file with all block_ids removed and a concated service_id+trip_id for all trips with a trip_short_name.

## Usage
Tested with Python 3.9.<br>
```python bc-trips.py trips.txt```<br>
Adjusted trips.txt file is exported to the current directory for human review, after which it can be used for subsequent post-export modifications.<br>
