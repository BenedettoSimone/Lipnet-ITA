import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'idna==3.3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'imageio==2.16.1'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keras==2.8.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keras-nightly==2.9.0.dev2022031807'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'kiwisolver==1.4.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'libclang==13.0.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib==3.5.1'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'networkx==2.7.1'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy==1.22.3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'oauthlib==3.2.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python==4.5.5.64'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opt-einsum==3.3.0'])