import requests
import matplotlib.pyplot as plt #per grafici

sito = 'http://www.google.com'
r = requests.get(sito)
#print(r.status_code)


#tempo di risposta del server
for _ in range(10): #non interessa l'indice del ciclo
    r = requests.get(sito)
    #print('Tempo di Risposta: ', r.elapsed.microseconds/1000, 'ms')
    
    

#media,max,min
tempi_ms = []
num_ciclo = 10

for _ in range(num_ciclo):
    r = requests.get(sito)
    tempi_ms.append(r.elapsed.microseconds/1000)

#print('Tempo minimo MIN', min(tempi_ms), 'ms')
#print('Tempo medio AVG', sum(tempi_ms)/len(tempi_ms), 'ms')
#print('Tempo massimo MAX', max(tempi_ms), 'ms')


#grafici
plt.figure() #spazio predefinito del grafico
plt.plot(tempi_ms) #aggiunge lista dei tempi_ms al grafico e li distribuisce
plt.ylim([0,1.1*max(tempi_ms)]) #per vedere chiaro tutto quanto partendo da un valore y di 0 anzichè del minimo dei miei valori
plt.show() #mostra il grafico