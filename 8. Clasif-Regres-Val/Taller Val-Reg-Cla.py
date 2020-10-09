#!/usr/bin/env python
# coding: utf-8

# In[14]:


# PROCESAMIENTO DIGITAL
# Se importan las librería numpy y las funciones de preprocesamiento
#Editado por: Alejandro Rios
import numpy as np 
from sklearn import preprocessing
# Datos de prueba
input_data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5], [5.3, -2.9, -6.2]])
print(input_data)


# In[15]:


# Binarizar los datos
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data) 
print("\nDatos binarizados:\n", data_binarized)


# In[16]:


# Imprimir la media y la desviación estándar
print("\nANTES:") 
print("Media =", input_data.mean(axis=0))
print("Desviación estándar =", input_data.std(axis=0))


# In[17]:


# Remover la media
data_scaled = preprocessing.scale(input_data) 
print("\nDESPUÉS:")
print("Media =", data_scaled.mean(axis=0)) 
print("Desviación estándar =",
data_scaled.std(axis=0))


# In[18]:


# Escalamiento Min Max
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max escalamiento de datos:\n", data_scaled_minmax)


# In[19]:


# Normalización de datos
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 dato normalizado:\n", data_normalized_l1) 
print("\nL2 dato normalizado:\n", data_normalized_l2)


# In[21]:


# Manejo de etiquetas
import numpy as np 
from sklearn import preprocessing
# Se definen algunas etiquetas simples 
input_labels = ['up', 'down', 'right', 'left', 'back', 'foward', 'ok']
# Se crea un codificador de etiquetas y se ajustan las etiquetas 
encoder = preprocessing.LabelEncoder() 
encoder.fit(input_labels)
# Se imprime el mapeo entre palabras y números print("\nMapeo de etiquetas:") 
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)
# Codificar un conjunto de etiquetas con el codificador 
test_labels = ['down', 'right', 'up'] 
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels) 
print("Encoded values =", list(encoded_values))
# Decodificar un conjunto de valores usando el codificador 
encoded_values = [3, 0, 4, 1] 
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values) 
print("Decoded labels =", list(decoded_list))

