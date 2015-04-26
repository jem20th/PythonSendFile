#!/usr/bin/env python
#
#LAN File Sending and Logging Script
#Python 2.7
#Harrison Ching
#hching@ucdavis.edu

'''	
Assume UNIX system (windows has a different netstat format)
Assume log file format is one user per line in the following format "nameofuser, ip_address"
For input simplicity, both the logfile and the text file are assumed to be in the current directory
'''

import os, re, sys, socket, mmap

#define size of text file in bytes, subject to change, only use for sendall()
sizeOfTxtFile = 4096
#command line args: names for text file and log file
txtFile = sys.argv[1]
logFile = sys.argv[2] 
#user prompt input
#txtFile = raw_input('Enter name of text file: ')
#logFile = raw_input('Enter name of log file: ')

#send file to users
def transmit(filename, ip_address, port_num):
	#if text file exists
	if os.path.exists(filename):
		#open txt file and store in packet
		with open(filename, 'rb') as f:
			#initialize socket transfer
			try:
				sock = socket.socket()
				#this can also be:
#				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			except socket.error:
				print 'Socket not created'
				sys.exit()
			print 'Socket created!'
			sock.connect_ex((ip_address, port_num))
			#this can also be: 
#			sock.connect((ip_address, port_num))
			print 'Socket connected to ' + ip_address
			#start sending file through buffer
			while True:
				chunk = f.read(sizeOfTxtFile)
				#continue until EOF
				if not chunk:
					break
				try:
					sock.sendall(chunk)
				except socket.error:
					print 'File not sent'
					sys.exit()
			print 'File sent!'
			
#print to log file
def markLog(filename, ip_address):
	flag = 0
	#check to see if log file exists
	if os.path.exists(filename):
		#append to file
		f = open(filename, 'a+')
		#scan for computers
		s = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
		if s.find(ip_address) != -1:
			#if ip matches logfile, print transmitted to ip
			f.write("\nFile transmitted to: {}".format(ip_address))
			flag = 1
		#if ip_address does not match in logfile, print transmitted to discovered ip
		if flag == 0:	
			f.write("\nFile transmitted to new discovered computer: {}".format(ip_address))
	
#in order to read the temp file by string
def readString(file):
	for line in file:
		for str in line.split():
			yield str
	
#netstat displays active TCP connections and stores it in a txt file
#use -n to skip determining host names
os.system('netstat -n > temp.txt')
flag = 0
f = open('temp.txt', 'r')
#put all strings into an interator object
read = readString(f)
#first few words are irrelevant
next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read);next(read)
	
while True:
	#only scan through local ip addresses
	for entry in read:
		#protocol check
		if entry not in ('tcp','udp','icmp','ip','tcpv6','udpv6','icmpv6','ipv6'):
			flag = 1
			break
		else:
			break
	if flag == 1:
		sys.exit()
	#skip recv, and send columns
	for entry in read:
		if True:
			break
	for entry in read:
		if True:
			break
	#read in current ip address
	for entry in read:
		local_ip = entry
		#seperate into ip and port
		ip, delim, port = local_ip.rpartition(':')
		#assert delim
		port = int(port)
		#send text file to computer
		transmit(txtFile, ip, port)
		#mark local_ip in log file
		markLog(logFile, ip)
		if True:
			break
	#skip foreign address and state columns
	for entry in read:
		if True:
			break
	for entry in read:
		if True:
			break
f.close()

#delete txt file with list of active connections
if os.path.isfile('temp.txt'):
	os.remove('temp.txt')
