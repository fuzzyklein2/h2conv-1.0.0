if __debug__:
    breakpoint()

from .startup import *
from .convert import Convert

if __name__ == '__main__':
    # print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Convert()
    p.run()
    
    # log.info(f'Execution complete.')
