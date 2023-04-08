import os , platform , socket
from datetime import date

root_folders = os.listdir('/') 

def final():
    with open(f'result-{date.today().strftime("%m-%d-%Y")}.txt', 'w') as txt:
        txt.write('MADE WITH <3 BY LUKKSHH ~ https://lukkshh.ga\n')
        
        txt.write('\n')
        txt.write('~~~~~ SYSTEM INFO ~~~~~')
        txt.write('\n')

        txt.write(f"\nOS: {platform.system()}")
        txt.write(f"\nOS NAME: {platform.node()}")
        txt.write(f"\nVersion: {platform.version()}")
        txt.write(f"\nIPv4 Address: {socket.gethostbyname(socket.gethostname())}")
        txt.write(f"\nArchitecture: {platform.architecture()}")
        txt.write(f"\nProcessor: {platform.processor()}")

        txt.write('\n')
        txt.write('\n~~~~~ SYSTEM INFO ENDING ~~~~~')
        
        
        txt.write('\n')
        txt.write('\n~~~~~ ALL FOLDER IN ROOT DIRECTORY ~~~~~')
        txt.write('\n')
        for folder in root_folders:
            txt.write('\n'+ folder)
        txt.write('\n')
        txt.write('\n~~~~~ ALL FOLDER IN ROOT DIRECTORY ENDING ~~~~~')
        txt.write('\n')
final()