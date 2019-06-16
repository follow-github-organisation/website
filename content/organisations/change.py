import os
import codecs

for d in os.listdir('.'):
	if '.md' not in d and '.py' not in d:
		for f in os.listdir('./{}'.format(d)):
			if 'repo' in f:
				print(f)
				with open('./{}/{}'.format(d, f), 'r') as fl:
					lines = fl.readlines()
				lines.append('\n---')
				if '---' in lines[-2]:
					lines[-2] = lines[-2].replace('---', '')
				with open('./{}/{}'.format(d, f), 'w') as fl:
					fl.write("".join(lines))
