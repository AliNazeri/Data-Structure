from implementation import *
from reader import reader_fun,get_ssuspect,df_faz1
#from gui import TestApp
this_graph = Graph_Abstract()
print("فاز یک")
reader_fun(this_graph)
df_faz1=df_faz1(this_graph)
print(df_faz1)




print("فاز دو")
this_graph.Faze2()
df=get_ssuspect(this_graph)

print(df)
print("فاز سه")
this_graph.Faze3()
df=get_ssuspect(this_graph)
print(df)
print("فاز چهار")
this_graph.Faze4()
df=get_ssuspect(this_graph)
print(df)