#criação de um método abstrato
from abc import ABC, abstractmethod

class ItemCardapio(ABC):

  def __init__(self,nome, preco):
      self.nome = nome
      self._preco = preco
     #Alocação do método abstrato
      @abstractmethod
      def aplicar_desconto(self):
        pass





