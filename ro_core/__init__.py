import roplus
import gamelog

'''
Turns off debugging in Revelation Online's built-in debugger
  This is intended to be imported, then executed.
'''

def fake_debugger(*args, **kw):
    ''' Instead of being noisy and logging to the built-in logger, just do nothing '''
    pass

def silence_debug():
    if gamelog.debug.__name__ == 'debug':  # The default function name
        gamelog.debug = fake_debugger
        roplus.log('gamelog.debug silenced.')
    else:
        roplus.log('gamelog.debug was already silenced. Skipping...')

def silence_info():
    if gamelog.info.__name__ == 'info':  # The default function name
        gamelog.info = fake_debugger
        roplus.log('gamelog.info silenced.')
    else:
        roplus.log('gamelog.info was already silenced. Skipping...')

def silence_error():
    if gamelog.error.__name__ == 'error':  # The default function name
        gamelog.error = fake_debugger
        roplus.log('gamelog.error silenced.')
    else:
        roplus.log('gamelog.error was already silenced. Skipping...')
