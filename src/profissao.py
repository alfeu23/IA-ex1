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
    
    profissao.assert_fact(
        id=13,
        nome="Farmacêutico",
        categoria="liberal",
        setor="saude",
        salario_medio=6500.0,
        nivel_autonomia="alto",
        descricao="Manipula medicamentos, orienta sobre uso correto de fármacos e atua em farmácias"
    )

    curso_profissao.assert_fact(
        curso_nome="FARMÁCIA",
        profissao_nome="Farmacêutico",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=14,
        nome="Nutricionista",
        categoria="privado",
        setor="saude",
        salario_medio=4500.0,
        nivel_autonomia="medio",
        descricao="Planeja dietas, orienta sobre alimentação saudável e atua em hospitais e clínicas"
    )

    curso_profissao.assert_fact(
        curso_nome="NUTRIÇÃO",
        profissao_nome="Nutricionista",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=15,
        nome="Psicólogo",
        categoria="liberal",
        setor="saude",
        salario_medio=5500.0,
        nivel_autonomia="alto",
        descricao="Atende pacientes, realiza terapias e avaliações psicológicas"
    )

    curso_profissao.assert_fact(
        curso_nome="PSICOLOGIA",
        profissao_nome="Psicólogo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=16,
        nome="Fisioterapeuta",
        categoria="privado",
        setor="saude",
        salario_medio=4800.0,
        nivel_autonomia="medio",
        descricao="Realiza reabilitação física, trata lesões e problemas motores"
    )

    curso_profissao.assert_fact(
        curso_nome="FISIOTERAPIA",
        profissao_nome="Fisioterapeuta",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=17,
        nome="Fonoaudiólogo",
        categoria="privado",
        setor="saude",
        salario_medio=4200.0,
        nivel_autonomia="medio",
        descricao="Trata distúrbios da comunicação, fala e audição"
    )

    curso_profissao.assert_fact(
        curso_nome="FONOAUDIOLOGIA",
        profissao_nome="Fonoaudiólogo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=18,
        nome="Arquiteto",
        categoria="liberal",
        setor="engenharia",
        salario_medio=8500.0,
        nivel_autonomia="alto",
        descricao="Projeta edificações, planeja espaços urbanos e coordena obras"
    )

    curso_profissao.assert_fact(
        curso_nome="ARQUITETURA E URBANISMO",
        profissao_nome="Arquiteto",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=19,
        nome="Designer Gráfico",
        categoria="autonomo",
        setor="arte",
        salario_medio=4000.0,
        nivel_autonomia="alto",
        descricao="Cria identidades visuais, layouts e materiais gráficos"
    )

    curso_profissao.assert_fact(
        curso_nome="DESIGN",
        profissao_nome="Designer Gráfico",
        requisitos_adicionais="portfolio"
    )

    curso_profissao.assert_fact(
        curso_nome="DESIGN DE PRODUTO",
        profissao_nome="Designer Gráfico",
        requisitos_adicionais="portfolio"
    )

    profissao.assert_fact(
        id=20,
        nome="Contador",
        categoria="liberal",
        setor="administracao",
        salario_medio=5500.0,
        nivel_autonomia="alto",
        descricao="Gerencia contabilidade de empresas, elabora demonstrações financeiras"
    )

    curso_profissao.assert_fact(
        curso_nome="CIÊNCIAS CONTÁBEIS",
        profissao_nome="Contador",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=21,
        nome="Economista",
        categoria="privado",
        setor="administracao",
        salario_medio=7500.0,
        nivel_autonomia="alto",
        descricao="Analisa mercados, elabora relatórios econômicos e assessora investimentos"
    )

    curso_profissao.assert_fact(
        curso_nome="CIÊNCIAS ECONÔMICAS",
        profissao_nome="Economista",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=22,
        nome="Engenheiro Elétrico",
        categoria="privado",
        setor="engenharia",
        salario_medio=9500.0,
        nivel_autonomia="medio",
        descricao="Projeta sistemas elétricos, desenvolve equipamentos eletrônicos"
    )

    engenharias_eletricas = ["ENG. ELÉTRICA", "ENG. ELETRÔNICA", "ENG. DE ENERGIA", 
                           "ENG. DE CONTROLE E AUTOMAÇÃO", "ENG. MECATRÔNICA"]
    
    for curso in engenharias_eletricas:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Engenheiro Elétrico",
            requisitos_adicionais="registro_crea"
        )

    profissao.assert_fact(
        id=23,
        nome="Engenheiro Mecânico",
        categoria="privado",
        setor="engenharia",
        salario_medio=9200.0,
        nivel_autonomia="medio",
        descricao="Projeta máquinas, sistemas mecânicos e processos industriais"
    )

    engenharias_mecanicas = ["ENG. MECÂNICA", "ENG. AUTOMOTIVA", "ENG. AEROESPACIAL", 
                           "ENG. MECATRÔNICA", "ENG. NAVAL"]
    
    for curso in engenharias_mecanicas:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Engenheiro Mecânico",
            requisitos_adicionais="registro_crea"
        )

    profissao.assert_fact(
        id=24,
        nome="Engenheiro de Materiais",
        categoria="privado",
        setor="engenharia",
        salario_medio=8800.0,
        nivel_autonomia="medio",
        descricao="Desenvolve novos materiais, testa propriedades e otimiza processos"
    )

    engenharias_materiais = ["ENG. DE MATERIAIS", "ENG. TÊXTIL", "ENG. DE ALIMENTOS", "ENG. QUÍMICA"]
    
    for curso in engenharias_materiais:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Engenheiro de Materiais",
            requisitos_adicionais="registro_crea"
        )

    profissao.assert_fact(
        id=25,
        nome="Veterinário",
        categoria="liberal",
        setor="agrario",
        salario_medio=6000.0,
        nivel_autonomia="alto",
        descricao="Cuida da saúde animal, realiza cirurgias veterinárias"
    )

    curso_profissao.assert_fact(
        curso_nome="MEDICINA VETERINÁRIA",
        profissao_nome="Veterinário",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=26,
        nome="Agrônomo",
        categoria="privado",
        setor="agrario",
        salario_medio=6500.0,
        nivel_autonomia="medio",
        descricao="Planeja e supervisiona cultivos, desenvolve técnicas agrícolas"
    )

    curso_profissao.assert_fact(
        curso_nome="AGRONOMIA",
        profissao_nome="Agrônomo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=27,
        nome="Zootecnista",
        categoria="privado",
        setor="agrario",
        salario_medio=5500.0,
        nivel_autonomia="medio",
        descricao="Gerencia criação de animais, desenvolve técnicas de produção animal"
    )

    curso_profissao.assert_fact(
        curso_nome="ZOOTECNIA",
        profissao_nome="Zootecnista",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=28,
        nome="Cinematógrafo",
        categoria="autonomo",
        setor="arte",
        salario_medio=5000.0,
        nivel_autonomia="alto",
        descricao="Produz filmes, dirige, edita e cria conteúdo audiovisual"
    )

    curso_profissao.assert_fact(
        curso_nome="CINEMA",
        profissao_nome="Cinematógrafo",
        requisitos_adicionais="portfolio"
    )

    profissao.assert_fact(
        id=29,
        nome="Animador",
        categoria="autonomo",
        setor="arte",
        salario_medio=4500.0,
        nivel_autonomia="alto",
        descricao="Cria animações para filmes, jogos e publicidade"
    )

    curso_profissao.assert_fact(
        curso_nome="ANIMAÇÃO",
        profissao_nome="Animador",
        requisitos_adicionais="portfolio"
    )

    profissao.assert_fact(
        id=30,
        nome="Ator",
        categoria="autonomo",
        setor="arte",
        salario_medio=3500.0,
        nivel_autonomia="alto",
        descricao="Atua em peças teatrais, filmes e produções audiovisuais"
    )

    curso_profissao.assert_fact(
        curso_nome="ARTES CÊNICAS",
        profissao_nome="Ator",
        requisitos_adicionais="experiencia_artistica"
    )

    profissao.assert_fact(
        id=31,
        nome="Bibliotecário",
        categoria="publico",
        setor="educacao",
        salario_medio=4000.0,
        nivel_autonomia="medio",
        descricao="Organiza acervos, orienta pesquisas e gerencia bibliotecas"
    )

    curso_profissao.assert_fact(
        curso_nome="BIBLIOTECONOMIA",
        profissao_nome="Bibliotecário",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=32,
        nome="Arquivista",
        categoria="publico",
        setor="administracao",
        salario_medio=4200.0,
        nivel_autonomia="medio",
        descricao="Organiza e preserva documentos históricos e institucionais"
    )

    curso_profissao.assert_fact(
        curso_nome="ARQUIVOLOGIA",
        profissao_nome="Arquivista",
        requisitos_adicionais="concurso_publico"
    )

    profissao.assert_fact(
        id=33,
        nome="Cientista de Dados",
        categoria="privado",
        setor="tecnologia",
        salario_medio=12000.0,
        nivel_autonomia="medio",
        descricao="Analisa grandes volumes de dados, cria modelos preditivos"
    )

    cursos_dados = ["CIÊNCIA DA COMPUTAÇÃO", "SISTEMAS DE INFO.", "MATEMÁTICA", 
                   "FÍSICA", "CIÊNCIA DA INFO."]
    
    for curso in cursos_dados:
        curso_profissao.assert_fact(
            curso_nome=curso,
            profissao_nome="Cientista de Dados",
            requisitos_adicionais="especializacao_dados"
        )

    profissao.assert_fact(
        id=34,
        nome="Físico",
        categoria="academico",
        setor="ciencias",
        salario_medio=7000.0,
        nivel_autonomia="alto",
        descricao="Pesquisa fenômenos físicos, desenvolve teorias e aplicações"
    )

    curso_profissao.assert_fact(
        curso_nome="FÍSICA",
        profissao_nome="Físico",
        requisitos_adicionais="pos_graduacao"
    )

    profissao.assert_fact(
        id=35,
        nome="Químico",
        categoria="privado",
        setor="ciencias",
        salario_medio=6500.0,
        nivel_autonomia="medio",
        descricao="Desenvolve produtos químicos, analisa substâncias e processos"
    )

    curso_profissao.assert_fact(
        curso_nome="QUÍMICA",
        profissao_nome="Químico",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=36,
        nome="Geólogo",
        categoria="privado",
        setor="ciencias",
        salario_medio=8000.0,
        nivel_autonomia="medio",
        descricao="Estuda rochas, minerais e formações geológicas"
    )

    curso_profissao.assert_fact(
        curso_nome="GEOLOGIA",
        profissao_nome="Geólogo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=37,
        nome="Oceanógrafo",
        categoria="academico",
        setor="ciencias",
        salario_medio=6000.0,
        nivel_autonomia="alto",
        descricao="Estuda oceanos, vida marinha e fenômenos aquáticos"
    )

    curso_profissao.assert_fact(
        curso_nome="OCEANOGRAFIA",
        profissao_nome="Oceanógrafo",
        requisitos_adicionais="pos_graduacao"
    )

    profissao.assert_fact(
        id=38,
        nome="Meteorologista",
        categoria="publico",
        setor="ciencias",
        salario_medio=7500.0,
        nivel_autonomia="medio",
        descricao="Estuda clima e tempo, faz previsões meteorológicas"
    )

    curso_profissao.assert_fact(
        curso_nome="METEOROLOGIA",
        profissao_nome="Meteorologista",
        requisitos_adicionais="concurso_publico"
    )

    profissao.assert_fact(
        id=39,
        nome="Museólogo",
        categoria="publico",
        setor="arte",
        salario_medio=4500.0,
        nivel_autonomia="medio",
        descricao="Gerencia museus, organiza exposições e preserva patrimônio cultural"
    )

    curso_profissao.assert_fact(
        curso_nome="MUSEOLOGIA",
        profissao_nome="Museólogo",
        requisitos_adicionais="concurso_publico"
    )

    profissao.assert_fact(
        id=40,
        nome="Geógrafo",
        categoria="publico",
        setor="ciencias",
        salario_medio=5000.0,
        nivel_autonomia="medio",
        descricao="Analisa território, planeja uso do solo e estuda fenômenos espaciais"
    )

    curso_profissao.assert_fact(
        curso_nome="GEOGRAFIA",
        profissao_nome="Geógrafo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=41,
        nome="Historiador",
        categoria="academico",
        setor="educacao",
        salario_medio=4800.0,
        nivel_autonomia="alto",
        descricao="Pesquisa e documenta eventos históricos, preserva memória"
    )

    curso_profissao.assert_fact(
        curso_nome="HISTÓRIA",
        profissao_nome="Historiador",
        requisitos_adicionais="pos_graduacao"
    )

    profissao.assert_fact(
        id=42,
        nome="Filósofo",
        categoria="academico",
        setor="educacao",
        salario_medio=5000.0,
        nivel_autonomia="alto",
        descricao="Desenvolve teorias filosóficas, ensina e pesquisa pensamento crítico"
    )

    curso_profissao.assert_fact(
        curso_nome="FILOSOFIA",
        profissao_nome="Filósofo",
        requisitos_adicionais="pos_graduacao"
    )

    profissao.assert_fact(
        id=43,
        nome="Antropólogo",
        categoria="academico",
        setor="ciencias",
        salario_medio=5500.0,
        nivel_autonomia="alto",
        descricao="Estuda culturas e sociedades humanas"
    )

    curso_profissao.assert_fact(
        curso_nome="ANTROPOLOGIA",
        profissao_nome="Antropólogo",
        requisitos_adicionais="pos_graduacao"
    )

    profissao.assert_fact(
        id=44,
        nome="Diplomata",
        categoria="publico",
        setor="administracao",
        salario_medio=20000.0,
        nivel_autonomia="alto",
        descricao="Representa o país em relações internacionais e negociações"
    )

    curso_profissao.assert_fact(
        curso_nome="RELAÇÕES INTERNACIONAIS",
        profissao_nome="Diplomata",
        requisitos_adicionais="concurso_publico"
    )

    profissao.assert_fact(
        id=45,
        nome="Secretário Executivo",
        categoria="privado",
        setor="administracao",
        salario_medio=4500.0,
        nivel_autonomia="medio",
        descricao="Assessora executivos, organiza agendas e coordena reuniões"
    )

    curso_profissao.assert_fact(
        curso_nome="SECRETARIADO EXECUTIVO",
        profissao_nome="Secretário Executivo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=46,
        nome="Assistente Social",
        categoria="publico",
        setor="administracao",
        salario_medio=4000.0,
        nivel_autonomia="medio",
        descricao="Atende famílias em vulnerabilidade, desenvolve projetos sociais"
    )

    curso_profissao.assert_fact(
        curso_nome="SERVIÇO SOCIAL",
        profissao_nome="Assistente Social",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=47,
        nome="Biólogo",
        categoria="academico",
        setor="ciencias",
        salario_medio=5500.0,
        nivel_autonomia="alto",
        descricao="Estuda seres vivos, ecossistemas e biodiversidade"
    )

    curso_profissao.assert_fact(
        curso_nome="CIÊNCIAS BIOLÓGICAS",
        profissao_nome="Biólogo",
        requisitos_adicionais="registro_profissional"
    )

    profissao.assert_fact(
        id=48,
        nome="Engenheiro Florestal",
        categoria="privado",
        setor="agrario",
        salario_medio=7000.0,
        nivel_autonomia="medio",
        descricao="Gerencia florestas, desenvolve projetos de reflorestamento"
    )

    curso_profissao.assert_fact(
        curso_nome="ENG. FLORESTAL",
        profissao_nome="Engenheiro Florestal",
        requisitos_adicionais="registro_crea"
    )

    profissao.assert_fact(
        id=49,
        nome="Engenheiro de Produção",
        categoria="privado",
        setor="engenharia",
        salario_medio=9000.0,
        nivel_autonomia="medio",
        descricao="Otimiza processos produtivos, gerencia qualidade e logística"
    )

    curso_profissao.assert_fact(
        curso_nome="ENG. DE PRODUÇÃO",
        profissao_nome="Engenheiro de Produção",
        requisitos_adicionais="registro_crea"
    )