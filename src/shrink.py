# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import re

comment_re = re.compile(r'\s*//.*$')

leading_whitespace_re = re.compile(r'^\s+')

table_re = re.compile(r'^\s*(-?[0-9]+[,])\s*$')

for l in sys.stdin:
    l = re.sub(comment_re, "", l)
    l = re.sub(leading_whitespace_re, "", l)
    tm = table_re.match(l)
    if tm:
        sys.stdout.write(tm.group(1))
    else:
        sys.stdout.write(l)

