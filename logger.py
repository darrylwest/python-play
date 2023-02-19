#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 13:48:27
#

# @see https://docs.python.org/3/howto/logging-cookbook.html for improved formatting, file rotation, etc.

import logging as log

fname='test.log'
log.basicConfig(filename=fname, filemode='w', level=log.DEBUG)

def main():
    log.debug("a debug test")
    log.info('this is a test...')
    log.warning('warning you')
    log.error('this is an error')

    print('look at the logfile %s' %{fname})


if __name__ == '__main__':
    main()
