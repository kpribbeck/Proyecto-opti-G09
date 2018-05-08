from gurobipy import *

# Crea un modelo vacío
m = Model()


###########################################################################
#                              Conjuntos                                  #
###########################################################################
equipos = ["Colegio Los Leones de Quilpue",
    "Español de Talca",
    "Tinguiririca de San Fernando",
    "Universidad Católica",
    "Universidad de Concepción",
    "Municipal de Puente Alto",
    "Club Deportivo Valdivia",
    "AB Ancud",
    "Osorno Básquetbol",
    "Deportes Castro",
    "Las Ánimas de Valdivia",
    "CEB Puerto Montt"]

estadios = [
    "Gimnasio Colegio Los Leones",
    "Gimnasio Regional de Talca",
    "Gimnasio Municipal de San Fernando",
    "Estadio Palestino",
    "Casa del Deporte",
    "Gimnasio Municipal de Puente Alto",
    "Coliseo Municipal Antonio Azurmendy",
    "Gimnasio Fiscal de Ancud",
    "Gimnasio Monumental María Gallardo",
    "Gimnasio Fiscal de Castro",
    "Gimnasio de Las Ánimas",
    "Gimnasio Municipal Mario Merchant Binder"
]

# Fechas
F_N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
F_I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Rondas
T_N = [1, 2] # 1 = ida, 2 = vuelta
T_I = [1, 2]

# Conferencias
C = ["Centro", "Sur"]


###########################################################################
#                             Parámetros                                  #
###########################################################################

# Estadio j pertenece a equipo i
e = {
    "Colegio Los Leones de Quilpue": {"Gimnasio Colegio Los Leones": 1, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Español de Talca": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 1, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Tinguiririca de San Fernando": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 1, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Universidad Católica": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 1, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Universidad de Concepción": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 1, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Municipal de Puente Alto": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 1, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Club Deportivo Valdivia": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 1, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "AB Ancud": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 1, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Osorno Básquetbol": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 1, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Deportes Castro": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 1, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 0},
    "Las Ánimas de Valdivia": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 1, "Gimnasio Municipal Mario Merchant Binder": 0},
    "CEB Puerto Montt": {"Gimnasio Colegio Los Leones": 0, "Gimnasio Regional de Talca": 0, "Gimnasio Municipal de San Fernando": 0, "Estadio Palestino": 0, "Casa del Deporte": 0, "Gimnasio Municipal de Puente Alto": 0, "Coliseo Municipal Antonio Azurmendy": 0, "Gimnasio Fiscal de Ancud": 0, "Gimnasio Monumental María Gallardo": 0, "Gimnasio Fiscal de Castro": 0, "Gimnasio de Las Ánimas": 0, "Gimnasio Municipal Mario Merchant Binder": 1}
}

# Equipo i pertenece a conferencia c
co = {
    "Colegio Los Leones de Quilpue": {"Centro": 1, "Sur": 0},
    "Español de Talca": {"Centro": 1, "Sur": 0},
    "Tinguiririca de San Fernando": {"Centro": 1, "Sur": 0},
    "Universidad Católica": {"Centro": 1, "Sur": 0},
    "Universidad de Concepción": {"Centro": 1, "Sur": 0},
    "Municipal de Puente Alto": {"Centro": 1, "Sur": 0},
    "Club Deportivo Valdivia": {"Centro": 0, "Sur": 1},
    "AB Ancud": {"Centro": 0, "Sur": 1},
    "Osorno Básquetbol": {"Centro": 0, "Sur": 1},
    "Deportes Castro": {"Centro": 0, "Sur": 1},
    "Las Ánimas de Valdivia": {"Centro": 0, "Sur": 1},
    "CEB Puerto Montt": {"Centro": 0, "Sur": 1}
}

# Capacidad estadios
c = {
    "Gimnasio Colegio Los Leones": 800,
    "Gimnasio Regional de Talca": 2500,
    "Gimnasio Municipal de San Fernando": 2500,
    "Estadio Palestino": 700,
    "Casa del Deporte": 2000,
    "Gimnasio Municipal de Puente Alto": 1500,
    "Coliseo Municipal Antonio Azurmendy": 5000,
    "Gimnasio Fiscal de Ancud": 2450,
    "Gimnasio Monumental María Gallardo": 4500,
    "Gimnasio Fiscal de Castro": 1000,
    "Gimnasio de Las Ánimas": 5000,
    "Gimnasio Municipal Mario Merchant Binder": 2000
}


###########################################################################
#                              Variables                                  #
###########################################################################

x = {}
y = {}

for equipo1 in equipos:
    for equipo2 in equipos:
        if (equipo1 == equipo2):
            continue
        for fecha_n in F_N:
            for estadio in estadios:
                for ronda in T_N:
                    x[equipo1, equipo2, fecha_n, estadio, ronda] = m.addVar(vtype=GRB.BINARY, name="x_{}_{}_{}_{}_{}".format(equipo1, equipo2, fecha_n, estadio, ronda))
        for fecha_i in F_I:
            for estadio in estadios:
                for ronda in T_N:
                    y[equipo1, equipo2, fecha_i, estadio, ronda] = m.addVar(vtype=GRB.BINARY, name="x_{}_{}_{}_{}_{}".format(equipo1, equipo2, fecha_i, estadio, ronda))



H = m.addVar(vtype=GRB.CONTINUOUS, name="H")



#proceso de actualizaciones pendiente
m.update()


###########################################################################
#                          Función Objetivo                               #
###########################################################################
m.setObjective(H, GRB.MAXIMIZE)


###########################################################################
#                            Restricciones                                #
###########################################################################
#Agregar restricciones
c1 = m.addConstr(x + 2*y + 3*z <= 4)
c2 = m.addConstr(x + y >= 1)

#Resolver el modelo
m.optimize()

#Imprimir los valores de las variables para la solución óptima
# m.printAttr("X")