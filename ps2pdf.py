import os,sys
for d,dirs,files in os.walk('.'):
    for f in files:
        if not f.endswith('.PS'):
            continue
        pdf = os.path.splitext(f.lower())[0]
        
        ps  = d + os.sep + f
        pdf = d + os.sep + pdf + '.pdf'
        cmd = "ps2pdf14 '%s'  '%s'" % ( ps,pdf)
        errno=os.system(cmd)
        if errno:
            print >>sys.stderr,"error for ",cmd
