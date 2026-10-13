import subprocess

out = subprocess.check_output(['git', 'log', '--oneline', '-n', '20'], text=True, encoding='utf-8')
print(out)
