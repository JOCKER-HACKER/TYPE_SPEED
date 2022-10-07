#Version 1.0
import random
import time
from colorama import Fore, Back, Style,init
import pyfiglet
from tqdm import tqdm
from time import sleep
import webbrowser
import os
os.system('clear')
##############################
banner = pyfiglet.figlet_format(''+"TYPE_SPEED" , font = "slant" ) #only 10
print(Fore.LIGHTCYAN_EX+banner)
##############################
print(
'        ' +Fore.LIGHTCYAN_EX+ '+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+' +
'              ' +'     '+Fore.LIGHTYELLOW_EX+'|M|A|D|E| ' +Fore.LIGHTMAGENTA_EX+'|B|Y| '+Fore.LIGHTCYAN_EX+'|J|O|C|K|E|R|' , Fore.LIGHTRED_EX+'|W|I|T|H| ',Fore.LIGHTCYAN_EX+'|❤️|' + '                   ' + '+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
)
##############################
print()
try:
    user =int(input (
'    ' + Fore.LIGHTGREEN_EX+'[1]'+Fore.LIGHTRED_EX+'START' + '                                                        ' +
Fore.LIGHTGREEN_EX+'[2]'+Fore.LIGHTRED_EX+  'OUR OTHER TOOLS' +  '                                              ' +
Fore.LIGHTGREEN_EX+'[3]'+Fore.LIGHTRED_EX+'EXIT' + '    '+Fore.LIGHTYELLOW_EX
))
except Exception as s:
    print()
    print('  '+'INVALID OPR...')
    exit()
print()

if user ==1:
#[STEP 1ST ]text files
    with open('../TEXT/p1.txt' , 'r') as f:
        t1 = f.read()    
    with open('../TEXT/p2.txt' , 'r') as f:
        t2 = f.read()    
    with open('../TEXT/p3.txt' , 'r') as f:
        t3 = f.read()    
    with open('../TEXT/p4.txt' , 'r') as f:
        t4 = f.read()    
    with open('../TEXT/p5.txt' , 'r') as f:
        t5 = f.read()
    with open('../TEXT/p6.txt' , 'r') as f:
        t6 = f.read()
    with open('../TEXT/p7.txt' , 'r') as f:
        t7 = f.read()
    with open('../TEXT/p8.txt' , 'r') as f:
        t8 = f.read()    
    with open('../TEXT/p9.txt' , 'r') as f:
        t9 = f.read()    
    with open('../TEXT/p10.txt' , 'r') as f:
        t10= f.read()    
    with open('../TEXT/p11.txt' , 'r') as f:
        t11 = f.read()    
    with open('../TEXT/p12.txt' , 'r') as f:
        t12 = f.read()
    with open('../TEXT/p13.txt' , 'r') as f:
        t13 = f.read()
    with open('../TEXT/p14.txt' , 'r') as f:
        t14= f.read()
    with open('../TEXT/p15.txt' , 'r') as f:
        t15= f.read()    
    with open('../TEXT/p16.txt' , 'r') as f:
        t16 = f.read()    
    with open('../TEXT/p17.txt' , 'r') as f:
        t17 = f.read()
    with open('../TEXT/p18.txt' , 'r') as f:
        t18 = f.read()
    with open('../TEXT/p19.txt' , 'r') as f:
        t19 =  f.read()          
    with open('../TEXT/p20.txt' , 'r') as f:
        t20 =  f.read()              

    r = (t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20)
    r2 = (t5)
    r = random.choice(r)
    n = len(r)

    print(Fore.LIGHTGREEN_EX+ r)
              
    def GrossWPM(t1,t2,user_input): #done
        t = t2-t1
        le = len(user_input)
        tot1 = le
        tot2 = tot1/t
        tot3 = tot2
        tot4 = tot3
        tot5 = round(tot4)
        tot6 = tot5
        return tot6
        
 
    def GrossWPM2(t1,t2,user_input):#don
        t = t2-t1
        speed1 = len(user_input)
        speed2 = speed1
        speed3 = speed2/t
        speed4 = speed3
        speed5 = round(speed4)
        speed6 = speed5
        speed7 = speed6*60
        speed8 = speed7
        speed9 = speed8

        
        return speed9
    
      
        

    def nwpm(t1,t2,user_input): #done
        t = t2-t1
        x = len(user_input)
        y = wrong(r,input)
        nwpm = x-y
        nwp = nwpm
        nwp2 = nwp/t
        nwp3 = nwp2      
        nwp4 = nwp3
        nwp5 = nwp4*60
        nwp6 = nwp5
        nwp7 = round(nwp6)
        nwp8 = nwp7
        
        o = 0
        if nwp8 > 0:    
            return nwp8
        else:
            return o
            
    def nwpm2(): #done2
        x = nwpm(time_1,time_2,input)
        x2 = x
        x3 = x2*60
       # y = x3*60
        y = x3
        y2 = round(y)
        y3 = y2
       
        o = 0
        if y3 > 0:    
            return y3
        else:
            return o
                  
    def mistake(text,user_input):
        error = 0
        p=0   
        for i in range(len(text)):
            try:
                if text[i] != user_input[i]:
                    error = error+1 
            except:
                error = error+1
        return error    
  
    def accurcy(text,user_input):
        error2 = 0
        right = 0
        totall = len(input)
        for i in range(len(text)):
            try:
                if text[i] != user_input[i]:
                    error2  = error2+1 
                else:
                    right = right+1        
            except Exception as s:
                     error2  = error2+1
        try:
            final = right/totall*100 
        except Exception as s:
            final = 0
        return round(final)
    
    def right(text,user_input):
            error3 = 0
            right2 = 0
            p2 = 0
            for i in range(len(text)):
                try:
                    if text[i] != user_input[i]:
                        error3 = error3+1 
                    else:
                        right2 = right2+1 
                except Exception as s:
                         p2 = p2+1     
            return right2 
        
    def wrong(text,user_input):
            error3 = 0
            right2 = 0
            for i in range(len(input)):
                try:
                    if text[i] != user_input[i]:
                        error3 = error3+1 
                    else:
                           right2 = right2+1 
                except Exception as s:
                         error3 = error3+1
            return error3    
             
    def WPM(n2,time_1,time_2):
        t = time_2-time_1
        x = n2/5
        x2 = x
        y = x2/t
        y2 = y
        y3 = round(y2)
        y4 = y3
        o = 0
        if y2 > 0:
            return y4
        else:
            return o   
    
    def WPM2():
        x = WPM(n2,time_1,time_2)
        x2 = x
        y = x2*60
        y2 = y
        o = 0
        if y2 > 0:
            return y2
        else:
            return o   
  
      
    print(Fore.LIGHTMAGENTA_EX + ' ' )   
    input1 = str(input('PRESS SHIFT KEY '+   Fore.LIGHTCYAN_EX + '⏎ ' + Fore.               LIGHTMAGENTA_EX + 'TO START: '))
    print()
    time_1 = time.time() 
    input = str(input(Style.BRIGHT+'Enter the text: ' + Fore.LIGHTYELLOW_EX + ' ' ))
    time_2 = time.time() 
    print()
    n2 = len(input)
      
    print()
    print(' '+Fore.LIGHTYELLOW_EX+'PROCCESING...') ##############################
    print(' '+Fore.LIGHTGREEN_EX+'')
    for i  in tqdm(range(0,5), ncols = 80,
desc ="PROCESSING"):
            sleep(.1)
    print()
    print(' '+Fore.LIGHTYELLOW_EX+'PROCCESING SUCCESFULL')
    print()
    print(' '+Fore.LIGHTCYAN_EX+'PROCCES[1]COMPLETED')

    print()
