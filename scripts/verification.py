#!/usr/bin/env python3
#
# Copyright (c) 2018 - 2019 Christoph Kepler <development@kepler.international>
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
#
# Error codes:
# -1 - no final newline error (one newline to few)
#  0 - Everything fine
#  1 - undefinded final newline error (newline not detectable)
#  2 - one final newline too much error (2 newlines)
# 12 - tab error and no final newline error
# 13 - tab error (unlucky 13)
# 14 - tab error and undefinded final newline error
# 15 - tab error and one final newline too much error
# 20 - alphabetical order error and no final newline error
# 21 - alphabetical order error (wrong order hence 21)
# 22 - alphabetical order error and undefinded final
#      newline error
# 23 - alphabetical order error and one final newline too
#      much error
# 33 - alphabetical order error and tab error and no final
#      newline error
# 34 - alphabetical order error and tab error
# 35 - alphabetical order error and tab error and undefinded
#      final newline error
# 36 - alphabetical order error and tab error and one final
#      newline too much error
# 42 - file not openable/readable error (this could mean
#      anything hence 42)
#

import sys

import newline
import tabspaces

filename = "playlist.org"

# Open the file and read it into a variable and close it

try:
    file = open(filename, 'r')
except IOError:
    print("[✖] Unable to open file [%s]" % filename)
    print("Script terminating unexpectedly before first import.")
    sys.exit(42)

data = file.readlines()

file.close()

# Return an error code and exit if the file is not readable
# ---------------------------------------------------------
# Start the final newline tests

nl_state = newline.is_there(data)

if nl_state == 1:
    print("[✔] The final newline is placed properly!")
    nl_code = 0
elif not nl_state:
    print("[✖] The final newline could not be found.")
    nl_code = 1
elif nl_state == 2:
    print("[✖] There was one final newline too much.")
    nl_code = 2
elif nl_state == -1:
    print("[✖] There was no final newline.")
    nl_code = -1

# End the final newline tests
# ---------------------------
# Start the no-tabs tests

tabs_state = tabspaces.only_spaces(data)

if tabs_state == 0:
    print("[✔] No TABS found!")
    tabs_code = 0
elif tabs_state == 13:
    print("[✖] There was a TAB found!")
    tabs_code = 13

# End the no-tabs tests
# ----------------------------------------
# Close the file and calculate return code

return_code = nl_code + tabs_code

sys.exit(return_code)
