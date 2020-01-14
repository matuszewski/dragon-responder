#! python
import sys
import os
import socket, threading, time
from queue import Queue
import subprocess
from datetime import datetime
# for styling
from colorama import init
from colorama import Fore, Back, Style


#TODO DIFFERENT MASKS
from netaddr import IPNetwork
#print(str(IPNetwork('1.2.3.4/255.255.255.0').cidr))



init()
hostname = "localhost"

q = Queue()
print_lock = threading.Lock()



timeout = 0.2
threads = 200
start_port = 1
end_port = 1024


def Banner():

  print(Fore.RED)
  print("                                         ")
  print("                                                                                                   ")
  print("                                                      .                                            ")
  print("                                        ,          ;kv                                             ")
  print("                                       S          vd\           _)S                                ")
  print("                                      S$         $$|         )$NV                                  ")
  print("                                      QF        QQQV~,/)f9dd8QQ8             =P8                   ")
  print("                            '        `$V       |R$$R88$$R8RQ$$d$8R$_      _kQ$88S                  ")
  print("                            d        fQP   \XRQ$$Q8QQRRR$$$8RR$R$$$8$$\.)$$Q$R$8QR=                ")
  print("                           ;8        RR8~~9RR$Q$$$QQN$RRR$RRQ$$$8RR$RR$Q$$$$QRRR$$8                ")
  print("                           $R        8$$R$RRRRR$RRRRR$$$$$RRR$$$$$RRRR$$$$QNQ8ddRl                 ")
  print("                           R8       ;8RRQ8RRRRR$$R$$$$$$R$RRR$$$$$$RRRRR88RRR8R$                   ")
  print("                          \88      d$RQRRRRRRR$$$$$$RRRRRRRRRRRRRRR$$RR8888RRd\                    ")
  print("                          x8RV   ~RR$Q$$RRRRR$$$88R88RRRRR$$$R888RR$$$$R$RR$Qd                     ")
  print("                          V8$RV d8Q8$$$$RRRRR$$$RRR$N$RR$QR$$Q$R$88RR$$$$RQQ$R8\                   ")
  print("                          VQ$R88R$8RR$$$$$$$$$$R8RR$$$$R8d8R$$$RRRR88R$$R8QQR8$$                   ")
  print("                          SR888R8Rd$R$$$$$$$$$RR8R8$QQ$RR$88$QRR$R8888R$88QQ$888                   ")
  print("                          SR$P8RB$RRR$RR$$$R$RRRR$8$P=      .d$dB$8R8R$$R8$Q$8R$P                  ")
  print("                         v$R88R$$$$8$$RRR$$$R8R$$d/            )8QN8RR$$RR$$$RRRQ$R$88QQ$          ")
  print("                         $R$R88R$RRR$$R8R$$QQ$Rd                [RRRRRRR$$$$R$$$$$$R$88RNV         ")
  print("                        PN$$$88RRRR$$RRRR$Q$d$f                  lQ$RRR$$$$RR$$$$$$R88d$$Q         ")
  print("                      \RQRNR8RRR$$RR$RRRRRRRQ'                    /R8R$$$$$$R$RR$$$R$$$$$S         ")
  print("                      dRRRd8RQQQQ$RRRR$$$8R$k                      RR8$$$$$$R$$8$$R$RS_            ")
  print("                     PRR888R$$Q$$RR88RQQ$8RS                       RRR$$$R$$$RR$8RB                ")
  print("                    v$88R888$R$$RRR88RQQ$88`                       8RR$$RR$$R$RR8$Q                ")
  print("                   XR8; )Q$8RR$$RRRRR$RRRR,                        $8d$$RR$$R$$RR$$                ")
  print("                  `$Q9  ,$$$RRR$RRRQ$R88R\                        =RRR$R8R$$$$$d$QN                ")
  print("                 \8$v   kR$RRR$$$$RRRRR8R                         8RRRRR88$QQ$RRQQQ                ")
  print("                V88   )N$8RRR$$$$$$RQ$RRR                        8Q$$$RRRR$Q$$88Q$R                ")
  print("                8$P \d8RRQRR$$$$$$$Q$8$d/                       $QR$$RRRRR$RRR$R$$R$8f.            ")
  print("              _Q$QRR$RQRR8R$$$$$$$$Q$RRR                       =8RR$$RR$$R$$$$$$ddRRQ8888V         ")
  print("              9R; \R$8RR$R$RRRR$$$$$$8RR                      ;8Q$R$$R$$R8RR$$$$Pd8R8R$dQQ         ")
  print("                  FRQQ8dR$$$$$$$RRR888R)                     Q8Rd8R$$RRRR8RR$$RdQQ$RQR8RRP         ")
  print("                v8dNNRRRR$$$$RRR$RR$$QR\                   fQQ$d8R$Q$$RR$$$$$R8$$$QNQ$RRRl         ")
  print("               ,RRRR8RR8R$$$$R$$RQN$8S                  _XR88RRRQRRRRRRR$$$$RRR$dV[PRRd89          ")
  print("              FRR$$Rd88R$$R888R$Pv                    $Q$888dRRQ$Q$RRRR$R$RR$RR8                   ")
  print("            ;QQ8QQQ8RRR$R$$$R[                     /R$$RR8RRR$$$$$$$$$$$R$RRRR$9                   ")
  print("            8" "QdR$QNQRRdv                      `XB$R8RR$$$$$$$$$$$$$$R$$$$8$X                    ")
  print("        ;  [\   R$8$QRRRR`                      _d$$R88R$QQ$$$$$$$$$$$$R$RQ$$$'                    ")
  print("        f/8\    $R8$8$;                        lQR8888RRR$$Q$$$$$$$$$$$$Q$$88f                     ")
  print("        dS  8P  $$R8;                         R$RR8R$$$$RRRRR$$$$$$$$$$$$$Rdd$$                    ")
  print("        R; )Rx ;8P\                          RR$$$$$Q$$$$R88R$$$$$$$$$$$$$8d8$R$                   ")
  print("        kRd$RfS8                           =Q88RQQ$$RRRRRRRRR$$$$$$$$$$$$RRR$Q$8dX                 ")
  print("        vRQRR$\                           98RRQRRRR888R$$QRRR$$RRRR$$$RR8d$QQQ$$8d)                ")
  print("         P$dfSx                          RR$Q$RR8RR$RR$R$$$$$RR$RR8R8R=   x8$RRRR                  ")
  print("                                        \$$R$$R8$$QQ$RRR$$$$$$$$R8$$X.       SQ$                   ")
  print("                                        P$RRR$R8$$QQ$R88R$$$R$$$RRRx          '\                   ")
  print("                                       8888RRQR8R$$Q$$R8RRRRRR$$RRR                                ")
  print("                                      d8RP8RRNR8$R88RR$RR8$R8R$Rd8R                                ")
  print("                                      QQQ$$R$8RRdRR8d$NN$dP$Q$RRRR$                                ")
  print("                                         \SRR8dR$R8P|_      k$dR$R$[                               ")
  print("                                           \RR$R8$N          dR$$NQRd                              ")
  print("                                            RRR8RRR           P$Q$R                                ")
  print("                                            $R88RR8           ;QQV                                 ")
  print("                                            fR88QNQ                                                ")
  print("                                            `R$Q8QR                                                ")
                                                                                  
  print(Fore.RESET)                                                                                                                                     

