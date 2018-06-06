'''Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
Autor:    Ronaldo Daniel da Silva (rds)
Email:    rds@cin.ufpe.br
Data:     06/06/2018
Descrição:  Implementação de Lista Duplamente Encadeada utilizando POO.
Copyright(c) 2018 Ronaldo Daniel da Silva'''

class No:
    def __init__(self,item=None, ante=None ,prox=None):
        self.item = item 
        self.ante = ante 
        self.prox = prox
    
class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
    
    def vazia(self):
        return self.primeiro == self.ultimo

    def pesquisar(self,item):
        if self.vazia():
            return None
        aux = self.primeiro.prox
        while aux != None and aux.item != item:
            aux = aux.prox
        item = aux.item
        return item
    
    def addFinal(self,item):
        novoNo = No(item,self.ultimo,None)
        self.ultimo.prox = novoNo
        self.ultimo = self.ultimo.prox
        
    def addInicio(self,item):
        novoNo = No(item,self.primeiro,self.primeiro.prox)
        self.primeiro.prox = novoNo
        if self.vazia():
            self.ultimo = novoNo
        else:
            novoNo.prox.ante = novoNo    
        
    def remover(self,item):
        if self.vazia():
            return None
        aux = self.primeiro.prox
        while aux != None and aux.item != item:
            aux = aux.prox
        if aux ==  None:
            return None
        elif aux.prox == None:
            item = aux.item
            aux.ante.prox = None
            self.ultimo = aux.ante
            del aux
            return item
        else:
            item = aux.item
            aux.prox.ante = aux.ante
            aux.ante.prox = aux.prox
            del aux
            return item
            
    def removerInicio(self):
        if self.vazia():
            return None
        delNo = self.primeiro.prox #No a ser deletado
        delNo.prox.ante = self.primeiro #Muda a referencia do anterior do proximo no a ser deletado(passa a apontar para o primeiro No)
        self.primeiro.prox = delNo.prox #muda a referencia do proximo do primeiro No(No de cabeca)
        temp = delNo
        del temp
        return delNo.item 
        
    def removerFinal(self):
        if self.vazia():
            return None
        delNo = self.ultimo
        self.ultimo = delNo.ante
        self.ultimo.prox = None
        item = delNo.item
        del delNo
        return item

    def __str__(self):
        aux = self.primeiro.prox
        modelo = '['
        while aux != None:
            modelo += str(aux.item) + ','
            aux = aux.prox
        modelo = modelo.strip(',')
        modelo += ']'
        return modelo
            
    def __repr__(self):
        return self.__str__()
        

        
