class Livre:    #class livre

    def __init__(self, Titre, Auteur, Nb_Pages):    #constructeur de class Livre
        try:
            if not isinstance(Nb_Pages, int) or Nb_Pages <= 0:      #====================
                raise ValueError("le nombre des pages doit etre ENTIER POSITIVE") 
            self.Titre = Titre      #Attributs Titre | Auteur 
            self.Auteur = Auteur
            self.Nb_Pages = Nb_Pages
        except ValueError as e:  #-----except an error 
            print(f"Erreur de type : {e}")
        else:
             ("Le neauvou livre ajouté ave c succes !")
        finally:    #----Finally
            print(f"le titre de livre {self.Titre}, l' auteur {self.Auteur}, et le Nombre des pages {self.Nb_Pages}")



class Bibliotheque:     #class Bibliothéque
    
    def __init__(self):     #constructeur de Bibliothéque
        self.Livres = [] 

    def AjouterLivre(self, livre_A):     #fonction de l' Ajoute de Livre
        try:
            if not isinstance(livre_A, Livre):
                raise TypeError(f"Livre pas contient d'instance !")
            self.Livres.append(livre_A)
        except TypeError as e:  #----except an error
            print(f"Erreur de type : {e}")
        else:
            ("Le livre etait ajouté avec succes.")
        finally:
            print("fin de l'opération de l' Ajoute.")


    def SupprimerLivre(self, Titre):   #fonction de supprission 
        try:    
            Livre_S = None
            for Livre in self.Livres:
                if Livre[Titre] == Livre_S:
                    Livre_S = Livre
                    break
            if Livre_S is None:
                raise KeyError("Ce titre n'est exist pas !")
            self.Livres.remove(Livre_S)
        except KeyError as e:
            print(f"Erreur lors de la supprission : {e}")
        finally:
            print("fin de l'opération de la supprission")


#======= instanciation ========#

livre = Livre("Arabe", "Ahmed", 200)

livre = Bibliotheque()
livre.AjouterLivre("Francais")
livre.SupprimerLivre("Mathematique")
