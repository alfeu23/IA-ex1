import clips

campus_d = {
    "FLN": "Florianopolis",
    "ARA": "Ararangua",
    "BLU": "Blumenau",
    "CUR": "Curitibanos",
    "JOI": "Joinville",
}

area_d = {
    "CET": "Ciencias Exatas e da Terra",
    "LLA": "Linguistica, Letras e Artes",
    "CB": "Ciencias Biologicas",
    "ENG": "Engenharias",
    "CS": "Ciencias da Saude",
    "CIA": "Ciencias Sociais Aplicadas",
    "CA": "Ciencias Agrarias",
    "CH": "Ciencias Humanas",
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
   (multislot tipo (type STRING)) ;; licenciatura/bacharelado
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
curso = env.find_template("curso")

curso.assert_fact(
    nome="ADMINISTRAÇÃO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=716.95,
)

curso.assert_fact(
    nome="ADMINISTRAÇÃO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=708.06,
)

curso.assert_fact(
    nome="AGRONOMIA",
    campus=campus_d["CUR"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CA"],
    nota_corte=658.95,
)

curso.assert_fact(
    nome="AGRONOMIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CA"],
    nota_corte=697.85,
)

curso.assert_fact(
    nome="ANIMAÇÃO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["LLA"],
    nota_corte=781.58,
)

curso.assert_fact(
    nome="ANTROPOLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="bacharelado",
    area=area_d["CH"],
    nota_corte=643.07,
)

curso.assert_fact(
    nome="ARQUIVOLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=644.73,
)

curso.assert_fact(
    nome="ARTES CÊNICAS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["LLA"],
    nota_corte=717.11,
)

curso.assert_fact(
    nome="BIBLIOTECONOMIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=640.67,
)

curso.assert_fact(
    nome="CIÊNCIA DA INFO.",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=696.16,
)

curso.assert_fact(
    nome="CIÊNCIA E TEC.",
    campus=campus_d["JOI"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=691.61,
)

curso.assert_fact(
    nome="CIÊNCIAS BIOLÓGICAS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="licenciatura",
    area=area_d["CB"],
    nota_corte=711.27,
)

curso.assert_fact(
    nome="CIÊNCIAS CONTÁBEIS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=718.43,
)

curso.assert_fact(
    nome="CIÊNCIAS CONTÁBEIS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=670.73,
)

curso.assert_fact(
    nome="CIÊNCIAS ECONÔMICAS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=737.71,
)

curso.assert_fact(
    nome="CIÊNCIAS ECONÔMICAS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=757.53,
)

curso.assert_fact(
    nome="CIÊNCIAS SOCIAIS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado/licenciatura",
    area=area_d["CIA"],
    nota_corte=711.24,
)

curso.assert_fact(
    nome="CIÊNCIAS SOCIAIS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado/licenciatura",
    area=area_d["CIA"],
    nota_corte=726.93,
)

curso.assert_fact(
    nome="CINEMA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["LLA"],
    nota_corte=698.35,
)

curso.assert_fact(
    nome="DESIGN",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=757.56,
)

curso.assert_fact(
    nome="DIREITO",
    campus=campus_d["FLN"],
    duracao="10",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=757.13,
)

curso.assert_fact(
    nome="DIREITO",
    campus=campus_d["FLN"],
    duracao="10",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=770.76,
)

curso.assert_fact(
    nome="EDUCAÇÃO FÍSICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=721.82,
)

curso.assert_fact(
    nome="EDUCAÇÃO FÍSICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=663.58,
)

curso.assert_fact(
    nome="ENFERMAGEM",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=751.45,
)

curso.assert_fact(
    nome="ENG. AEROESPACIAL",
    campus=campus_d["JOI"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=796.37,
)

curso.assert_fact(
    nome="ENG. AUTOMOTIVA",
    campus=campus_d["JOI"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=738.4,
)

curso.assert_fact(
    nome="ENG. CIVIL",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=723.61,
)

curso.assert_fact(
    nome="ENG. DE ALIMENTOS",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=703.07,
)

curso.assert_fact(
    nome="ENG. DE ENERGIA",
    campus=campus_d["ARA"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=674.46,
)

curso.assert_fact(
    nome="ENG. DE MATERIAIS",
    campus=campus_d["BLU"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=637.67,
)

curso.assert_fact(
    nome="ENG. DE MATERIAIS",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=730.56,
)

curso.assert_fact(
    nome="ENG. DE PRODUÇÃO",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=742.72,
)

curso.assert_fact(
    nome="ENG. ELÉTRICA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=739.84,
)

curso.assert_fact(
    nome="ENG. ELETRÔNICA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=723.92,
)

curso.assert_fact(
    nome="ENG. FLORESTAL",
    campus=campus_d["CUR"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=638.71,
)

curso.assert_fact(
    nome="ENG. MECÂNICA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=761.65,
)

curso.assert_fact(
    nome="ENG. MECATRÔNICA",
    campus=campus_d["JOI"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=769.68,
)

curso.assert_fact(
    nome="ENG. NAVAL",
    campus=campus_d["JOI"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=753.09,
)

curso.assert_fact(
    nome="ENG. QUÍMICA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=760.37,
)

curso.assert_fact(
    nome="ENG. TÊXTIL",
    campus=campus_d["BLU"],
    duracao="10",
    turno="matutino",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=624.95,
)

curso.assert_fact(
    nome="FARMÁCIA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=739.91,
)

curso.assert_fact(
    nome="FILOSOFIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CH"],
    nota_corte=725.8,
)

curso.assert_fact(
    nome="FILOSOFIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="licenciatura",
    area=area_d["CH"],
    nota_corte=735.07,
)

curso.assert_fact(
    nome="FÍSICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=726.67,
)

curso.assert_fact(
    nome="FÍSICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=667.62,
)

curso.assert_fact(
    nome="FISIOTERAPIA",
    campus=campus_d["ARA"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=746.62,
)

curso.assert_fact(
    nome="FONOAUDIOLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=659.44,
)

curso.assert_fact(
    nome="GEOGRAFIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="bacharelado/licenciatura",
    area=area_d["CH"],
    nota_corte=705.16,
)

curso.assert_fact(
    nome="GEOGRAFIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado/licenciatura",
    area=area_d["CH"],
    nota_corte=679.95,
)

curso.assert_fact(
    nome="GEOLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=656.25,
)

curso.assert_fact(
    nome="HISTÓRIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="ABI",
    area=area_d["CH"],
    nota_corte=744.16,
)

curso.assert_fact(
    nome="HISTÓRIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="ABI",
    area=area_d["CH"],
    nota_corte=716.71,
)

curso.assert_fact(
    nome="JORNALISMO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=749.21,
)

curso.assert_fact(
    nome="LETRAS ALEMÃO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="ABI",
    area=area_d["LLA"],
    nota_corte=698.18,
)

curso.assert_fact(
    nome="LETRAS ESPANHOL",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="ABI",
    area=area_d["LLA"],
    nota_corte=663.25,
)

curso.assert_fact(
    nome="LETRAS FRANCÊS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="ABI",
    area=area_d["LLA"],
    nota_corte=681.27,
)

curso.assert_fact(
    nome="LETRAS INGLÊS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="ABI",
    area=area_d["LLA"],
    nota_corte=674.33,
)

curso.assert_fact(
    nome="LETRAS ITALIANO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="ABI",
    area=area_d["LLA"],
    nota_corte=691.31,
)

curso.assert_fact(
    nome="LETRAS PORTUGUÊS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado/licenciatura",
    area=area_d["LLA"],
    nota_corte=683.81,
)

curso.assert_fact(
    nome="MATEMÁTICA",
    campus=campus_d["BLU"],
    duracao="8",
    turno="noturno",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=682.46,
)

curso.assert_fact(
    nome="MATEMÁTICA",
    campus=campus_d["BLU"],
    duracao="8",
    turno="matutino",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=672.72,
)

curso.assert_fact(
    nome="MATEMÁTICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=749.46,
)

curso.assert_fact(
    nome="MATEMÁTICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="matutino",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=692.27,
)

curso.assert_fact(
    nome="MEDICINA",
    campus=campus_d["ARA"],
    duracao="12",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=817.27,
)

curso.assert_fact(
    nome="MEDICINA",
    campus=campus_d["FLN"],
    duracao="12",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=823.84,
)

curso.assert_fact(
    nome="METEOROLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=615.82,
)

curso.assert_fact(
    nome="MUSEOLOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=636.39,
)

curso.assert_fact(
    nome="NUTRIÇÃO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=771.11,
)

curso.assert_fact(
    nome="OCEANOGRAFIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=686.76,
)

curso.assert_fact(
    nome="ODONTOLOGIA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CS"],
    nota_corte=773.36,
)

curso.assert_fact(
    nome="PEDAGOGIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="licenciatura",
    area=area_d["CH"],
    nota_corte=683.93,
)

curso.assert_fact(
    nome="PSICOLOGIA",
    campus=campus_d["FLN"],
    duracao="10",
    turno="integral",
    tipo="bacharelado/licenciatura",
    area=area_d["CS"],
    nota_corte=770.51,
)

curso.assert_fact(
    nome="QUÍMICA",
    campus=campus_d["BLU"],
    duracao="8",
    turno="noturno",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=678.71,
)

curso.assert_fact(
    nome="QUÍMICA",
    campus=campus_d["BLU"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=699.15,
)

curso.assert_fact(
    nome="QUÍMICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="licenciatura",
    area=area_d["CET"],
    nota_corte=704.07,
)

curso.assert_fact(
    nome="QUÍMICA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CET"],
    nota_corte=712.65,
)

curso.assert_fact(
    nome="RELAÇÕES INTERNACIONAIS",
    campus=campus_d["FLN"],
    duracao="8",
    turno="vespertino",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=755.64,
)

curso.assert_fact(
    nome="SECRETARIADO EXECUTIVO",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=680.78,
)

curso.assert_fact(
    nome="SERVIÇO SOCIAL",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["CIA"],
    nota_corte=660.71,
)

curso.assert_fact(
    nome="SISTEMAS DE INFO.",
    campus=campus_d["FLN"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=739.73,
)

curso.assert_fact(
    nome="TEC. DA INFO. E COMUNICAÇÃO",
    campus=campus_d["ARA"],
    duracao="8",
    turno="noturno",
    tipo="bacharelado",
    area=area_d["ENG"],
    nota_corte=705.96,
)

curso.assert_fact(
    nome="ZOOTECNIA",
    campus=campus_d["FLN"],
    duracao="8",
    turno="integral",
    tipo="bacharelado",
    area=area_d["CA"],
    nota_corte=671.67,
)


# Perfil

perfil = env.find_template("perfil")
perfil.assert_fact(
    preferencia_turno="integral",
    nota_enem=680.00,
    areas_interesse=[area_d["CS"], area_d["CET"]],
    locais_interesse=[campus_d["FLN"], campus_d["CUR"]],
)

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
