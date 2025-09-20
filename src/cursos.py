from template import campus_d, area_d


def add_cursos_facts(env):
    """Add the course facts"""
    curso = env.find_template("curso")
    curso_engenharia = env.find_template("curso-engenharia")

    curso.assert_fact(
        id=1,
        nome="ADMINISTRAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=716.95,
    )

    curso.assert_fact(
        id=2,
        nome="ADMINISTRAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=708.06,
    )

    curso.assert_fact(
        id=3,
        nome="AGRONOMIA",
        campus=campus_d["CUR"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=658.95,
    )

    curso.assert_fact(
        id=4,
        nome="AGRONOMIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=697.85,
    )

    curso.assert_fact(
        id=5,
        nome="ANIMAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=781.58,
    )

    curso.assert_fact(
        id=6,
        nome="ANTROPOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=643.07,
    )

    curso.assert_fact(
        id=7,
        nome="ARQUIVOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=644.73,
    )

    curso.assert_fact(
        id=8,
        nome="ARTES CÊNICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=717.11,
    )

    curso.assert_fact(
        id=9,
        nome="BIBLIOTECONOMIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=640.67,
    )

    curso.assert_fact(
        id=10,
        nome="CIÊNCIA DA INFO.",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=696.16,
    )

    curso.assert_fact(
        id=11,
        nome="CIÊNCIA E TEC.",
        campus=campus_d["JOI"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=691.61,
    )

    curso.assert_fact(
        id=12,
        nome="CIÊNCIAS BIOLÓGICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CB"],
        nota_corte=711.27,
    )

    curso.assert_fact(
        id=13,
        nome="CIÊNCIAS CONTÁBEIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=718.43,
    )

    curso.assert_fact(
        id=14,
        nome="CIÊNCIAS CONTÁBEIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=670.73,
    )

    curso.assert_fact(
        id=15,
        nome="CIÊNCIAS ECONÔMICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=737.71,
    )

    curso.assert_fact(
        id=16,
        nome="CIÊNCIAS ECONÔMICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.53,
    )

    curso.assert_fact(
        id=17,
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado/licenciatura",
        area=area_d["CIA"],
        nota_corte=711.24,
    )

    curso.assert_fact(
        id=18,
        nome="CIÊNCIAS SOCIAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado/licenciatura",
        area=area_d["CIA"],
        nota_corte=726.93,
    )

    curso.assert_fact(
        id=19,
        nome="CINEMA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["LLA"],
        nota_corte=698.35,
    )

    curso.assert_fact(
        id=20,
        nome="DESIGN",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.56,
    )

    curso.assert_fact(
        id=21,
        nome="DIREITO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=757.13,
    )

    curso.assert_fact(
        id=22,
        nome="DIREITO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=770.76,
    )

    curso.assert_fact(
        id=23,
        nome="EDUCAÇÃO FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=721.82,
    )

    curso.assert_fact(
        id=24,
        nome="EDUCAÇÃO FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=663.58,
    )

    curso.assert_fact(
        id=25,
        nome="ENFERMAGEM",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=751.45,
    )

    curso.assert_fact(
        id=26,
        nome="ENG. AEROESPACIAL",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=796.37,
    )

    curso_engenharia.assert_fact(id=26, nome="ENG. AEROESPACIAL", foco="mecânica")

    curso.assert_fact(
        id=27,
        nome="ENG. AUTOMOTIVA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=738.4,
    )

    curso_engenharia.assert_fact(id=27, nome="ENG. AUTOMOTIVA", foco="mecânica")

    curso.assert_fact(
        id=28,
        nome="ENG. CIVIL",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=723.61,
    )

    curso_engenharia.assert_fact(id=28, nome="ENG. CIVIL", foco="infraestrutura")

    curso.assert_fact(
        id=29,
        nome="ENG. DE ALIMENTOS",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=703.07,
    )

    curso_engenharia.assert_fact(id=29, nome="ENG. DE ALIMENTOS", foco="materiais")

    curso.assert_fact(
        id=30,
        nome="ENG. DE ENERGIA",
        campus=campus_d["ARA"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=674.46,
    )

    curso_engenharia.assert_fact(id=30, nome="ENG. DE ENERGIA", foco="elétrica")

    curso.assert_fact(
        id=31,
        nome="ENG. DE MATERIAIS",
        campus=campus_d["BLU"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=637.67,
    )

    curso_engenharia.assert_fact(id=31, nome="ENG. DE MATERIAIS", foco="materiais")

    curso.assert_fact(
        id=32,
        nome="ENG. DE MATERIAIS",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=730.56,
    )

    curso_engenharia.assert_fact(id=32, nome="ENG. DE MATERIAIS", foco="materiais")

    curso.assert_fact(
        id=33,
        nome="ENG. DE PRODUÇÃO",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=742.72,
    )

    curso_engenharia.assert_fact(id=33, nome="ENG. DE PRODUÇÃO", foco="infraestrutura")

    curso.assert_fact(
        id=34,
        nome="ENG. ELÉTRICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=739.84,
    )

    curso_engenharia.assert_fact(id=34, nome="ENG. ELÉTRICA", foco="elétrica")

    curso.assert_fact(
        id=35,
        nome="ENG. ELETRÔNICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=723.92,
    )

    curso_engenharia.assert_fact(id=35, nome="ENG. ELETRÔNICA", foco="elétrica")

    curso.assert_fact(
        id=36,
        nome="ENG. FLORESTAL",
        campus=campus_d["CUR"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=638.71,
    )

    curso_engenharia.assert_fact(id=36, nome="ENG. FLORESTAL", foco="infraestrutura")

    curso.assert_fact(
        id=37,
        nome="ENG. MECÂNICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=761.65,
    )

    curso_engenharia.assert_fact(id=37, nome="ENG. MECÂNICA", foco="mecânica")

    curso.assert_fact(
        id=38,
        nome="ENG. MECATRÔNICA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=769.68,
    )

    curso_engenharia.assert_fact(id=38, nome="ENG. MECATRÔNICA", foco="mecânica")

    curso.assert_fact(
        id=39,
        nome="ENG. NAVAL",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=753.09,
    )

    curso_engenharia.assert_fact(id=39, nome="ENG. NAVAL", foco="infraestrutura")

    curso.assert_fact(
        id=40,
        nome="ENG. QUÍMICA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=760.37,
    )

    curso_engenharia.assert_fact(id=40, nome="ENG. QUIMICA", foco="materiais")

    curso.assert_fact(
        id=41,
        nome="ENG. TÊXTIL",
        campus=campus_d["BLU"],
        duracao=10,
        turno="matutino",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=624.95,
    )

    curso_engenharia.assert_fact(id=41, nome="ENG. TÊXTIL", foco="materiais")

    curso.assert_fact(
        id=42,
        nome="FARMÁCIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=739.91,
    )

    curso.assert_fact(
        id=43,
        nome="FILOSOFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CH"],
        nota_corte=725.8,
    )

    curso.assert_fact(
        id=44,
        nome="FILOSOFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=735.07,
    )

    curso.assert_fact(
        id=45,
        nome="FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=726.67,
    )

    curso.assert_fact(
        id=46,
        nome="FÍSICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=667.62,
    )

    curso.assert_fact(
        id=47,
        nome="FISIOTERAPIA",
        campus=campus_d["ARA"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=746.62,
    )

    curso.assert_fact(
        id=48,
        nome="FONOAUDIOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=659.44,
    )

    curso.assert_fact(
        id=49,
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="bacharelado/licenciatura",
        area=area_d["CH"],
        nota_corte=705.16,
    )

    curso.assert_fact(
        id=50,
        nome="GEOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado/licenciatura",
        area=area_d["CH"],
        nota_corte=679.95,
    )

    curso.assert_fact(
        id=51,
        nome="GEOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=656.25,
    )

    curso.assert_fact(
        id=52,
        nome="HISTÓRIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["CH"],
        nota_corte=744.16,
    )

    curso.assert_fact(
        id=53,
        nome="HISTÓRIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="ABI",
        area=area_d["CH"],
        nota_corte=716.71,
    )

    curso.assert_fact(
        id=54,
        nome="JORNALISMO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=749.21,
    )

    curso.assert_fact(
        id=55,
        nome="LETRAS ALEMÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=698.18,
    )

    curso.assert_fact(
        id=56,
        nome="LETRAS ESPANHOL",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=663.25,
    )

    curso.assert_fact(
        id=57,
        nome="LETRAS FRANCÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=681.27,
    )

    curso.assert_fact(
        id=58,
        nome="LETRAS INGLÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=674.33,
    )

    curso.assert_fact(
        id=59,
        nome="LETRAS ITALIANO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="ABI",
        area=area_d["LLA"],
        nota_corte=691.31,
    )

    curso.assert_fact(
        id=60,
        nome="LETRAS PORTUGUÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado/licenciatura",
        area=area_d["LLA"],
        nota_corte=683.81,
    )

    curso.assert_fact(
        id=61,
        nome="MATEMÁTICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=682.46,
    )

    curso.assert_fact(
        id=62,
        nome="MATEMÁTICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=672.72,
    )

    curso.assert_fact(
        id=63,
        nome="MATEMÁTICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=749.46,
    )

    curso.assert_fact(
        id=64,
        nome="MATEMÁTICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="matutino",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=692.27,
    )

    curso.assert_fact(
        id=65,
        nome="MEDICINA",
        campus=campus_d["ARA"],
        duracao=12,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=817.27,
    )

    curso.assert_fact(
        id=66,
        nome="MEDICINA",
        campus=campus_d["FLN"],
        duracao=12,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=823.84,
    )

    curso.assert_fact(
        id=67,
        nome="METEOROLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=615.82,
    )

    curso.assert_fact(
        id=68,
        nome="MUSEOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=636.39,
    )

    curso.assert_fact(
        id=69,
        nome="NUTRIÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=771.11,
    )

    curso.assert_fact(
        id=70,
        nome="OCEANOGRAFIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=686.76,
    )

    curso.assert_fact(
        id=71,
        nome="ODONTOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=773.36,
    )

    curso.assert_fact(
        id=72,
        nome="PEDAGOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="licenciatura",
        area=area_d["CH"],
        nota_corte=683.93,
    )

    curso.assert_fact(
        id=73,
        nome="PSICOLOGIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado/licenciatura",
        area=area_d["CS"],
        nota_corte=770.51,
    )

    curso.assert_fact(
        id=74,
        nome="QUÍMICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=678.71,
    )

    curso.assert_fact(
        id=75,
        nome="QUÍMICA",
        campus=campus_d["BLU"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=699.15,
    )

    curso.assert_fact(
        id=76,
        nome="QUÍMICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="licenciatura",
        area=area_d["CET"],
        nota_corte=704.07,
    )

    curso.assert_fact(
        id=77,
        nome="QUÍMICA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=712.65,
    )

    curso.assert_fact(
        id=78,
        nome="RELAÇÕES INTERNACIONAIS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="vespertino",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=755.64,
    )

    curso.assert_fact(
        id=79,
        nome="SECRETARIADO EXECUTIVO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=680.78,
    )

    curso.assert_fact(
        id=80,
        nome="SERVIÇO SOCIAL",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CIA"],
        nota_corte=660.71,
    )

    curso.assert_fact(
        id=81,
        nome="SISTEMAS DE INFO.",
        campus=campus_d["FLN"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=739.73,
    )

    curso.assert_fact(
        id=82,
        nome="TEC. DA INFO. E COMUNICAÇÃO",
        campus=campus_d["ARA"],
        duracao=8,
        turno="noturno",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=705.96,
    )

    curso.assert_fact(
        id=83,
        nome="ZOOTECNIA",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=671.67,
    )

    curso.assert_fact(
        id=84,
        nome="ARQUITETURA E URBANISMO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=771.45,
    )

    curso.assert_fact(
        id=85,
        nome="CIÊNCIA DA COMPUTAÇÃO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CET"],
        nota_corte=809.98,
    )

    curso.assert_fact(
        id=86,
        nome="CIÊNCIA E TEC. DE ALIMENTOS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=669.67,
    )

    curso.assert_fact(
        id=87,
        nome="CIÊNCIAS BIOLÓGICAS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado/licenciatura",
        area=area_d["CB"],
        nota_corte=737.18,
    )

    curso.assert_fact(
        id=88,
        nome="DESIGN DE PRODUTO",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CS"],
        nota_corte=735.23,
    )

    curso.assert_fact(
        id=89,
        nome="ENG. CIVIL DE INFRAESTRUTURA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=729.74,
    )

    curso_engenharia.assert_fact(
        id=89, nome="ENG. CIVIL DE INFRAESTRUTURA", foco="infraestrutura"
    )

    curso.assert_fact(
        id=90,
        nome="ENG. DE AQUICULTURA",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=634.16,
    )

    curso_engenharia.assert_fact(
        id=90, nome="ENG. DE AQUICULTURA", foco="infraestrutura"
    )

    curso.assert_fact(
        id=91,
        nome="ENG. DE COMPUTAÇÃO",
        campus=campus_d["ARA"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=755.35,
    )
    
    curso_engenharia.assert_fact(id=91, nome="ENG. DE COMPUTAÇÃO", foco="elétrica")

    curso_engenharia.assert_fact(id=91, nome="ENG. DE COMPUTAÇÃO", foco="elétrica")

    curso.assert_fact(
        id=92,
        nome="ENG. DE CONTROLE E AUTOMAÇÃO",
        campus=campus_d["BLU"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=695.91,
    )

    curso_engenharia.assert_fact(
        id=92, nome="ENG. DE CONTROLE E AUTOMAÇÃO", foco="elétrica"
    )

    curso.assert_fact(
        id=93,
        nome="ENG. DE CONTROLE E AUTOMAÇÃO",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=740.03,
    )

    curso_engenharia.assert_fact(
        id=93, nome="ENG. DE CONTROLE E AUTOMAÇÃO", foco="elétrica"
    )

    curso.assert_fact(
        id=94,
        nome="ENG. DE TRANSP. E LOG.",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=657.68,
    )

    curso_engenharia.assert_fact(
        id=94, nome="ENG. DE TRANSP. E LOG.", foco="infraestrutura"
    )

    curso.assert_fact(
        id=95,
        nome="ENG. FERROV. E METROVIÁRIA",
        campus=campus_d["JOI"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=673.48,
    )

    curso_engenharia.assert_fact(
        id=95, nome="ENG. FERROV. E METROVIÁRIA", foco="infraestrutura"
    )

    curso.assert_fact(
        id=96,
        nome="ENG. SANITÁRIA E AMBIENTAL",
        campus=campus_d["FLN"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["ENG"],
        nota_corte=687.61,
    )

    curso_engenharia.assert_fact(
        id=96, nome="ENG. SANITÁRIA E AMBIENTAL", foco="infraestrutura"
    )

    curso.assert_fact(
        id=97,
        nome="LETRAS PORTUGUÊS",
        campus=campus_d["FLN"],
        duracao=8,
        turno="integral",
        tipo="bacharelado/licenciatura",
        area=area_d["LLA"],
        nota_corte=665.45,
    )

    curso.assert_fact(
        id=98,
        nome="MEDICINA VETERINÁRIA",
        campus=campus_d["CUR"],
        duracao=10,
        turno="integral",
        tipo="bacharelado",
        area=area_d["CA"],
        nota_corte=737.53,
    )
