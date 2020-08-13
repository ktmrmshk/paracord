import subprocess
import logging

class pcord(object):
    def __init__(self, timeout=None):
        self.timeout=timeout

    def run(self, cmd):
        try:
            ret=subprocess.check_output(cmd, timeout=self.timeout)
            ('Ret: {}'.format(ret.decode('utf-8').strip() ) )
        except subprocess.TimeoutExpired as e:
            logging.error('timeout')
            logging.error('{}, {}, {}, {}'.format(e.cmd, e.timeout, e.output, e.stderr))
        except:
            logging.error('some errors')

def test():
    cmd = ['sleep', '2']
    pc=pcord(1)
    pc.run(cmd)


if __name__ == '__main__':
    test()
