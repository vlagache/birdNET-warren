# birdNET-warren

Documentation BirdNET: https://birdnet-team.github.io/BirdNET-Analyzer/  
Commandes CLI BirdNET : https://birdnet-team.github.io/BirdNET-Analyzer/usage.html

## Commandes

---

### Générer la liste des espèces

Génère un fichier `species_list.txt` utilisable comme filtre dans `detect_birds/config.toml` (`slist`).
Il faut ensuite enlever les noms des espèces que l'on ne souhaite pas détecter du fichier.

**Bordeaux** — espèces attendues à cette localisation :

```bash
uv run python -m birdnet_analyzer.species --lat 44.837 --lon -0.579 --week -1 detect_birds/species_list.txt
```

**Monde entier** — toutes les espèces du modèle (~6500) :

```bash
uv run python -m birdnet_analyzer.species detect_birds/species_list.txt
```
