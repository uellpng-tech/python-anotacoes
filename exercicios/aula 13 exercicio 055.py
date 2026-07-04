m = 0
me = 0
for p in range (1,6):
    p = float (input('peso da {} pessoa '.format(p)))
    if p == 1:
        m = p
        me = p
    else:
        if p > m:
            m = p
        if p < me:
            me = p
print ('maior {}'.format(m))
print ('menor {}'.format(me))