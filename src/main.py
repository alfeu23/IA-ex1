from template import create_environment_with_templates, campus_d, area_d
from cursos import add_cursos_facts
from regras import add_rules


def main():
    env = create_environment_with_templates()

    add_cursos_facts(env)

    perfil = env.find_template("perfil")
    perfil.assert_fact(
        preferencia_turno="integral",
        nota_enem=780.00,
        areas_interesse=[area_d["CS"], area_d["CET"]],
        locais_interesse=[campus_d["FLN"], campus_d["CUR"]],
        tipo_preferencia="bacharelado",
        duracao_preferencia=10,
    )

    # Add rules
    add_rules(env)

    # Run the system
    env.run()


if __name__ == "__main__":
    main()