def Logo(name):
  print("     ___                            ____             _           ")   
  print("    / _ \_______ ____ ____  ___    / __/__ _____  __(_)______ ___")
  print("   / // / __/ _ `/ _ `/ _ \/ _ \  _\ \/ -_) __/ |/ / / __/ -_|_-<")
  print("  /____/_/  \_,_/\_, /\___/_//_/ /___/\__/_/  |___/_/\__/\__/___/")
  print("                /___/                                            ")

  print(Fore.MAGENTA + "  " +name + Fore.RESET + " \t \t \t VERSION 1.3")
  

# USED BY PORT SCANNER  

def scan(port, h):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set socket on local machine
    s.settimeout(timeout)# 

    try:
        con = s.connect((h, port))
        with print_lock:
            print('['+Fore.LIGHTGREEN_EX+'OPEN'+Fore.RESET+'] ' + "\t port: " + str(port))
        con.close()
    except:
        pass

def threader(b):
    while True:
        worker = q.get()
        scan(worker, str(b))
        q.task_done()











# FEATURES

def PortScanner():
  subprocess.call('cls', shell=True) # clear
  Logo(Fore.YELLOW + "Multi-thread fast port Scanner")


  separator_length = 66
  separator_length_ports = 21

  try:

    print("Enter host to scan: (press Enter for localhost) ")
    hostname = input()

    if (hostname == ""):    # if input was not set, use default - localhost
      hostname = "localhost"
    
    try:
      IP = socket.gethostbyname(hostname)
    except:
      pass


    # OLD GOOD PART 
    print("SCAN PREFERENCES:")
    print("-"*separator_length)

    print((Fore.CYAN+"ip address"+Fore.RESET+'\t-> ').ljust(20) + hostname)
    print((Fore.CYAN+"hostname"+Fore.RESET+'\t-> ').ljust(20) + str(IP))
    print((Fore.CYAN+"tcp timeout"+Fore.RESET+'\t-> ').ljust(20) + str(timeout) + "s")
    print((Fore.CYAN+"threads"+Fore.RESET+'\t\t-> ').ljust(20) + str(threads))
    print((Fore.CYAN+"port range"+Fore.RESET+'\t-> ').ljust(20) + str(start_port) + '-' + str(end_port)) 
    
    print("-"*separator_length)
    print("")


    # to-main external arguments handling --------------------------------------------------------
    if len(sys.argv) == 2 : # checks ammount of arguments given:    0 - program name/path, 1 - host
      hostname = sys.argv[1]
      #sys.exit(1)
    


      
    print(hostname)
    print("-"*separator_length_ports)



    for thread in range(threads):
      t = threading.Thread(target=threader, kwargs={'b':hostname})
      t.daemon = True
      t.start()

    for port in range(start_port, end_port+1):
      q.put(port)

    q.join()

    print("-"*separator_length_ports)
    print("")
  except:
    print("Couldn't resolve IP")
    pass


  print("["+Fore.LIGHTGREEN_EX+">"+Fore.RESET+"] Done")

  os.system("pause")


  
  # reverse check
  #test = socket.gethostbyaddr(IP)
  #print(test)
  ## resolution : ('kubernetes.docker.internal', [], ['127.0.0.1'])

  # exit option

  pass

