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
        (slot foco_preferencia (type STRING))
    )
    """

    profissao_template = """
    (deftemplate profissao
        (slot id (type INTEGER))
        (slot nome (type STRING))
        (slot categoria (type STRING)) ;; publico, privado, academico, autonomo
        (slot setor (type STRING)) ;; saude, educacao, tecnologia, juridico, engenharia, etc
        (slot salario_medio (type FLOAT))
        (slot nivel_autonomia (type STRING)) ;; baixo, medio, alto
        (slot descricao (type STRING))
    )
    """

    curso_profissao_template = """
    (deftemplate curso-profissao
        (slot curso_nome (type STRING))
        (slot profissao_nome (type STRING))
        (slot requisitos_adicionais (type STRING)) ;; concurso, pos-graduacao, certificacao, experiencia
    )
    """

    perfil_profissional_template = """
    (deftemplate perfil-profissional
        (multislot categorias_interesse (type STRING))
        (multislot setores_interesse (type STRING))
        (slot salario_minimo_desejado (type FLOAT))
        (slot autonomia_desejada (type STRING))
    )
    """

    env.build(curso_template)
    env.build(perfil_template)
    env.build(curso_engenharia_template)
    env.build(perfil_engenharia_template)
    env.build(profissao_template)
    env.build(curso_profissao_template)
    env.build(perfil_profissional_template)

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

areas_dict = {i+1: area for i, area in enumerate(area_d.values())}
campus_dict = {i+1: campus for i, campus in enumerate(campus_d.values())}

tipos_dict = {
        1: "bacharelado",
        2: "licenciatura",
        3: "ABI"
    }
    
focos_engenharia_dict = {
        1: "infraestrutura",
        2: "elétrica",
        3: "mecânica",
        4: "materiais"
}

turnos_dict = {
        1: "matutino",
        2: "vespertino", 
        3: "noturno",
        4: "integral"
}

categorias_profissao_dict = {
    1: "autonomo",
    2: "publico", 
    3: "privado",
    4: "academico",
}

setores_profissao_dict = {
    1: "saude",
    2: "educacao",
    3: "tecnologia",
    4: "juridico",
    5: "engenharia",
    6: "administracao",
    7: "comunicacao",
    8: "arte",
    9: "ciencias",
    10: "agrario"
}

autonomia_dict = {
    1: "baixo",
    2: "medio", 
    3: "alto"
}
