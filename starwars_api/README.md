# Star Wars API

Scripts en Node.js qui interrogent la [Star Wars API](https://swapi-api.alx-tools.com/)
à l'aide du module `request`.

## Prérequis

- Node.js 10.14.x
- Module `request` (`sudo npm install -g request`)
- `export NODE_PATH=/usr/lib/node_modules`

## Tasks

### 0. Star Wars Characters

`0-starwars_characters.js` affiche tous les personnages d'un film Star Wars.

- Le premier argument positionnel est l'ID du film (ex : `3` = *Return of the Jedi*).
- Un nom de personnage par ligne, dans le même ordre que la liste `characters`
  de l'endpoint `/films/`.

#### Usage

```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
...
```
