#coding utf-8
import yaml

obj=yaml.load(
"""
- hero:
    hp:  34
    sp:  8
    level :  4
- orc:
    hp:
     - 12
     - 30
    sp:  0
    level:   2
""")

for i in obj:
    print i
