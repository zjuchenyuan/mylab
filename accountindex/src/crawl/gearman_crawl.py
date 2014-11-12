import gearman
import json
from crawl_relation import *

Servers=['10.171.96.244:4730', '10.162.216.1:4730', '10.171.41.109:4730',]
workfn='crawl_relations'
Queue_num=50


def taskfn(worker, job):
#    uids = json.loads(job.data)
    uid = job.data
    print worker.worker_client_id, uid
    process = CrawlRelation(uid, table=FRIENDS_TABLE)
    process.get_friends(trim_status=0)
    return 'done'


def dowork():
    import os
    gw = gearman.GearmanWorker(Servers)
    gw.set_client_id('work_%s' %os.getpid())   #optional
    gw.register_task(workfn, taskfn)
    # Enter our work loop
    gw.work()


def cli_use(fname):
    cli = gearman.GearmanClient(Servers)
    lst=[]
    for uid in seed_uids(fname):
        lst.append(dict(task=workfn, data=str(uid)))
        if len(lst)>=Queue_num:
            reqs= cli.submit_multiple_jobs(lst, wait_until_complete=False)
            res = cli.wait_until_jobs_completed(reqs)
            lst=[]
        #print req.state, req.result


def main():
    from optparse import OptionParser
    parser = OptionParser(usage='Usage: %prog [options] filename')
    parser.add_option('-w', 
                      action='store_true', dest='workermode', default=None,
                      help='worker mode')
    parser.add_option('-c', 
                      action='store_false', dest='workermode', 
                      help='client mode')
    (options, args) = parser.parse_args()
    is_worker = options.workermode
    if not is_worker and len(args)<1:
        parser.print_help()
        exit(-1)
    if is_worker:
        dowork()
    else:
        cli_use(args[0])
    

if __name__ == '__main__':
    sys.exit(main())
