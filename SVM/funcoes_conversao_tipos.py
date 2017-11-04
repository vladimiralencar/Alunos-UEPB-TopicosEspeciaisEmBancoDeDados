
# coding: utf-8

# # Funcoes de conversao tipos - Dataframe

# Converte dados categoricos para inteiros no dataframe
# mantem dicionarios com as conversoes

# ## Normaliza os dados do dataframe
#  aumenta a acurácia do modelo
#  
# valores são transpostos para o intervalo 0-1

# In[9]:


import pandas as pd
# normalize the data attributes
from sklearn import preprocessing
def normalizar_dataframe(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    columns = df.columns
    np_scaled = min_max_scaler.fit_transform(df)
    df_normalized = pd.DataFrame(np_scaled)
    df_normalized.columns = columns
    return df_normalized


# ## Dataset - Cancer

# In[5]:


from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
data.target[[10, 50, 85]]

list(data.target_names)


# 'malignant': 0, 'benign':1

# In[7]:


df = pd.DataFrame(data.data)
df.columns = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
df["class"] = data.target
df.head()


# In[11]:


normalizar_dataframe(df).head()


# ## Dataset Carros

# In[145]:


df = pd.read_csv("car.data")
df.columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "Class"]
df.head()


# In[146]:


# codifica todo o dataframe para numérico
from sklearn.preprocessing import LabelEncoder
def codificar_dataframe(df):
    le = LabelEncoder()
    df2 = df.copy()
    for col in df2.columns.values:
        # Encoding only categorical variables
        #print(len(df2[col]))
        if df2[col].dtypes=='object':
            data=df2[col]
            le.fit(data.values)
            #print (data.values)
            #print(le.fit(data.values))
            df2[col]=le.transform(df2[col])           
            
    # gerar os dicionarios das categorias e dos inteiros
    dict_scalar ={}
    dict_to_string = {}
    d = {}
    columns = df.columns.values.tolist()
    #print(type(columns))
    #print(columns)
    for col in columns:
        #print(col)
        values = list(set(df[col]))
        #print (values)
        le = LabelEncoder()
        vt = le.fit_transform(values)
        #print(le.transform(values))
        dict_scalar[col] = {}
        dict_to_string[col] = {}
        d = {}
        ds = {}
        for v, vt in zip(values, vt): 
            #print (v,vt)
            d[v] = vt
            ds[vt] = v
        dict_scalar[col] = d
        dict_to_string[col] = ds
        
    return(df2, dict_scalar, dict_to_string)


# In[147]:


df.head()


# In[148]:


df2, dict_scalar, dict_to_string = codificar_dataframe(df)
df2.head()


# In[149]:


dict_scalar


# In[150]:


dict_to_string


# In[151]:


dict_to_string["buying"]


# In[152]:


df2.head()


# In[153]:


col = 'buying'
#value = 0
#df['col1'].map(di) 
df2['buying'].map(dict_to_string[col]).head()


# In[154]:


# decodificar o dataframe
def decodificar_dataframe(df2,dict_to_string):
    df3 = pd.DataFrame()
    columns = df2.columns.values.tolist()
    for col in columns:
        df3[col] = df2[col].map(dict_to_string[col])
    return (df3)


# In[155]:


df6 = decodificar_dataframe(df2,dict_to_string)
df6.head()


# In[156]:


df_test = df6.loc[:3,:]
df_test


# In[157]:


dict_scalar


# In[159]:


# codifica os exemplos
def codificar_exemplos(df,dict_to_int):
    df3 = pd.DataFrame()
    columns = df.columns.values.tolist()
    for col in columns:
        df3[col] = df[col].map(dict_to_int[col])
    return (df3)


# In[161]:


dict_to_int = dict_scalar 
df_test_cod = codificar_exemplos(df_test, dict_to_int)
df_test_cod


# In[163]:


# decodifica os exemplos
def decodificar_exemplos(df,dict_to_string):
    df3 = pd.DataFrame()
    columns = df.columns.values.tolist()
    for col in columns:
        df3[col] = df[col].map(dict_to_string[col])
    return (df3)


# In[165]:


decodificar_exemplos(df_test_cod, dict_to_string)

