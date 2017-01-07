import multiprocessing
import socket
import sys
import time
import subprocess

from subprocess import Popen


movie_path = ''
movie_path1 = '/home/pi/udp_player_see/movie1.mp4'
movie_path2 = '/home/pi/udp_player_see/movie2.mp4'
movie_path3 = '/home/pi/udp_player_see/movie3.mp4'
movie_path4 = '/home/pi/udp_player_see/movie4.mp4'
movie_path5 = '/home/pi/udp_player_see/movie5.mp4'
movie_path6 = '/home/pi/udp_player_see/movie6.mp4'
movie_path7 = '/home/pi/udp_player_see/movie7.mp4'
movie_path8 = '/home/pi/udp_player_see/movie8.mp4'
movie_path9 = '/home/pi/udp_player_see/movie9.mp4'
movie_path10 ='/home/pi/udp_player_see/movie10.mp4'

# def initial():
#     """worker function"""
#     omxp = Popen(['omxplayer',movie_path1])
#     omxp.communicate()
#     print 'over'
#     s.sendto("ok \n", addr)
#     return

def worker():
    """worker function"""
    # jobs[-1].terminate()
    print jobs
    if jobs:
    	jobs[-1].terminate()
    omxp = Popen(['omxplayer',movie_path])
    omxp.communicate()
    print 'over'
    s.sendto("ok \n", addr)
    # jobs[-1].terminate()
    # p.joing()


    return
def start():
    """worker function"""
    
    omxp = Popen(['omxplayer',movie_path1])
    omxp.communicate()
    print 'movie1 over'
    # s.sendto("ok \n", addr)
    return


p2 = multiprocessing.Process(target=start)
p2.daemon = True


flag = 0



if __name__ == '__main__':
	
	HOST = ''   # Symbolic name meaning all available interfaces
	PORT = 1111	 # Arbitrary non-privileged port
	
	# Datagram (udp) socket
	try :
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    print 'UDP Server Started...'

	except socket.error, msg :
	    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	    sys.exit()
	 
	 
	# Bind socket to local host and port
	try:
	    s.bind((HOST, PORT))
	except socket.error , msg:
	    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	    sys.exit()
	     
	print 'Socket bind complete'
	jobs = []
	i = 0
	# if p.is_alive()
	# 	p2.start()
	# p2.join()

	while True:
	
		d = s.recvfrom(1024)
		flag = 1
		data = d[0]
		addr = d[1]

		if data.strip() == 'movie1':
			subprocess.Popen('killall omxplayer.bin', shell=True)
			subprocess.Popen('killall omxplayer.bin', shell=True)
			movie_path = movie_path1
			print movie_path
		if data.strip() == 'movie2':
			subprocess.Popen('killall omxplayer.bin', shell=True)
			subprocess.Popen('killall omxplayer.bin', shell=True)
			movie_path = movie_path2
			print movie_path
		p = multiprocessing.Process(target=worker)
		p.start()

		jobs = []
        jobs.append(p)
        print jobs

	# if True:
	# 	movie_path = movie_path2
	# 	p = multiprocessing.Process(target=worker)
	# 	#jobs.append(p)
	# 	p.start()
	# 	i = i+1
