#!/usr/bin/env python3
#
# Copyright (c) 2018 Christoph Kepler <development@kepler.international>
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
# Internal error codes:
# -1 - no final newline error (one newline to few)
#  0 - Everything fine
#  1 - undefinded final newline error (newline not detectable)
#  2 - one final newline to much error (2 newlines)
# 13 - tab error (unlucky 13)
# 21 - alphabetical order error (wrong order hence 21)
# 42 - file not openable/readable error (this could mean
#      anything hence 42)
#

import newline
import tabspaces
import sys

filename = "playlist.org"

# Open the file

try:
    file = open(filename, 'r')
except IOError:
    print("[✖] Unable to open file [%s]" % filename)
    print("Script terminating unexpectedly.")
    sys.exit(42)

# Return an error code and exit if the file is not readable
# ---------------------------------------------------------
# Start the final newline tests

nl_state = newline.is_there(file)

if nl_state:
    print("[✔] The final newline is placed properly!")
    nl_code = 0
elif nl_state is 1:
    print("[✖] The final newline could not be found.")
    nl_code = 1
elif nl_state is 2:
    print("[✖] There was one final newline too much.")
    nl_code = 2
elif nl_state is -1:
    print("[✖] There was no final newline.")
    nl_code = -1

# End the final newline tests
# ---------------------------
# Start the no-tabs tests

tabs_state = tabspaces.only_spaces(file)

if tabs_state is 0:
    print("[✔] No TABS found!")
    tab_code = 0
elif tabs_state is 13:
    print("[✖] There was a TAB found!")
    tab_code = 13

# End the no-tabs tests
# ----------------------------------
# Calculate return code

return_code = 0

if nl_state is not 0:
    return_code += 1

if tabs_state is not 0:
    return_code += 2

if return_code is not 0:
    sys.exit(return_code)
