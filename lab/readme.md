# Pilotage Générateur & Oscilloscope Rigol

### Python · PyVISA · Mode OFFLINE / ONLINE

Ce projet est structuré en blocs indépendants afin de piloter un générateur et un oscilloscope Rigol de manière robuste, lisible et examen-proof, aussi bien au labo que hors connexion matérielle.

---

### Structure générale du projet

| Bloc         | Rôle                                               |
| ------------ | -------------------------------------------------- |
| Bloc OFFLINE | Exécution sans instruments (mode démonstration)    |
| Bloc 1       | Détection des instruments (VISA IDs)               |
| Bloc 2       | Prise en main complète du générateur               |
| Bloc 3       | Oscilloscope (mesures, waveform, sweep, slew rate) |
| Bloc final   | Fermeture propre des instruments                   |

Ce README documente Bloc OFFLINE, Bloc 1 et Bloc 2.

---

### BLOC OFFLINE — Mode démonstration (sans instruments)

#### Objectif

- Tester tout le code sans générateur ni oscilloscope

- Vérifier les commandes SCPI envoyées

- Éviter toute dépendance matérielle hors labo

---

#### principe

- Un flag OFFLINE
- Une classe FakeInstrument
- Les méthodes write, query, read_raw sont simulées

```python
OFFLINE = True   # Hors labo
OFFLINE = False  # Au labo
```
Aucune autre modification n’est nécessaire.

---

#### Fonctionnement du FakeInstrument

- write(cmd) → affiche la commande SCPI
- query(cmd) → renvoie des valeurs plausibles
- read_raw() → renvoie une waveform binaire simulée

ous les blocs (générateur, oscillo, calculs) peuvent s’exécuter sans erreur.

---

## Explication 

J’ai prévu un mode offline pour tester et valider le code sans dépendre du matériel.

---

# Bloc 1

### Objectif

- Identifier les instruments connectés via VISA

- Récupérer les IDs

- Éviter l’ouverture d’un mauvais port

---

### Fonctionnement

- Utilisation de rm.list_resources()

- Affichage de toutes les ressources avec un index

- Sélection manuelle de l’index du générateur et de l’oscilloscope

---

### Points importants

- USB0::... → instrument USB (Rigol classique)

- ASRLx::INSTR → port série (COM)

---

### Résultat

Le bloc fournit deux variables :

```text
GEN_ID   = ...
SCOPE_ID = ...
```
Ces IDs sont ensuite copiés manuellement dans les blocs suivants.

---

### Explication: 

Je commence par identifier les ressources VISA disponibles, sans ouvrir les instruments.

---

# Bloc 2 : Générateur Rigol (prise en main complète)

### Objectif

- Piloter le générateur Rigol via commandes SCPI

- Générer tous les signaux demandés à l’examen

- Garder le générateur ouvert pendant toute la manipulation

---

### Ouverture du générateur

- L’ID est collé manuellement depuis le Bloc 1

- Ouverture sécurisée avec try/except

- Compatible OFFLINE et ONLINE

---

### Fonctions disponibles

#### Signaux sur CH1

- Sinus

- Carré

- Rampe (triangle)

- Réglage fréquence, amplitude (Vpp), offset et phase

```pyton
ch1_sine(freq, vpp, offset, phase)
ch1_square(freq, vpp, offset, phase)
ch1_ramp(freq, vpp, offset, phase)
```

---

#### Canal CH2 (optionnel)

- Disponible si nécessaire

- Entièrement commentable à l’examen

```python
ch2_ramp(freq, vpp, offset, phase)
```

---

#### Sweep (balayage interne Rigol)

```python
ch1_linear_sweep_sine(f_start, f_stop, sweep_time)
```
---

#### Burst 
```python
ch1_burst_square(ncycles, burst_period)
```
---

### Exemples prêts à l'emploi 
Une section “EXEMPLES PRÊTS” permet de :

- décommenter une seule ligne

- générer immédiatement le signal souhaité

Aucun code n’est à réécrire pendant l’examen.

---
### Explication

Le générateur est ouvert une seule fois. Ensuite, je sélectionne le signal voulu via des fonctions SCPI conformes à la documentation Rigol.

---