import os
import base64
a="JVCEC5COKRAXITSULF2FC6SBORGUIQLUJVCGOSY="
a=base64.b32decode(a.encode("utf-8")).decode("utf-8","ignore")
a=base64.b64decode(a.encode("utf-8")).decode("utf-8","ignore")

li=(base64.b16encode(a.encode("ascii"))).decode("utf-8")



print(li)