#!/usr/bin/python
#-*- encoding:utf-8 -*-

import sys, os;
import time, datetime;
import math;
if __name__ == "__main__":
    '''
    if len( sys.argv ) < 2:
        print "python monitor.py process";
        exit( -1 );
    process = sys.argv[1];
    '''
    while True:
        process = "*";
        process2 = "*";
        cmd = "ps -ef | egrep \"(%s|%s)\" | awk -F \" \" '{print $2,$5}'" % (process,process2);
        Res = os.popen( cmd ).readlines();
        min = "%d" % int(time.strftime( "%M", time.localtime( time.time() ) ));
        for line in Res:
            line = line.strip();
            processinfo = line.split( ' ' );
            ntime = "%d" % int(processinfo[1].split(':')[1]);
            if math.fabs( int(min) - int(ntime )) >2:
                cmd = "kill -9 %s" % processinfo[0];
                os.system( cmd );
        time.sleep( 60 );
            
