import pyvisa, time
rm = pyvisa.ResourceManager()       # sans '@py' car on uutlise NI-VISA
ID=rm.list_resources()
print(ID)



# ici je commente car je prends l'ID d'une liste
generator = rm.open_resource(ID[0])  # ouvrir le premier instrument de la liste

generator.timeout = 10000  # definir le timeout a 5000 ms
generator.read_termination = '\n'  # definir le caractere de fin de lecture
generator.write_termination = '\n'  # definir le caractere de fin d'ecriture
generator.chunk_size = 102400  # definir la taille du buffer
generator.clear()  # vider les buffers de l'instrument

generator.write("OUT ON")  # activation ch1
time.sleep(10)  # attendre 10 s
print("je viens de lire CH1")
# print("Etat CH1 :", generator.query("OUT?"))  # envoyer la commande OUT? et afficher la reponse



generator.write("OUT OFF")  # desactivation ch1
time.sleep(10)  # attendre 10 s
print("je viens de fermer CH1")
#print("Etat CH1 :", generator.query("OUT?"))  # envoyer la commande OUT? et afficher la reponse



generator.close()  # fermer l'instrument
rm.close()  # fermer le gestionnaire de ressources
