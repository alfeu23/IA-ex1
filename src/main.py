from template import create_environment_with_templates, campus_dict, areas_dict, tipos_dict, focos_engenharia_dict, turnos_dict
from cursos import add_cursos_facts
from regras import add_rules


def choose_option(title: str, options: dict, multiple=False):
    print(f"{title}")
    for num, option in options.items():
        print(f"{num}: {option}")

    while True:
        try:
            if multiple:
                entry = input(f"Digite os números das opções desejadas (separados por vírgula): ")
                num = [int(n.strip()) for n in entry.split(",")]
                invalid = [n for n in num if n not in options]
                
                if invalid:
                    print(f"Números inválidos: {invalid}. Escolha entre {list(options.keys())}.")
                    continue
                
                return [options[n] for n in num]
            else:
                num = int(input(f"Digite o número da opção desejada: "))
                if num in options:
                    return options[num]
                else:
                    print(f"Número inválido. Escolha entre {list(options.keys())}.")
        except ValueError:
            print("Escolha entre as opcoes!")


def main():
    env = create_environment_with_templates()
    add_cursos_facts(env)

    # Coleta de dados
    preferencia_turno = choose_option("Preferência de turno", turnos_dict)
    
    nota_enem = float(input("\nNota ENEM (com pontos decimais): "))
    
    areas_interesse = choose_option("Áreas de interesse", areas_dict, multiple=True)
    
    foco = ""
    if "Engenharias" in areas_interesse:
        foco = choose_option("Foco em Engenharia", focos_engenharia_dict)
    
    locais_interesse = choose_option("Locais de interesse", campus_dict, multiple=True)
    
    tipo_preferencia = choose_option("Tipo de preferência", tipos_dict)
    
    duracao_preferencia = int(input("\nDuração máxima do curso: "))

    # Formatação para o sistema de regras
    areas_str = " ".join([f'"{area}"' for area in areas_interesse])
    locais_str = " ".join([f'"{local}"' for local in locais_interesse])
    fact_string = (
        f"(perfil "
        f'(preferencia_turno "{preferencia_turno.strip()}") '
        f"(nota_enem {nota_enem}) "
        f"(areas_interesse {areas_str}) "
        f"(locais_interesse {locais_str}) "
        f'(tipo_preferencia "{tipo_preferencia.strip()}") '
        f"(duracao_preferencia {duracao_preferencia}))"
    )

    env.assert_string(fact_string)

    if "Engenharias" in areas_interesse:
        env.assert_string(f'(perfil-engenharia (foco_preferencia "{foco}"))')

    add_rules(env)
    env.run()


if __name__ == "__main__":
    main()
