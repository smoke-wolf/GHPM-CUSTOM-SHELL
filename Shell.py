import cmd
import os
import subprocess

# Number of times to go up in the directory structure
levels_to_go_up = 6  # Change this to the desired number of levels

# Perform multiple "cd .." operations
for _ in range(levels_to_go_up):
    os.chdir('..')
print('\n'*200)


class MyShell(cmd.Cmd):
    intro = '''========================================
    ┓ ┏  ┓                  
┃┃┃┏┓┃┏┏┓┏┳┓┏┓  ╋┏┓     
┗┻┛┗ ┗┗┗┛┛┗┗┗   ┗┗┛     
┳┓   ┓ ┏┓   •   •    ┓  
┣┫┏┓┏┣┓┃┃┏┓╋┓┏┳┓┓┓┏┓┏┫  
┻┛┗┻┛┛┗┗┛┣┛┗┗┛┗┗┗┗┗ ┗┻  
┏┓┓   ┓┓ ┛              
┗┓┣┓┏┓┃┃                
┗┛┛┗┗ ┗┗                
========================================
. Type 'help' for a list of commands.'''
    prompt = "anonymous <powered by gh>$ "
    def default(self, line):
        """Execute shell commands."""
        try:
            output = subprocess.check_output(line, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def do_exit(self, arg):
        """Exit the shell."""
        print("Goodbye!")
        return True

    def do_ip(self, arg):
        """ip
        """
        import requests

        # Use a public API to get your public IP address
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()

        public_ip = data["ip"]

        print(f"Public IP Address: {public_ip}")
    def do_exit(self, arg):
        """Exit the shell."""
        print("Goodbye!")
    def do_clear(self, arg):
        """Exit the shell."""
        print("\n"*250)

    def do_cd(self, arg):
        """cd shell."""
        os.system(f'{os.getcwd()}/{arg}')
    def do_lis(self, arg):
        """mask links with link shield"""
        print(f'=============================link-shield=============================')
        module = 'https://github.com/smoke-wolf/LinkShield.git'
        print('when shown a list, select option (1)')
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        nvum = input('enter the value corresponding to "LinkShield": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================link-shield-end=============================')

    def do_tk(self, arg):
        """Use ToolKit"""
        print(f'=============================link-shield=============================')
        module = 'https://github.com/smoke-wolf/ToolKit.git'
        print('when shown a list, select option (1)')
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        nvum = input('enter the value corresponding to "ToolKit": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================link-shield-end=============================')

    def do_ts(self, arg):
        """optimize with TouchScript"""
        print(f'=============================TouchScript=============================')
        module = 'https://github.com/smoke-wolf/TouchScript.git'
        print('when shown a list, select option (1)')
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        nvum = input('enter the value corresponding to "TouchScript": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================TouchScript=============================')

    def do_bt(self, arg):
        """optimize with BlackTi"""
        print(f'=============================TouchScript=============================')
        module = 'https://github.com/smoke-wolf/BlackTip.git'
        print('when shown a list, select option (1)')
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        nvum = input('enter the value corresponding to "BlackTip": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================TouchScript=============================')


    def do_zph(self, arg):
        """easy mac zphisher implementation"""
        print(f'=============================zphisher=============================')
        module = 'https://github.com/htr-tech/zphisher.git'
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        print('''
                   ====
                   IF you're on mac, open a new instance of this tool, and once you've set your fishing site to localhost
                   use this tool to then forward it to the internet with 'push local port'. then use LinkShield to mask your
                   phishing link.
                   ====
                   ''')
        nvum = input('enter the value corresponding to "zphisher": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================zphisher-end=============================')

    def do_locator(self, arg):
        """Locate Targets With GeoPrecision"""
        print(f'=============================LOCATE=============================')
        print('enter the value corresponding to locator.sh": ')
        module = 'https://github.com/yuhisern7/locator.git'
        os.system(f'python3 gh.py -I {module}')
        os.system('python3 gh.py -LG')
        print('''
                                ====
                                IF you're on mac, open a new instance of this tool,
                                and once you've set up your phishing site,
                                use LinkShield to mask your phishing link.
                                ====
                                ''')
        nvum = input('enter the value corresponding to locator.sh": ')
        os.system(f'python3 gh.py -LG {nvum}')
        print(f'=============================LOCATE-END=============================')



    def do_version(self, arg):
        """Exit the shell."""
        print('''
version v1.0.0
developer: maliq barnard
        ''')



if __name__ == '__main__':
    MyShell().cmdloop()
