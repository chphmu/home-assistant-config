# Home Assistant Config by chphmu #

## Naming Concept ##

Home Assistant Type | Pattern | Hint
------ | ------ | ------
Default | ```<room>_<type>_<attr>_<name>``` |
Scene | ```<room>_<purpose>``` | scene.
Sensor | ```<room>_<sensortype>``` | sensor.
Input Text | ```<room>_<purpose>``` | Purpose must be only small letters

### Rooms ###
Room name | Room short
------ | ------
Global | glb
System | sys
Living room | lvn
Kitchen | kth
Master Bedroom | bdr
Dressing Room | drr
Child Room Left | crl
Child Room Right | crr
Guest room | gst 
Bathroom Main Floor | bt1
Bathroom First Floor | bt2
Bathroom Second Floor | bt3
Cellar Supply | cls
Cellar Laundry Room | cll
Cellar Workshop | clw
Hallway Cellar | hl0
Hallway Main Floor | hl1
Hallway First Floor | hl2
Hallway Second Floor | hl3

### Type ###
Type name | Type short
------ | ------
Button | btn
Switch | swt
Window Door Sensor | wds
Temperature Humidity Sensor | ths
Motion Sensor | mos

### Sensor Type ###
Sensor Type name | Sensor Type short
------ | ------
Temperature | tmp
Humidity | hum
Pressure | prs

### attribute ###
Attribute name| Attribute short
Batterly level | bal

