import socket
import json
import argparse
import logging
import select
import struct
import time



def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', 
        dest="port", 
        type=int, 
        default='9999',
        help='port number to listen on')
    parser.add_argument('--loglevel', '-l', 
        dest="loglevel",
        choices=['DEBUG','INFO','WARN','ERROR', 'CRITICAL'], 
        default='INFO',
        help='log level')
    args = parser.parse_args()
    return args


def main():
    args = parseArgs()      # parse the command-line arguments

    # set up logging
    log = logging.getLogger("myLogger")
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    level = logging.getLevelName(args.loglevel)
    log.setLevel(level)
    log.info(f"running with {args}")
    
    log.debug("waiting for new clients...")
    serverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSock.bind(("",args.port))
    serverSock.listen()

    clientList = []

    while True:

        # HERE'S WHERE YOU NEED TO FILL IN STUFF

        # DELETE THE NEXT TWO LINES. It's here now to prevent busy-waiting.
        time.sleep(1)
        log.info("not much happening here.  someone should rewrite this part of the code.")

                            
    

if __name__ == "__main__":
    exit(main())

