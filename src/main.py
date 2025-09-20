from template import (
    create_environment_with_templates,
    campus_dict,
    areas_dict,
    tipos_dict,
    focos_engenharia_dict,
    turnos_dict,
    categorias_profissao_dict,
    setores_profissao_dict,
    autonomia_dict,
)
from cursos import add_cursos_facts
from profissao import add_profissoes_facts
from regras import add_rules


def choose_option(title: str, options: dict, multiple=False):
    print(f"{title}")
    for num, option in options.items():
        print(f"{num}: {option}")

    while True:
        try:
            if multiple:
                entry = input(
                    "\nDigite os números das opções desejadas (separados por vírgula): "
                )
                num = [int(n.strip()) for n in entry.split(",")]
                invalid = [n for n in num if n not in options]

                if invalid:
                    print(
                        f"Números inválidos: {invalid}. Escolha entre {list(options.keys())}."
                    )
                    continue

                return [options[n] for n in num]
            else:
                num = int(input("\nDigite o número da opção desejada: "))
                if num in options:
                    return options[num]
                else:
                    print(f"Número inválido. Escolha entre {list(options.keys())}.")
        except ValueError:
            print("Escolha entre as opcoes!")


def main():
    env = create_environment_with_templates()
    add_cursos_facts(env)
    add_profissoes_facts(env)

    # Etapa Academica
    print("="*60)
    print("SISTEMA DE RECOMENDAÇÃO DE CURSOS UFSC")
    print("="*60)
    print("ETAPA 1: PREFERÊNCIAS ACADÊMICAS")
    print("="*60)

    preferencia_turno = choose_option("\nPreferência de turno", turnos_dict)

    nota_enem = float(input("\nNota ENEM (com pontos decimais): "))

    areas_interesse = choose_option("\nÁreas de interesse", areas_dict, multiple=True)

    foco = ""
    if "Engenharias" in areas_interesse:
        foco = choose_option("\nFoco em Engenharia", focos_engenharia_dict)

    locais_interesse = choose_option(
        "\nLocais de interesse", campus_dict, multiple=True
    )

    tipo_preferencia = choose_option("\nTipo de preferência", tipos_dict)

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
    
    print("\n" + "="*60)
    print("CURSOS COMPATÍVEIS COM SEU PERFIL:")
    print("="*60)
    
    env.run()

    curso_recomendado_facts = list(env.facts())
    cursos_recomendados = [fact for fact in curso_recomendado_facts if fact.template.name == "curso-recomendado"]
    
    if not cursos_recomendados:
        print("\nNenhum curso encontrado com suas preferências. Tente ajustar seus critérios.")
        return

    # Etapa de carreira
    print("\n" + "="*60)
    print("ETAPA 2: PREFERÊNCIAS DE CARREIRA")
    print("="*60)
    print("Agora vamos encontrar o curso IDEAL baseado em seus objetivos profissionais:")
    
    categorias_interesse = choose_option(
        "\nCategorias profissionais de interesse", 
        categorias_profissao_dict, 
        multiple=True
    )
    
    setores_interesse = choose_option(
        "\nSetores de interesse", 
        setores_profissao_dict, 
        multiple=True
    )
    
    salario_minimo = float(input("\nSalário mínimo desejado (R$): "))
    
    autonomia_desejada = choose_option(
        "\nNível de autonomia desejado", 
        autonomia_dict
    )

    categorias_str = " ".join([f'"{categoria}"' for categoria in categorias_interesse])
    setores_str = " ".join([f'"{setor}"' for setor in setores_interesse])
    
    perfil_profissional_string = (
        f"(perfil-profissional "
        f"(categorias_interesse {categorias_str}) "
        f"(setores_interesse {setores_str}) "
        f"(salario_minimo_desejado {salario_minimo}) "
        f'(autonomia_desejada "{autonomia_desejada}"))'
    )

    env.assert_string(perfil_profissional_string)

    print("\n" + "="*60)
    print("CURSO(S) IDEAL(IS) PARA SUA CARREIRA:")
    print("="*60)
    
    env.run()

    curso_ideal_facts = list(env.facts())
    cursos_ideais = [fact for fact in curso_ideal_facts if fact.template.name == "curso-ideal"]
    
    if not cursos_ideais:
        print
        print("\n O seu plano de carreira nao se adequa ao seu curso.")
        print("\n Por favor faca novas escolhas.")


if __name__ == "__main__":
    main()