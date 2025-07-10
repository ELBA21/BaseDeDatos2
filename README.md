# Sistema de gestión de torneos de tenis de mesa

Este proyecto modela un sistema completo de torneos de tenis de mesa. Incluye funcionalidades para gestionar jugadores, equipos, categorías, torneos, partidos y resultados, utilizando Python y SQLAlchemy como ORM.

---
## Características principales
- Registro de jugadores y asociaciones
- Administración de ciudades y países
- Organización de torneos con múltiples categorías
- Soporte para inscripciones individuales y por equipo
- Asignación de mesas, horarios y fases de competición
- Registro detallado de resultados por set
- Relaciones claras entre entidades: partidos, jugadores, equipos, fases, etc.
---
## Estructura de modelos
### Jugador
- Atributos: nombre, fecha de nacimiento, género, ciudad, categoría
- Relaciones: pertenece a una asociación, puede estar en uno o dos equipos, puede jugar múltiples partidos e inscribirse en torneos

### Asociación
- Asociación a la que puede pertenecer un jugador
- Tiene una ciudad asociada

### Ciudad y País
- Una ciudad pertenece a un país :D porque como dijo el Agustín (casi seguro que fue él) no vamos a estar en puerto montt en francia
- Los jugadores y asociaciones están ligados a ciudades

### Equipo
- Equipos dobles compuestos por dos jugadores
- Participan en partidos y pueden inscribirse a torneos

### Torneo
- Incluye fecha de inscripción, nombre y tipo de competencia
- Relación con mesas y categorías mediante TorneoCategoria

### Categoría
- Define edad mínima/máxima, género, sets por partido y puntos por set
- Se relaciona con jugadores, equipos y partidos

### Inscripción
- Relaciona jugadores o equipos con una categoría dentro de un torneo.

### Fase
- Define etapas como grupos o eliminación directa
- Pertenece a una categoría dentro de un torneo TorneoCategoria

### Partido
- Incluye equipos y/o jugadores, mesa asignada, horario, fase y categoría
- Registra quién fue el ganador y los sets jugados

### Mesa
- Asignada a partidos dentro de un torneo

### Set
- Guarda los puntos de cada jugador por set en un partido

### Género
- Usado para categorizar jugadores y categorías
---
## Tecnologías utilizadas
- Python 3.11
- SQLAlchemy
- SQLite 
- FastAPI
---

## Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/ELBA21/BaseDeDatos2.git
cd BaseDeDatos2
