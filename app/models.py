from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table, Time
from sqlalchemy.orm import relationship
from .db import Base

#Cada tabla tiene una estructura algo asi
#class Nombre_Tabla_A(Base):
#   __tablename_ = "Tabla_A" (Puede ser comillas normales o dobles)
#   #Naturalmente esto es el nombre que tiene la tabla
# 
#   #Atributos
#   #Para definir cada atributo se usa un metodo tal que asi
#   id = Column(Integer, primarykey = true)
#       
#   #Naturalmente esto es
#   #id -> Nombre del atributo dentro de la clase
#   #Column -> Tipo de dato que se usa (Integer, String, Date, Time, DateTime)
#   #Luego pueden usar primarykey o foreignkey segun convenga, se puede no poner ninguno
#   Es bastante usado tambien (nullable = false)
#
#   #Foreignkeys
#   #Es practicamente lo mismo que los atributos
#   clave_Tabla_B = Column(Integer, ForeignKey("Tabla_B.id")) <- Se pueden usar comillas simples o dobles
#   Se mentiene el mismo formato solo que aca se usa ForeignKey("NOMBREDELACUESTION ")
#
#   #Relationships
#   #Relationships es la cuestion de alchemy para conectar 2 clases que representan tablas en python
#   #nombre_tabla_b = Relationship("Tabla_B","nombre_tabla_b")
#   
#   #Parece confuso, por eso porfavor dirigirse a las clases Jugador-Equipo para explicara fondo todo


class Asociacion(Base):
    __tablename__ = 'asociacion'
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    #RelationShips
    #jugadores = relationship("Jugador", back_populates="asociacion")

class Jugador(Base):
    __tablename__ = 'jugador'
    #Atributos - En esta seccion se declaran las columnas de la tabla no relacionado con tablas externas
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable =False)
    genero = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)


    #ForegKeys - Esta seccion se declaran las columnas de la tabla RELACIONADA a otras tablas
    #Esto crearia las columnas de las claves foraneas
    asociacion_id = Column(Integer, ForeignKey('asociacion.id')) # <-- Se pueden usar comillas simples o dobles aparemente
    ategoria_id = Column(Integer, ForeignKey('categoria.id'))
    #Notar que la estructura es practicamente la misma, solo que se agrega el nombre de la tabla + '.id' dentro del argumento del Foreignkey

    #Relationships
    #Los 'relationship' ayudan a conectar las tablas en python
    #asociacion = relationship("Asociacion", back_populates="jugadores")
    #categoria = relationship("Categoria", back_populates="jugadores")

    #Para entenderlos prestar especial atencion a estos 2, principalmente al nombre y a lo que esta igualado en back_populates
    #equipos_jugador1 = relationship("Equipo", back_populates="jugador1")
    #equipos_jugador2 = relationship("Equipo", back_populates="jugador2")
    # equipo_jugador1, es un nombre que sera llamado luego en Equipo
    #en realtionship("Equipo") se refiere a que esta llamando algo de la CLASE "Equipo", no tiene nada que ver con tablename, solo el nombre de la clase
    # back_populates esta llamando al simil de equipo_jugador1, pero de la CLASE Equipo, porfavor seguir la explicacion en clase Equipo


class Equipo(Base):
    __tablename__ = 'equipo'
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    
    #ForeignKeys
    jugador_id = Column(Integer, ForeignKey('jugador.id'))
    jugador2_id = Column(Integer, ForeignKey('jugador.id'))
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    #RelationShips

    #Siguiendo con la explicacion anterior
    #Noten como jugador1, es exactamente lo mismo que se encontraba en la linea
    #       equipos_jugador1 = relationship("Equipo", back_populates="jugador1")
    #jugador1 fue llamado en back_populates="jugador1" hasta aca

    #Siento que me puse cargante con la explicacion asi que cualquier wea me preguntan en la u o por wsp
    #Ojala ya les haya quedado claro
    #jugador1 = relationship("Jugador",back_populates="equipos_jugador1")
    #jugador2 = relationship("Jugador", back_populates="equipos_jugador2")
#
#
    #categoria = relationship("Categoria", back_populates="equipos")
    #partido_equipo1 = relationship("Partido", back_populates="equipo1")
    #partido_equipo2 = relationship("Partido", back_populates="equipo2")
    #partido_jugador1 = relationship("Partido",back_populates= "jugador1")
    #partido_jugador2 = relationship("Partido",back_populates= "jugador2")
    
