from template import create_environment_with_templates, campus_d, area_d
from cursos import add_cursos_facts
from regras import add_rules


def main():
    env = create_environment_with_templates()
    add_cursos_facts(env)

    
    # Coleta de dados via input
    preferencia_turno = input("Preferência de turno [matutino, vespertino, noturno, integral]: ")
    nota_enem = float(input("Nota ENEM: "))
    
    # Coleta áreas e converte abreviações
    print("\nÁreas disponíveis:")
    for sigla, nome in area_d.items():
        print(f"  {sigla}: {nome}")

    areas_input = input("Áreas de interesse (separadas por vírgula): ").split(",")
    areas_interesse = []


    for area in areas_input:
        area = area.strip().upper()
        if area in area_d:
            areas_interesse.append(area_d[area])
        else:
            areas_interesse.append(area)

    foco = ""
    if "Engenharias" in areas_interesse:
        foco = input("Foco em Engenharia: ")

    # Coleta locais e converte abreviações
    print("\nCampi disponíveis:")
    for sigla, nome in campus_d.items():
        print(f"  {sigla}: {nome}")

    locais_input = input("Locais de interesse (separados por vírgula): ").split(",")
    locais_interesse = []
    for local in locais_input:
        local = local.strip().upper()
        if local in campus_d:
            locais_interesse.append(campus_d[local])
        else:
            locais_interesse.append(local)

    tipo_preferencia = input("Tipo de preferência [bacharelado/licenciatura/abi]: ")
    duracao_preferencia = int(input("Duração máxima do curso: "))

    # Formatação mais limpa usando aspas duplas para a string externa
    # e aspas simples para os valores internos
    areas_str = " ".join([f'"{area}"' for area in areas_interesse])
    locais_str = " ".join([f'"{local}"' for local in locais_interesse])
    
    fact_string = (
        f'(perfil '
        f'(preferencia_turno "{preferencia_turno.strip()}") '
        f'(nota_enem {nota_enem}) '
        f'(areas_interesse {areas_str}) '
        f'(locais_interesse {locais_str}) '
        f'(tipo_preferencia "{tipo_preferencia.strip()}") '
        f'(duracao_preferencia {duracao_preferencia}))'
    )
    
    env.assert_string(fact_string)
    
    if "Engenharias" in areas_interesse:
        env.assert_string(
            f'(perfil-engenharia '
            f'(cpf 1) ' # usando 1 como ID temporário
            f'(foco_preferencia "{foco}"))'
        )

    add_rules(env)
    env.run()


if __name__ == "__main__":
    main()