from template import campus_d, area_d


def add_cursos_facts(env):
    """Add all course facts to the CLIPS environment"""
    curso = env.find_template("curso")

    curso.assert_fact(
        nome="ADMINISTRAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=716.95,
    )

    curso.assert_fact(
        nome="ADMINISTRAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=708.06,
    )

    curso.assert_fact(
        nome="AGRONOMIA",
        campus=campus_d["CUR"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=658.95,
    )

    curso.assert_fact(
        nome="AGRONOMIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=697.85,
    )

    curso.assert_fact(
        nome="ANIMAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=781.58,
    )

    curso.assert_fact(
        nome="ANTROPOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=643.07,
    )

    curso.assert_fact(
        nome="ARQUIVOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=644.73,
    )

    curso.assert_fact(
        nome="ARTES CÊNICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=717.11,
    )

    curso.assert_fact(
        nome="BIBLIOTECONOMIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=640.67,
    )

    curso.assert_fact(
        nome="CIÊNCIA DA INFO.",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=696.16,
    )

    curso.assert_fact(
        nome="CIÊNCIA E TEC.",
        campus=campus_d["JOI"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=691.61,
    )

    curso.assert_fact(
        nome="CIÊNCIAS BIOLÓGICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CB"],
        nota_corte=711.27,
    )

    curso.assert_fact(
        nome="CIÊNCIAS CONTÁBEIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=718.43,
    )

    curso.assert_fact(
        nome="CIÊNCIAS CONTÁBEIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=670.73,
    )

    curso.assert_fact(
        nome="CIÊNCIAS ECONÔMICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=737.71,
    )

    curso.assert_fact(
        nome="CIÊNCIAS ECONÔMICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.53,
    )

    curso.assert_fact(
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=711.24,
    )

    curso.assert_fact(
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CIA"],
        nota_corte=711.24,
    )

    curso.assert_fact(
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=726.93,
    )

    curso.assert_fact(
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CIA"],
        nota_corte=726.93,
    )

    curso.assert_fact(
        nome="CINEMA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=698.35,
    )

    curso.assert_fact(
        nome="DESIGN",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.56,
    )

    curso.assert_fact(
        nome="DIREITO",
        campus=campus_d["FLN"],
        duracao=10,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.13,
    )

    curso.assert_fact(
        nome="DIREITO",
        campus=campus_d["FLN"],
        duracao=10,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=770.76,
    )

    curso.assert_fact(
        nome="EDUCAÇÃO FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=721.82,
    )

    curso.assert_fact(
        nome="EDUCAÇÃO FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=663.58,
    )

    curso.assert_fact(
        nome="ENFERMAGEM",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=751.45,
    )

    curso.assert_fact(
        nome="ENG. AEROESPACIAL",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=796.37,
    )

    curso.assert_fact(
        nome="ENG. AUTOMOTIVA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=738.4,
    )

    curso.assert_fact(
        nome="ENG. CIVIL",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=723.61,
    )

    curso.assert_fact(
        nome="ENG. DE ALIMENTOS",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=703.07,
    )

    curso.assert_fact(
        nome="ENG. DE ENERGIA",
        campus=campus_d["ARA"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=674.46,
    )

    curso.assert_fact(
        nome="ENG. DE MATERIAIS",
        campus=campus_d["BLU"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=637.67,
    )

    curso.assert_fact(
        nome="ENG. DE MATERIAIS",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=730.56,
    )

    curso.assert_fact(
        nome="ENG. DE PRODUÇÃO",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=742.72,
    )

    curso.assert_fact(
        nome="ENG. ELÉTRICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=739.84,
    )

    curso.assert_fact(
        nome="ENG. ELETRÔNICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=723.92,
    )

    curso.assert_fact(
        nome="ENG. FLORESTAL",
        campus=campus_d["CUR"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=638.71,
    )

    curso.assert_fact(
        nome="ENG. MECÂNICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=761.65,
    )

    curso.assert_fact(
        nome="ENG. MECATRÔNICA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=769.68,
    )

    curso.assert_fact(
        nome="ENG. NAVAL",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=753.09,
    )

    curso.assert_fact(
        nome="ENG. QUÍMICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=760.37,
    )

    curso.assert_fact(
        nome="ENG. TÊXTIL",
        campus=campus_d["BLU"],
        duracao=10,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=624.95,
    )

    curso.assert_fact(
        nome="FARMÁCIA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=739.91,
    )

    curso.assert_fact(
        nome="FILOSOFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=725.8,
    )

    curso.assert_fact(
        nome="FILOSOFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=735.07,
    )

    curso.assert_fact(
        nome="FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=726.67,
    )

    curso.assert_fact(
        nome="FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=667.62,
    )

    curso.assert_fact(
        nome="FISIOTERAPIA",
        campus=campus_d["ARA"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=746.62,
    )

    curso.assert_fact(
        nome="FONOAUDIOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=659.44,
    )

    curso.assert_fact(
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=705.16,
    )

    curso.assert_fact(
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=705.16,
    )

    curso.assert_fact(
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=679.95,
    )

    curso.assert_fact(
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=679.95,
    )

    curso.assert_fact(
        nome="GEOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=656.25,
    )

    curso.assert_fact(
        nome="HISTÓRIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["CH"],
        nota_corte=744.16,
    )

    curso.assert_fact(
        nome="HISTÓRIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="ABI",
        area=area_d["CH"],
        nota_corte=716.71,
    )

    curso.assert_fact(
        nome="JORNALISMO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=749.21,
    )

    curso.assert_fact(
        nome="LETRAS ALEMÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=698.18,
    )

    curso.assert_fact(
        nome="LETRAS ESPANHOL",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=663.25,
    )

    curso.assert_fact(
        nome="LETRAS FRANCÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=681.27,
    )

    curso.assert_fact(
        nome="LETRAS INGLÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=674.33,
    )

    curso.assert_fact(
        nome="LETRAS ITALIANO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=691.31,
    )

    curso.assert_fact(
        nome="LETRAS PORTUGUÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=683.81,
    )

    curso.assert_fact(
        nome="LETRAS PORTUGUÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["LLA"],
        nota_corte=683.81,
    )

    curso.assert_fact(
        nome="MATEMÁTICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=682.46,
    )

    curso.assert_fact(
        nome="MATEMÁTICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=672.72,
    )

    curso.assert_fact(
        nome="MATEMÁTICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=749.46,
    )

    curso.assert_fact(
        nome="MATEMÁTICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=692.27,
    )

    curso.assert_fact(
        nome="MEDICINA",
        campus=campus_d["ARA"],
        duracao=12,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=817.27,
    )

    curso.assert_fact(
        nome="MEDICINA",
        campus=campus_d["FLN"],
        duracao=12,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=823.84,
    )

    curso.assert_fact(
        nome="METEOROLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=615.82,
    )

    curso.assert_fact(
        nome="MUSEOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=636.39,
    )

    curso.assert_fact(
        nome="NUTRIÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=771.11,
    )

    curso.assert_fact(
        nome="OCEANOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=686.76,
    )

    curso.assert_fact(
        nome="ODONTOLOGIA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=773.36,
    )

    curso.assert_fact(
        nome="PEDAGOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=683.93,
    )

    curso.assert_fact(
        nome="PSICOLOGIA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=770.51,
    )

    curso.assert_fact(
        nome="PSICOLOGIA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="licenciatura",
        area=area_d["CS"],
        nota_corte=770.51,
    )

    curso.assert_fact(
        nome="QUÍMICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=678.71,
    )

    curso.assert_fact(
        nome="QUÍMICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=699.15,
    )

    curso.assert_fact(
        nome="QUÍMICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=704.07,
    )

    curso.assert_fact(
        nome="QUÍMICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=712.65,
    )

    curso.assert_fact(
        nome="RELAÇÕES INTERNACIONAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=755.64,
    )

    curso.assert_fact(
        nome="SECRETARIADO EXECUTIVO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=680.78,
    )

    curso.assert_fact(
        nome="SERVIÇO SOCIAL",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=660.71,
    )

    curso.assert_fact(
        nome="SISTEMAS DE INFO.",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=739.73,
    )

    curso.assert_fact(
        nome="TEC. DA INFO. E COMUNICAÇÃO",
        campus=campus_d["ARA"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=705.96,
    )

    curso.assert_fact(
        nome="ZOOTECNIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=671.67,
    )
