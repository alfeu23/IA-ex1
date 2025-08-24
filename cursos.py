import clips

campus_d = {
    "FLN": "Florianopolis",
    "ARA": "Ararangua",
    "BLU": "Blumenau",
    "CUR": "Curitibanos",
    "JOI": "Joinville"
}

area_d = {
    "CET": "Ciencias Exatas e da Terra",
    "LLA": "Linguistica, Letras e Artes",
    "CB": "Ciencias Biologicas",
    "ENG": "Engenharias",
    "CS": "Ciencias da Saude",
    "CIA": "Ciencias Sociais Aplicadas",
    "CA": "Ciencias Agrarias",
    "CH": "Ciencias Humanas"
}

# Criar ambiente CLIPS
env = clips.Environment()



# --- Templates ---

curso_template = """
(deftemplate curso
   (slot nome (type STRING))
   (slot campus (type STRING))
   (slot duracao (type INTEGER)) ;; em semestres
   (slot turno (type STRING)) ;; matutino/vespertino/noturno/integral
   (slot tipo (type STRING)) ;; licenciatura/bacharelado
   (slot area (type STRING)) ;; Ciências Exatas e da terra/Ciências Biológicas/Ciências da Saúde/Ciências Agrárias/Engenharias/Ciências Sociais Aplicadas/Ciências Humanas/Linguística, Letras e Artes
   (slot nota_corte (type FLOAT)) ;; https://sisu2024.ufsc.br/files/2024/02/notas-maximas-minimas-sisu2024.pdf
)
"""


perfil_template = """
(deftemplate perfil
   (slot preferencia_turno (type STRING))
   (slot nota_enem (type FLOAT))
   (multislot areas_interesse (type STRING))
   (multislot locais_interesse (type STRING))
)
"""


env.build(curso_template)
env.build(perfil_template)

# --- Fatos iniciais ---

# Cursos
curso = env.find_template('curso')
curso.assert_fact(nome='Ciencia da Computacao',
                  campus=campus_d["FLN"],
                  duracao=8,
                  turno='integral',
                  tipo='bacharelado',
                  area=area_d["CET"],
                  nota_corte=809.98)

curso.assert_fact(nome='Fisica',
                  campus=campus_d["FLN"],
                  duracao=7,
                  turno='integral',
                  tipo='bacharelado',
                  area=area_d["CET"],
                  nota_corte=726.67)

curso.assert_fact(nome='Fisica',
                  campus=campus_d["FLN"],
                  duracao=7,
                  turno='noturno',
                  tipo='licenciatura',
                  area=area_d["CET"],
                  nota_corte=667.62)

curso.assert_fact(nome='Medicina',
                  campus=campus_d["FLN"],
                  duracao=12,
                  turno='integral',
                  tipo='bacharelado',
                  area=area_d["CS"],
                  nota_corte=823.84)


# Perfil

perfil = env.find_template('perfil')
perfil.assert_fact(preferencia_turno='integral',
                   nota_enem=680.00,
                   areas_interesse=[area_d["CS"], area_d["CET"]],
                   locais_interesse=[campus_d["FLN"], campus_d["CUR"]])

# --- Regras ---
env.build("""
(defrule recomendar-curso-por-turno
   (perfil (preferencia_turno ?turno))
   (curso (nome ?n) (turno ?turno))
   =>
   (printout t "Recomendação por turno preferido: " ?n " - " ?turno crlf))
""")

env.build("""
(defrule recomendar-curso-por-nota
   (perfil (nota_enem ?ne))
   (curso (nome ?n) (nota_corte ?nc))
   (test (<= ?nc ?ne))
   =>
   (printout t "Curso possível com sua nota: " ?n " (Nota de corte: " ?nc ")" crlf))
""")

env.build("""
(defrule recomendar-curso-ideal
   (perfil (preferencia_turno ?turno) (areas_interesse $? ?area $?) (nota_enem ?ne))
   (curso (nome ?n) (turno ?turno) (area ?area) (nota_corte ?nc))
   (test (<= ?nc ?ne))
   =>
   (printout t "CURSO IDEAL: " ?n " - Corresponde ao seu turno, área de interesse e nota!" crlf))
""")


env.build(
"""
(defrule recomendar-curso
   ?p <- (perfil (nota_enem ?nota) (preferencia_turno ?turno) (areas_interesse $?areas))
   ?c <- (curso (nome ?nome) 
                (turno ?curso_turno) 
                (area ?area) 
                (nota_corte ?corte))
   (test (>= ?nota ?corte)) ;; só recomenda se a nota do aluno for suficiente
   (test (member$ ?area $?areas)) ;; verifica se a área está no interesse
   (test (or (eq ?turno "qualquer") (eq ?turno ?curso_turno))) ;; turno compatível ou "qualquer"
=>
   (printout t "O curso recomendado é: " ?nome " (" ?area ", turno: " ?curso_turno ")" crlf))
"""
)

# --- Rodar ---
env.run()