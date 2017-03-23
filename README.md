# routils

A collection of helper functions to manipulate in-game functions for Revelation Online.
See the forums at http://forums.roplus.io for addional info. More features will be added as I need them, or they are requested.

## Installation
Just place the `routils` folder into your `ROPlus\Scripts` directory

## routils.redirect
A few helpers to redirect STDOUT and STDERR to a text file for you.

## routils.ro_core
A few options to disable the various internal Revelation Online debugging functions which pollute your stdout output.

## Usage:
```Python
import roplus
from routils.ro_core import silence_debug, silence_info, silence_error
import routils.redirect

silence_debug()
silence_info()
silence_error()

routils.redirect.stdout('F:\\ro.stdout.txt')
routils.redirect.stderr('F:\\ro.stderr.txt')
```

You can optionally force the utility to clear and reopen sys.stdout. This clears the current output and opens a new file.
```
routils.redirect.stdout('F:\\ro.stdout.txt', force=True)
routils.redirect.stderr('F:\\ro.stderr.txt', force=True)
