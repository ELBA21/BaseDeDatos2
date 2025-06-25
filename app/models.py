from sqlalchemy import Column, Date, DateTime, Integer, String, ForeignKey, Table, Time
from sqlalchemy.orm import relationship
from .db import Base

#Comentario de prueba de mi rama local

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

    #asosiacion-jugador
    jugadores = relationship("Jugador", back_populates="asociacion")


class Partido(Base):
    __tablename__ = "partido"

    #Atributos
    id = Column(Integer,primary_key=True, index=True)
    horario = Column(Time, nullable=False)
    resultado = Column(String, nullable=False)
    
    #ForeignKeys (Se viene pesaito pipipipi)
    #Por convencion le agrego "_id" a las fKeys (nueva abreviacion para las ForeignKeys a partir de ahora) (no se volvio a usar)
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

    #equipo-partido
    equipo1 = relationship("Equipo", back_populates="partido_equipo1", foreign_keys=[equipo1_id])
    equipo2 = relationship("Equipo", back_populates="partido_equipo2",foreign_keys=[equipo2_id])
    #
    ##partido-jugador
    jugador1 = relationship("Jugador", back_populates="partido_jugador1", foreign_keys=[jugador1_id])
    jugador2 = relationship("Jugador", back_populates="partido_jugador2",foreign_keys=jugador2_id)
#
    #categoria-partido
    categoria = relationship("Categoria",back_populates="partidos")
#
    ##mesa-partido
    mesa = relationship("Mesa", back_populates="partidos")
#
    ##fase-partido
    fase= relationship("Fase", back_populates="partidos") 
#
    #sets-partido
    sets = relationship("Set", back_populates="partido")

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

    #jugador-equipo
    jugador1 = relationship("Jugador",back_populates="equipos_jugador1",foreign_keys=[jugador_id])
    jugador2 = relationship("Jugador", back_populates="equipos_jugador2", foreign_keys=[jugador2_id])

    #categoria-equipo
    categoria = relationship("Categoria", back_populates="equipos")

    #partido-equipo
    partido_equipo1 = relationship("Partido", back_populates="equipo1", foreign_keys=[Partido.equipo1_id])
    partido_equipo2 = relationship("Partido", back_populates="equipo2", foreign_keys=[Partido.equipo2_id])



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
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    #Notar que la estructura es practicamente la misma, solo que se agrega el nombre de la tabla + '.id' dentro del argumento del Foreignkey

    #Relationships
    #Los 'relationship' ayudan a conectar las tablas en python

    #asociacion-jugador
    asociacion = relationship("Asociacion", back_populates="jugadores")
    
    #Relationship categoria-jugador
    categoria = relationship("Categoria", back_populates="jugadores")

    #Relationship equipo-jugador
    equipos_jugador1 = relationship("Equipo",back_populates="jugador1",foreign_keys=[Equipo.jugador_id])
    equipos_jugador2 = relationship("Equipo",back_populates="jugador2",foreign_keys=[Equipo.jugador2_id])

    #partido-jugador
    partido_jugador1 =  relationship("Partido", back_populates="jugador1", foreign_keys=[Partido.jugador1_id])
    partido_jugador2 =  relationship("Partido", back_populates="jugador2", foreign_keys=[Partido.jugador2_id])


    
#torneo_categoria = Table("torneo_categoria",Base.metadata, Column("categoria", ForeignKey("categoria.id"), primary_key=True), Column("torneo", ForeignKey("torneo.id"), primary_key=True))

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
    #jugador-categoria
    jugadores = relationship("Jugador", back_populates="categoria")

    #equipo-categoria
    equipos = relationship("Equipo", back_populates="categoria")

    #partido-categoria
    partidos = relationship("Partido", back_populates="categoria")

    #torneo-categoria
    #torneos = relationship("Torneo", secondary=torneo_categoria, backref="categoria")
    torneo_categorias = relationship("TorneoCategoria", back_populates="categoria")

class TorneoCategoria(Base): #ELANDRE VVVVVVV
    __tablename__ = 'torneo_categoria'

    #Atributos
    torneo_id = Column(Integer, ForeignKey('torneo.id'), primary_key=True)
    categoria_id = Column(Integer, ForeignKey('categoria.id'), primary_key=True)

    #Relationships
    torneo = relationship("Torneo", back_populates="torneo_categorias")
    categoria = relationship("Categoria", back_populates="torneo_categorias")

class Torneo(Base):
    __tablename__ = "torneo"
    #Atributos
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_Inscripcion = Column(Date, nullable=False)
    competencia = Column(String)

    #Relationships
    #categoria-torneos
    #Se uso backref del lado contrario.

    #mesa-torneo
    mesas = relationship("Mesa", back_populates="torneo") 

    #fase-torneo
    fases = relationship("Fase", back_populates="torneo")

    torneo_categorias = relationship("TorneoCategoria", back_populates="torneo") #ELANDRE

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
    ##Aun asi la foreignKey debe ser llamada como relationship

    #Relationship
    #partido-fase
    partidos = relationship("Partido", back_populates="fase")

    #torneo-fase
    torneo =  relationship("Torneo", back_populates="fases")

class Mesa(Base):
    __tablename__ = "mesa"

    #Atributos
    id = Column(Integer, primary_key=True)

    #ForeignKeys
    Torneo_id = Column(Integer, ForeignKey('torneo.id'))

    #RelationShips
    #torneo-mesa
    torneo = relationship("Torneo", back_populates="mesas")

    #mesa-partido
    partidos = relationship("Partido", back_populates="mesa")

#Sinceramente no se que hace Base, estaba en la plantilla, debo preguntar eso
# Respuesta: Base hace referencia a la conexion a la base de datos (plantilla del profe)


class Set(Base):
    __tablename__ = "set"

    #Atributos
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    numero_Set = Column(Integer, nullable= False)
    puntos_Jugador1 = Column(Integer, nullable=False)
    puntos_Jugador2 = Column(Integer, nullable=False)

    #ForeignKey
    partido_id = Column(Integer, ForeignKey("partido.id"))

    #relationship
    #sets-partido
    partido = relationship("Partido", back_populates="sets")