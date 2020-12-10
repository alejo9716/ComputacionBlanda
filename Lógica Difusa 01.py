#!/usr/bin/env python
# coding: utf-8

# In[62]:


#Función de Membresía Trgiangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define un array x para el manejo del factor calidad en un restaurante
x = np.arange(0, 11, 1)

#Se define un array para la función miembre de tipo triangular
calidad = sk.trimf(x, [0, 0, 0])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[63]:


#Función de Membresía Trgiangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define un array x para el manejo del factor calidad en un restaurante
x = np.arange(0, 11, 1)

#Se define un array para la función miembre de tipo triangular
calidad = sk.trimf(x, [0, 0, 5])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[64]:


#Función de Membresía Trgiangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define un array x para el manejo del factor calidad en un restaurante
x = np.arange(0, 11, 1)

#Se define un array para la función miembre de tipo triangular
calidad = sk.trimf(x, [0, 5, 10])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[65]:


#Función de Membresía Trgiangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define un array x para el manejo del factor calidad en un restaurante
x = np.arange(0, 11, 1)

#Se define un array para la función miembre de tipo triangular
calidad = sk.trimf(x, [9, 9, 10])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[66]:


#Función de Membresía Trgiangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define un array x para el manejo del factor calidad en un restaurante
x = np.arange(0, 11, 1)

#Se define un array para la función miembre de tipo triangular
calidad = sk.trimf(x, [10, 10, 10])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[67]:


#Función de Membresía Trapezoidal

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define la variable independiente
x = np.arange(0, 11, 1)

#Se define la variable dependiente trapezoidal de membresía
vd_trapezoidal = sk.trapmf(x, [0, 0, 5, 5])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[68]:


#Función de Membresía Trapezoidal

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define la variable independiente
x = np.arange(0, 11, 1)

#Se define la variable dependiente trapezoidal de membresía
vd_trapezoidal = sk.trapmf(x, [0, 3, 5, 8])

#Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[69]:


#Función de Membresía Gausssiana

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define la variable independiente
x = np.arange(0, 11, 0.1)

#Se define la variable dependiente gaussiana de membresía
vd_guassiana = sk.gaussmf(x, np.mean(x), np.std(x))

#Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_guassiana, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[70]:


#Función de Membresía Gaussiana BELL

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define la variable independiente
x = np.arange(0, 11, 0.6)

#Se define la variable dependiente gaussiana de membresía
vd_guassiana_bell = sk.gbellmf(x, 2, 3, 5)

#Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_guassiana_bell, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[71]:


#Función de Membresía sigmoide
import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Se define la variable independiente
x = np.arange(-11, 11, 1)

#Se define la variable dependiente sigmoide de membresía
vd_sigmoide = sk.sigmf(x, 0, 1)

#Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_sigmoide, 'b', linewidth=1.5, label='servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[72]:


#Paquetes requeridos
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Definiendo los rangos de velocidad de 0 a 80
x = np.arange(30, 80, 0.1)

#Definiendo las funciones miembro triangulares
lento = fuzz.trimf(x, [30, 30, 50])
medio = fuzz.trimf(x, [30, 50, 70])
medio_rapido = fuzz.trimf(x, [50, 60, 80])
rapido = fuzz.trimf(x, [60, 80, 80])

#Dibujando las funciones de membresía
plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='Rapido')
plt.plot(x, medio_rapido, 'k', linewidth=1.5, label='Medio-Rapido')
plt.plot(x, medio, 'm', linewidth=1.5, label='Medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='Lento')
plt.title('Penalti difuso')
plt.ylabel('Membresía')
plt.xlabel('Velocidad (K/H)')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)


# In[83]:


#Union
import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#Definición de arreglo para calidad
x = np.arange(0, 11, 1)

#Definiendo funciones triagulares
bajo = sk.trimf(x, [0, 0, 5])
medio = sk.trimf(x, [0,5,10])

#Graficación
plt.figure()
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'r', linewidth=1.5, label='Medio')

#Dibujando las funciones de membresía
plt.title('Fución Unión (Máximo)')
plt.ylabel('Membresía')
plt.xlabel('Velocidad (K/H)')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.axvline(x=0, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=1, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=2, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=3, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=4, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=5, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=6, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=7, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=8, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=9, ymin=0, ymax=10, color='g', linestyle='-.')
plt.axvline(x=10, ymin=0, ymax=10, color='g', linestyle='-.')

plt.plot(0, 1, marker='o', markersize=10, color='g')
plt.plot(1, 0.8, marker='o', markersize=10, color='g')
plt.plot(2, 0.6, marker='o', markersize=10, color='g')
plt.plot(3, 0.6, marker='o', markersize=10, color='g')
plt.plot(4, 0.8, marker='o', markersize=10, color='g')
plt.plot(5, 1, marker='o', markersize=10, color='g')

plt.plot(6, 0.8, marker='o', markersize=10, color='g')
plt.plot(7, 0.6, marker='o', markersize=10, color='g')
plt.plot(8, 0.4, marker='o', markersize=10, color='g')
plt.plot(9, 0.2, marker='o', markersize=10, color='g')
plt.plot(10, 0, marker='o', markersize=10, color='g')

plt.show()

#Econtrando el máximo (Fuzzy OR)
sk.fuzzy_or(x, bajo, x, medio)


# In[ ]:




