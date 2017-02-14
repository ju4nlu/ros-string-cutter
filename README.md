# ROS String Cutter
Service which cuts an array of strings from the index specified.

When launching the client it must specify the array following this format: 'string1 string2 stringN' and the index from which the strings have to be cutted.

For example, **rosrun beginner_tutorials string_cutter_client.py 'Lorem ipsum dolor sit amet' 3** must return:
* [em], [um], [or], [], [t]

_This project is part of an introductory assignment on Autonomous Robotics, subject taken in the Computer Science degree at Universidad de Castilla La-Mancha in course 2016-2017._