##############################
    print(' '+Fore.LIGHTRED_EX+'')
    for i  in tqdm(range(0,25), ncols = 80,
desc ="PROCESSING"):
            sleep(.1)
    print()
    print(' '+Fore.LIGHTYELLOW_EX+'PROCCESING SUCCESFULL')
    print()
    print(' '+Fore.LIGHTCYAN_EX+'PROCCES[2]COMPLETED')
    print()
##############################
    print(' '+Fore.LIGHTCYAN_EX+'')
    for i  in tqdm(range(0, 20), ncols = 80,
desc ="PROCCESING"):
            sleep(.1)
    print()
    print(' '+Fore.LIGHTYELLOW_EX+'PROCCESING SUCCESFULL')
    print()
    print(' '+Fore.LIGHTCYAN_EX+'PROCESS[3]COMPLETED')
#############################
    print(' '+Fore.LIGHTCYAN_EX+'')
    print()
    for i in tqdm(range(0, 50), total = 50, 
desc ="PROCCESING"):
        sleep(.1)
    print()
    print(' '+Fore.LIGHTYELLOW_EX+'PROCCESING SUCCESFULL')
    print()  
   
    print(' '+Fore.LIGHTCYAN_EX+'PROCESS[3]COMPLETED')
    print()
    print()
    
   
############################## 
    print('_________________________________',end='')
    print('__________________________')
    print()
    print(Fore.LIGHTCYAN_EX , Style.BRIGHT+'RAW-SPEED: ' ,WPM(n2,time_1,time_2), "w/s" , WPM2() , "w/m")
    print('_________________________________',end='')
    print('__________________________')
    print()


    print(Fore.LIGHTYELLOW_EX  + ' ' + 'ACCURCY: ' ,str(accurcy(r,input))   +  "%" )
    print('_________________________________',end='')
    print('__________________________')
    print()

    print(Fore.LIGHTRED_EX  + ' ' + 'TOTALL ERROR: ' , mistake(r,input)
)
    print('_________________________________',end='')
    print('__________________________')
    print()
    
    print(Fore.LIGHTCYAN_EX  + ' ' +
f'TOTALL ENTRIES: {n2} ')
   
    print('_________________________________',end='')
    print('__________________________')
    print()  
    print(Fore.LIGHTGREEN_EX  + ' ' + 'CORRECT ENTRIES: ' , right(r,input) )
    
    
    print('_________________________________',end='')
    print('__________________________')
   
    print()
    print(Fore.LIGHTRED_EX  + ' ' + 'INCORRECT ENTRIES: ' , wrong(r,input) )
  
    print('_________________________________',end='')
    print('__________________________')
    
    print()
    print(Fore.LIGHTCYAN_EX  + ' ' + 'KEY-SPEED: ' ,nwpm(time_1,time_2,input) ,  "k/m")
    
    print('_________________________________',end='')
    print('__________________________')  
    print()
    
    print(Fore.LIGHTMAGENTA_EX  + ' ' + 'TOTALL TIME: ' ,round(time_2 - time_1),'(s)')
    print('_________________________________',end='')
    print('__________________________')
   
    print(' '+Fore.LIGHTGREEN_EX+' ')
 

elif user ==2:
    webbrowser.open('https://github.com/JOCKER-HACKER')
    print('  '+Fore.LIGHTYELLOW_EX+'OUR GITHUB PAGE LINK:-')
    print('  '+Fore.LIGHTGREEN_EX+'https://github.com/JOCKER-HACKER')
    print()
elif user ==3:
    print(' '+Fore.LIGHTRED_EX+"THANKS FOR USING THE TOOL")
    print()
    exit()

else:
    print(' '+Fore.LIGHTGREEN_EX+'INVALID OPR...')
##############################
