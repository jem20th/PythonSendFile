# PythonSendFile

On a Host that is connected to a LAN, 
you have a log-file that contains a list of users
who have logged onto some of the machines on the network, 
in the past 24 hrs. This script that searches for 
computers on the network that are currently online, 
and then sends a text-file to appropriate users on 
the online computers. At the end of the run, 
the script marks in the log file, computers
to which the file has been transmitted. In the log file, 
it also adds computers that have been discovered 
in the current traversal, which were not listed originally.
