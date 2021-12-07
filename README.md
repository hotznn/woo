# woo

```
#!/usr/bin/python27
#coding=utf-8
from woo import hot
from woo import ajax

print hot.now()
print hot.fullid()
print ajax.get("https://www.bimwook.com:11180/woo/about.do?mode=xml")
```
