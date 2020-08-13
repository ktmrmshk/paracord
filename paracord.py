import subprocess
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG)

class pwork(object):
    def __init__(self, timeout=None):
        self.timeout=timeout
        
    def work(self, cmd):
        try:
            ret=subprocess.check_output(cmd, timeout=self.timeout)
            logging.info('Ret: {}'.format(ret.decode('utf-8').strip() ) )
        except subprocess.TimeoutExpired as e:
            logging.error('timeout')
            logging.error('{}, {}, {}, {}'.format(e.cmd, e.timeout, e.output, e.stderr))
        except:
            logging.error('some errors')

    def run(self, cmd):
        self.work(cmd)


class pcord(object):
    def __init__(self, num_worker=1):
        self.num_worker = num_worker

    def run_worker(self, work, args):
        with Pool(processes=self.num_worker) as pool:
            pool.map(work, args)


def test2():
    cmd = ['sleep', '2']
    pc=pwork(1)
    pc.run(cmd)

def test():
    cmd = ['sleep', '2']
    pc=pwork(3)
    
    man=pcord(2)

    man.run_worker(pc.work, [cmd]*4)
    

if __name__ == '__main__':
    test()