def Responder():
    subprocess.call('cls', shell=True) # clear
    Logo(Fore.CYAN + "Website and adress list status checker")
    print("")

    separator_length = 79

    site_checklist = {
      "Dragon Services" : "dragon-services.eu",
      "GoldenSand Bank" : "www.goldensandbank.com",
      "Jira" : "jira.dragon-services.eu",
      "NotWorkingTets" : "bullshieturladdress",
      "Google" : "www.google.com",
      "RedHat" : "www.redhat.com"
    }
    
    #header
    print("-"*separator_length)
    print(Fore.CYAN+"STATE".ljust(9) + "NAME".ljust(27) + "HOSTNAME".ljust(30) + "IP" + Fore.RESET)
    print("-"*separator_length)

    for line in site_checklist:
      hostname = site_checklist.get(line)
      state = "["+Fore.RED+"dead"+Fore.RESET+"]"
      ip = ""

      try:
        ip  = socket.gethostbyname(hostname)
        state = "["+Fore.GREEN+"OK"+Fore.RESET+"]".ljust(6)

      except socket.error:
        state = "["+Fore.RED+"NA"+Fore.RESET+"]".ljust(6)
        ip = "can't resolve"
      
      print(state.ljust(9) + line.ljust(24) + "-> " + hostname.ljust(30) + "" +ip)
      # end for

    print("-"*separator_length)  
    print("["+Fore.LIGHTGREEN_EX+">"+Fore.RESET+"] Done")

    os.system("pause")
    
    pass

