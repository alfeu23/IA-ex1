def add_rules(env):
    """Add all recommendation rules to the CLIPS environment"""
    
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

    env.build("""
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
    """)