def add_rules(env):
    """Define the rules for the env"""

    #  env.build("""
    #  (defrule recomendar-curso-por-turno
    #     (perfil (preferencia_turno ?turno))
    #     (curso (nome ?n) (turno ?turno))
    #     =>
    #     (printout t "Recomendação por turno preferido: " ?n " - " ?turno crlf))
    #  """)

    #  env.build("""
    #  (defrule recomendar-curso-por-nota
    #     (perfil (nota_enem ?ne))
    #     (curso (nome ?n) (nota_corte ?nc))
    #     (test (<= ?nc ?ne))
    #     =>
    #     (printout t "Curso possível com sua nota: " ?n " (Nota de corte: " ?nc ")" crlf))
    #  """)

    env.build("""
      (defrule criar-engenharia-default
         (declare (salience 100))
         (curso
            (nome ?n)
            (area "Engenharias"))
         (not (curso-engenharia (nome ?n)))
         =>
         (assert (curso-engenharia
            (nome ?n)
            (foco "geral")
            (intensidade_matematica "alta")
            (laboratorio TRUE)))
         (printout t "DEBUG: Criado perfil de engenharia padrão para: " ?n crlf))
      """)

    env.build("""
   (defrule recomendar-curso-engenharia
      (declare (salience 50))
      (perfil
         (preferencia_turno ?turno)
         (nota_enem ?ne)
         (areas_interesse $? ?area $?)
         (locais_interesse $? ?campus $?)
         (duracao_preferencia ?d)
         (tipo_preferencia ?t))
      (curso
         (nome ?n)
         (campus ?campus)
         (duracao ?d)
         (turno ?turno)
         (tipo ?t)
         (area "Engenharias")
         (nota_corte ?nc))
      (curso-engenharia
         (nome ?n)
         (foco ?f)
         (intensidade_matematica ?im)
         (laboratorio ?lab))
      (test (<= ?nc ?ne))
      (test (eq ?area "Engenharias"))
      (test (or (eq ?tipoCurso ?t)
      (neq (str-index ?t ?tipoCurso) FALSE)))
      =>
      (printout t "======================================" crlf)
      (printout t "CURSO DE ENGENHARIA ENCONTRADO!" crlf)
      (printout t "======================================" crlf)
      (printout t "Nome: " ?n crlf)
      (printout t "Campus: " ?campus crlf)
      (printout t "Área: Engenharias" crlf)
      (printout t "Duração: " ?d " semestres" crlf)
      (printout t "Turno: " ?turno crlf)
      (printout t "Tipo: " ?t crlf)
      (printout t "Nota de Corte: " ?nc crlf)
      (printout t "Sua Nota ENEM: " ?ne crlf)
      (printout t "---------- DETALHES ENGENHARIA ----------" crlf)
      (printout t "Foco: " ?f crlf)
      (printout t "Intensidade Matemática: " ?im crlf)
      (printout t "Requer Laboratório: " ?lab crlf)
      (printout t "------------------------------------------" crlf)
      (printout t "======================================" crlf)
      (printout t crlf)
      (assert (curso-processado ?n)))
   """)

    env.build("""
   (defrule recomendar-curso-geral
      (declare (salience 10))
      (perfil
         (preferencia_turno ?turno)
         (nota_enem ?ne)
         (areas_interesse $? ?area $?)
         (locais_interesse $? ?campus $?)
         (duracao_preferencia ?d)
         (tipo_preferencia ?t))
      (curso
         (nome ?n)
         (campus ?campus)
         (duracao ?d)
         (turno ?turno)
         (tipo ?t)
         (area ?area)
         (nota_corte ?nc))
      (test (<= ?nc ?ne))
      (not (curso-processado ?n))
      (test (neq ?area "Engenharias"))
      (test (or (eq ?tipoCurso ?t)
      (neq (str-index ?t ?tipoCurso) FALSE)))
      =>
      (printout t "======================================" crlf)
      (printout t "CURSO IDEAL ENCONTRADO!" crlf)
      (printout t "======================================" crlf)
      (printout t "Nome: " ?n crlf)
      (printout t "Campus: " ?campus crlf)
      (printout t "Área: " ?area crlf)
      (printout t "Duração: " ?d " semestres" crlf)
      (printout t "Turno: " ?turno crlf)
      (printout t "Tipo: " ?t crlf)
      (printout t "Nota de Corte: " ?nc crlf)
      (printout t "Sua Nota ENEM: " ?ne crlf)
      (printout t "======================================" crlf)
      (printout t crlf)
      (assert (curso-processado ?n)))
   """)