def NetworkScanner():                           # TODO
  subprocess.call('cls', shell=True)            # clear screen

  print("STATUS: in development")
  os.system("pause")






def ShowMainMenu(show_banner):
  subprocess.call('cls', shell=True)          # clear screen
  if(show_banner):
    Banner()
  Logo("Advanced Network Analysis Toolset")   # show logo
  
                                              # show menu options
  print("""
  PLEASE SELECT OPTION:
  ["""+Fore.RED+"""1"""+Fore.RESET+"""] Port scanner
  ["""+Fore.RED+"""2"""+Fore.RESET+"""] Website responder
  ["""+Fore.RED+"""3"""+Fore.RESET+"""] Network scanner
  ["""+Fore.RED+"""0"""+Fore.RESET+"""] Exit
  """)
  

def Menu(show_banner):
  if(show_banner):
    ShowMainMenu(1)
  else:
    ShowMainMenu(0) 

  choice = 1
  exit_flag = 0
  try:
    while True:
      choice = input()

      if choice == "1":
        PortScanner()
        ShowMainMenu(0)
        continue

      elif choice == "2":
        Responder()
        ShowMainMenu(0)
        continue

      elif choice == "3":
        NetworkScanner()
        ShowMainMenu(0)
        continue

      elif(choice == "0" or choice == "exit" or choice =="quit"):
        print("["+Fore.RED+"*"+Fore.RESET+"] Exiting...\tBye!")
        exit_flag = 1
        sys.exit()
        
      else:
        print("["+Fore.RED+"!"+Fore.RESET+"] No such option!")
        continue
        pass

  except KeyboardInterrupt:
    print("["+Fore.RED+"*"+Fore.RESET+"] Exiting...\tBye!")
    exit_flag = 1
    sys.exit()

  except:
    if exit_flag != 1:
      print("["+Fore.RED+"!"+Fore.RESET+"] An error occured, exiting.")
    sys.exit()
  pass

def main():
  







  try:
    #subprocess.call('cls', shell=True)  # clear output
    #Banner()                            # print banner
    Menu(1)

    


    #print("Please wait, scanning remote host", host)
    #curr_port = 1
    #threads = 100
    #for x in range(1,threads): 
    #  sys.stdout.write("\r Scanning port no. :"+str(curr_port))
    #  sys.stdout.flush()
    # 
    #  
    #
    #  t = threading.Thread(target=portscan,kwargs={'port':curr_port}) 
    #
    #  curr_port += 1     
    #  t.start()
    #
    #t.join() # joins all threads, waits for completion


    #Scanner()


    print("")

    os.system("pause")
    pass

    #start_time = datetime.now()
    try:
      print(" ")
    except KeyboardInterrupt:
      print("["+Fore.RED+"!"+Fore.RESET+"] Keyboard interrupted, ending scan")
      sys.exit()

    except socket.gaierror:
      print("["+Fore.RED+"!"+Fore.RESET+"] Hostname couldn't be resolved")
      sys.exit()

    except socket.error:
      print("["+Fore.RED+"!"+Fore.RESET+"] Couldn't connect to server")
      sys.exit()

  except KeyboardInterrupt:
    print("")
    print("["+Fore.RED+"!"+Fore.RESET+"] Keyboard interrupted, exiting")
    print("Bye!")
    sys.exit()

if __name__== "__main__":   # to run as standalone program instead of reusable module
  main()