torneo_categoria = Table("torneo_categoria",Base.metadata, Column("categoria", ForeignKey("categoria.id"), primary_key=True), Column("torneo", ForeignKey("torneo.id"), primary_key=True))

class Categoria(Base):
    __tablename__ = 'categoria'
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    edad_Min = Column(Integer)
    edad_Max = Column(Integer)
    genero = Column(String, nullable=False)
    set_por_partido = Column(Integer)
    puntos_por_set = Column(Integer)
    #Relationships
    #jugadores = relationship("Jugador", back_populates="categoria")
    #equipos = relationship("Equipo", back_populates="categoria")
    #partidos = relationship("Partido", back_populates="categoria")
    #torneos = relationship("Torneo", secondary=torneo_categoria, backref="Categoria")

class Torneo(Base):
    __tablename__ = "torneo"
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_Inscripcion = Column(Date, nullable=False)
    competencia = Column(String)

    #Relationships
    #categoria = relationship("Categoria", secondary=torneo_categoria,backref="Torneo")
    #mesas = relationship("Mesa", back_populates="Torneo") 
    #fases = relationship("Fase", back_populates="Torneo")

class Fase(Base):
    __tablename__ = "fase"
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)

    #Como Fase Torneo tiene una relacion 1:N (Varias Fases - Un Torneo)
    #Fases debe llamar a la ForeignKey de Torneo
    #Llamamos un entero porque es un puto id obviamente es un entero
    Torneo_id = Column(Integer, ForeignKey('torneo.id'))


    #Por otro lado Fase en realcion a Partido es el 1, entonces solo llamamos el relationship()
    #partidos = relationship("Partido", back_populates="Fase")
    ##Aun asi la foreignKey debe ser llamada como relationship
    #Torneo =  relationship("Torneo", back_populates="fases")

class Mesa(Base):
    __tablename__ = "mesa"

    #Atributos
    id = Column(Integer, primary_key=True)

    #ForeignKeys
    Torneo_id = Column(Integer, ForeignKey('torneo.id'))

    #RelationShips
    #Torneo = relationship("Torneo", back_populates="mesas")
    #partidos = relationship("Partido", back_populates="Mesa")
#Sinceramente no se que hace Base, estaba en la plantilla, debo preguntar eso
class Partido(Base):
    __tablename__ = "partido"

    #Atributos
    id = Column(Integer,primary_key=True, index=True)
    horario = Column(Time, nullable=False)
    resultado = Column(String, nullable=False)
    
    #ForeignKeys (Se viene pesaito pipipipi)
    #Por convencion le agrego "_id" a las fKeys (nueva abreviacion para las ForeignKeys a partir de ahora)
    equipo1_id = Column(Integer, ForeignKey('equipo.id'))
    equipo2_id = Column(Integer, ForeignKey('equipo.id'))
    jugador1_id = Column(Integer, ForeignKey('jugador.id'))
    jugador2_id = Column(Integer,ForeignKey('jugador.id'))
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    mesa_id = Column(Integer, ForeignKey('mesa.id'))
    fase_id = Column(Integer, ForeignKey('fase.id'))
        #No fue tan pesao lol
    #btw pardio es el N, en la mayor parte de las relacione
    #Acabo de caer en cuenta que cuando nuro lea esto va a interpretar N de otra forma

    #Relationships
    #equipo1 = relationship("Equipo", back_populates="partido_equipo1")
    #equipo2 = relationship("Equipo", back_populates="partido_equipo2")
    #Jugador1 = relationship("Jugador", back_populates="partido_jugador1")
    #Jugador2 = relationship("Jugador", back_populates="partido_jugador2")
    #mesa = relationship("Mesa", back_populates="partidos")
    #fase= relationship("Fase", back_populates="partidos") 
    #sets = relationship("Set", back_populates="partido")
    #Chat-gpt me dijo que esto generapa problemas con las migraciones por eso lo deje comentado

class Set(Base):
    __tablename__ = "set"

    #Atributos
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    numero_Set = Column(Integer, nullable= False)
    puntos_Jugador1 = Column(Integer, nullable=False)
    puntos_Jugador2 = Column(Integer, nullable=False)
    #ForeignKey
    partido_id = Column(Integer, ForeignKey("partido.id"))

    #partido = relationship("Partido", back_populates="sets")