import os

path = os.getcwd ()
script = os.path.dirname(os.path.realpath(__file__))

print '='*70
print ' '*10 + 'Setup file path: ' + script + ' '*10
print ' '*10 + 'Working Directory: ' + path + ' '*10
print '='*70

try:
   os.system ('sudo mv "' + script + '/brutos" /usr/bin')
   os.system ('sudo chmod +x /usr/bin/brutos')
   os.system ('sudo mv "' + script + '/brutos_files" /usr/bin')
   print 'Installed!'
except:
   print 'Error!'