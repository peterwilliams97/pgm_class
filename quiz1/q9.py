from __future__ import division

Ppresident = [0.99, 0.01]
Paccident = [0.9, 0.1]

Ptraffic = {}
Ptraffic[0,0] = 0.1
Ptraffic[0,1] = 0.5
Ptraffic[1,0] = 0.9
Ptraffic[1,1] = 0.9

# P(accident=1,traffic=1)
Pat = Paccident[1] * sum([Ptraffic[p,1] for p in (0,1)])

# P(traffic=1)
Ptraff1 = sum([Ptraffic[(p,a)]*Ppresident[p]*Paccident[a] for a in (0,1) for p in (0,1)])
Ptraff0 = sum([(1.0-Ptraffic[(p,a)])*Ppresident[p]*Paccident[a] for a in (0,1) for p in (0,1)])
Ptraff = Ptraff1/(Ptraff0+Ptraff1)

# P(accident=1 | traffic = 1)
Pa_t = Pat/Ptraff

print 'Pat    = %f' % Pat
print 'Ptraff tot = %f' % (Ptraff0+Ptraff1)
print 'Ptraff = %f' % Ptraff
print 'Pa_t   = %f' % Pa_t