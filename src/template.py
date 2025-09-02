import clips


def create_environment_with_templates():
    """Create the env with course and profile templates"""
    env = clips.Environment()

    curso_template = """
    (deftemplate curso
        (slot id (type INTEGER))
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
        (slot id (type INTEGER))
        (slot preferencia_turno (type STRING))
        (slot nota_enem (type FLOAT))
        (multislot areas_interesse (type STRING))
        (multislot locais_interesse (type STRING))
        (slot tipo_preferencia (type STRING))
        (slot duracao_preferencia (type INTEGER))
    )
    """

    curso_engenharia_template = """
    (deftemplate curso-engenharia
        (slot id (type INTEGER)) ;; mirrors curso:id
        (slot nome (type STRING)) ;; mirrors curso:nome
        (slot foco (type STRING)) ;; ex: infraestrutura, elétrica, materiais, mecânica
    )
    """

    perfil_engenharia_template = """
    (deftemplate perfil-engenharia
        (slot cpf (type INTEGER)) ;; mirros perfil:cpf
        (slot foco_preferencia (type STRING))
    )
    """

    env.build(curso_template)
    env.build(perfil_template)
    env.build(curso_engenharia_template)
    env.build(perfil_engenharia_template)

    return env


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
