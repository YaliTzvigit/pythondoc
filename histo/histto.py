

# Definir des valeurs aleatoires:  

import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 250)


print(x)

# Creer l'histogramme 

y = numpy.random.uniform(0.0, 6.0, 100)

plt.hist(y, 6)

# Afficher l'histo :

plt.show()

