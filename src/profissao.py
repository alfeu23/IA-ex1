def add_profissoes_facts(env):
    """Add profession facts to the environment"""
    profissao = env.find_template("profissao")
    curso_profissao = env.find_template("curso-profissao")

    profissao.assert_fact(
        id=1,
        nome="Médico",
        categoria="liberal",
        setor="saude",
        salario_medio=15000.0,
        nivel_autonomia="alto",
        descricao="Diagnóstica e trata doenças, realiza cirurgias e cuida da saúde dos pacientes"
    )

    curso_profissao.assert_fact(
        curso_nome="MEDICINA",
        profissao_nome="Médico",
        requisitos_adicionais="residencia_medica"
    )

    profissao.assert_fact(
        id=2,
        nome="Enfermeiro",
        categoria="privado",
        setor="saude",
        salario_medio=5000.0,
        nivel_autonomia="medio",
        descricao="Cuida de pacientes, administra medicamentos e coordena equipes de enfermagem"
    )

    curso_profissao.assert_fact(
        curso_nome="ENFERMAGEM",
        profissao_nome="Enfermeiro",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=3,
        nome="Dentista",
        categoria="liberal",
        setor="saude",
        salario_medio=8000.0,
        nivel_autonomia="alto",
        descricao="Cuida da saúde bucal, realiza procedimentos odontológicos"
    )

    curso_profissao.assert_fact(
        curso_nome="ODONTOLOGIA",
        profissao_nome="Dentista",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=4,
        nome="Advogado",
        categoria="liberal",
        setor="juridico",
        salario_medio=7000.0,
        nivel_autonomia="alto",
        descricao="Representa clientes em questões legais, elabora contratos e petições"
    )

    curso_profissao.assert_fact(
        curso_nome="DIREITO",
        profissao_nome="Advogado",
        requisitos_adicionais="exame_oab"
    )

    profissao.assert_fact(
        id=5,
        nome="Juiz",
        categoria="publico",
        setor="juridico",
        salario_medio=30000.0,
        nivel_autonomia="alto",
        descricao="Julga casos em tribunais, interpreta leis e toma decisões judiciais"
    )

    curso_profissao.assert_fact(
        curso_nome="DIREITO",
        profissao_nome="Juiz",
        requisitos_adicionais="concurso_publico"
    )

    profissao.assert_fact(
        id=6,
        nome="Desenvolvedor de Software",
        categoria="privado",
        setor="tecnologia",
        salario_medio=8000.0,
        nivel_autonomia="medio",
        descricao="Desenvolve aplicações, sistemas e software para diferentes plataformas"
    )

    curso_profissao.assert_fact(
        curso_nome="CIÊNCIA DA COMPUTAÇÃO",
        profissao_nome="Desenvolvedor de Software",
        requisitos_adicionais="experiencia_pratica"
    )

    curso_profissao.assert_fact(
        curso_nome="SISTEMAS DE INFO.",
        profissao_nome="Desenvolvedor de Software",
        requisitos_adicionais="experiencia_pratica"
    )

    curso_profissao.assert_fact(
        curso_nome="ENG. DE COMPUTAÇÃO",
        profissao_nome="Desenvolvedor de Software",
        requisitos_adicionais="experiencia_pratica"
    )

    profissao.assert_fact(
        id=7,
        nome="Professor Universitário",
        categoria="academico",
        setor="educacao",
        salario_medio=8000.0,
        nivel_autonomia="alto",
        descricao="Ensina e pesquisa em universidades, orienta estudantes"
    )

    licenciaturas = ["CIÊNCIAS BIOLÓGICAS", "EDUCAÇÃO FÍSICA", "FILOSOFIA", "FÍSICA", 
                     "MATEMÁTICA", "QUÍMICA", "PEDAGOGIA", "LETRAS PORTUGUÊS"]
    
    for curso in licenciaturas:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Professor Universitário",
            requisitos_adicionais="mestrado_doutorado"
        )

    profissao.assert_fact(
        id=8,
        nome="Professor de Ensino Básico",
        categoria="publico",
        setor="educacao",
        salario_medio=4000.0,
        nivel_autonomia="medio",
        descricao="Ensina em escolas de ensino fundamental e médio"
    )

    for curso in licenciaturas:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Professor de Ensino Básico",
            requisitos_adicionais="concurso_publico"
        )

    profissao.assert_fact(
        id=9,
        nome="Engenheiro Civil",
        categoria="liberal",
        setor="engenharia",
        salario_medio=9000.0,
        nivel_autonomia="alto",
        descricao="Projeta e supervisiona construções, obras de infraestrutura"
    )

    curso_profissao.assert_fact(
        curso_nome="ENG. CIVIL",
        profissao_nome="Engenheiro Civil",
        requisitos_adicionais="registro_crea"
    )

    profissao.assert_fact(
        id=10,
        nome="Engenheiro de Software",
        categoria="privado",
        setor="tecnologia",
        salario_medio=12000.0,
        nivel_autonomia="medio",
        descricao="Arquiteta sistemas complexos, lidera equipes de desenvolvimento"
    )

    curso_profissao.assert_fact(
        curso_nome="ENG. DE COMPUTAÇÃO",
        profissao_nome="Engenheiro de Software",
        requisitos_adicionais="experiencia_tecnica"
    )

    profissao.assert_fact(
        id=11,
        nome="Gestor Empresarial",
        categoria="privado",
        setor="administracao",
        salario_medio=10000.0,
        nivel_autonomia="alto",
        descricao="Gerencia empresas, toma decisões estratégicas"
    )

    curso_profissao.assert_fact(
        curso_nome="ADMINISTRAÇÃO",
        profissao_nome="Gestor Empresarial",
        requisitos_adicionais="experiencia_gestao"
    )

    profissao.assert_fact(
        id=12,
        nome="Jornalista",
        categoria="privado",
        setor="comunicacao",
        salario_medio=4500.0,
        nivel_autonomia="medio",
        descricao="Produz conteúdo jornalístico, cobre eventos, entrevista pessoas"
    )

    curso_profissao.assert_fact(
        curso_nome="JORNALISMO",
        profissao_nome="Jornalista",
        requisitos_adicionais="registro_profissional"
    )