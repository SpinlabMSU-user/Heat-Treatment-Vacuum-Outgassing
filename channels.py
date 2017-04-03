import matplotlib.pylab as plt
t = []
h2 = []
h2o = []
n2 = []
co2 = []
oil = []

readfile = open('/Users/jakehuneau/Documents/school/MSU/work/Channels/channels2.txt','r')
sepfile = readfile.read().split('\r')
readfile.close()

for plotpair in sepfile:
        channels = plotpair.split('\t')
        t.append(float(channels[0]))
        h2.append(float(channels[1]))
        h2o.append(float(channels[2]))
        n2.append(float(channels[3]))
        co2.append(float(channels[4]))
        oil.append(float(channels[5]))
        
plt.plot(t, h2)
plt.title('H2')
plt.xlabel('time')
plt.ylabel('pressure (torr)')
plt.legend('h2')

plt.plot(t, h2o)
plt.title('H2O')
plt.xlabel('time')
plt.ylabel('pressure (torr)')
plt.legend('h2o')

plt.plot(t, n2)
plt.title('N2')
plt.xlabel('time')
plt.ylabel('pressure (torr)')
plt.legend('n2')

plt.plot(t, co2)
plt.title('CO2')
plt.xlabel('time')
plt.ylabel('pressure (torr)')

plt.plot(t, oil)
plt.title('OIL')
plt.xlabel('time')
plt.ylabel('pressure (torr)')

plt.title('all gases')