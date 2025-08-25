import pdfplumber
import re


def read_pdf(file_path):
    whole_text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    whole_text += text + "\n"
    except Exception as e:
        raise Exception(f"File not found{e}")

    return whole_text


def guess_duration(name, type):
    name = name.upper()

    set_durations = {
        "MEDICINA": 12,
        "MEDICINA VETERINÁRIA": 10,
        "ODONTOLOGIA": 10,
        "FARMÁCIA": 10,
        "PSICOLOGIA": 10,
        "ARQUITETURA": 10,
        "DIREITO": 10,
    }

    for course, duration in set_durations.items():
        if course in name:
            return duration

    if type == "licenciatura":
        return 8
    elif "ENG" in name:
        return 10
    else:
        return 8


def classify_area(course_name):
    course_name = course_name.upper()

    areas = {
        "CIÊNCIAS EXATAS E DA TERRA": [
            "MATEMÁTICA",
            "FÍSICA",
            "QUÍMICA",
            "CIÊNCIAS DA COMPUTAÇÃO",
            "GEOLOGIA",
            "OCEANOGRAFIA",
            "METEOROLOGIA",
            "SISTEMAS DE INFORMAÇÃO",
            "TECNOLOGIAS DA INFORMAÇÃO E COMUNICAÇÃO",
            "CIÊNCIA E TECNOLOGIA",
        ],
        "CIÊNCIAS BIOLÓGICAS": ["CIÊNCIAS BIOLÓGICAS"],
        "CIÊNCIAS DA SAÚDE": [
            "MEDICINA",
            "ODONTOLOGIA",
            "ENFERMAGEM",
            "FARMÁCIA",
            "PSICOLOGIA",
            "EDUCAÇÃO FÍSICA",
            "NUTRIÇÃO",
            "FONOAUDIOLOGIA",
            "FISIOTERAPIA",
        ],
        "CIÊNCIAS AGRÁRIAS": [
            "AGRONOMIA",
            "ENGENHARIA DE AQUICULTURA",
            "ENGENHARIA FLORESTAL",
            "ZOOTECNIA",
            "MEDICINA VETERINÁRIA",
            "CIÊNCIA E TECNOLOGIA DE ALIMENTOS",
        ],
        "ENGENHARIAS": [
            "ENGENHARIA",  # cobre todas as engenharias
        ],
        "CIÊNCIAS HUMANAS": [
            "FILOSOFIA",
            "GEOGRAFIA",
            "HISTÓRIA",
            "PEDAGOGIA",
            "ANTROPOLOGIA",
            "LICENCIATURA INDÍGENA",
        ],
        "CIÊNCIAS SOCIAIS APLICADAS": [
            "ADMINISTRAÇÃO",
            "DIREITO",
            "ECONOMIA",
            "CIÊNCIAS CONTÁBEIS",
            "ARQUITETURA",
            "ARQUIVOLOGIA",
            "BIBLIOTECONOMIA",
            "JORNALISMO",
            "MUSEOLOGIA",
            "DESIGN",
            "SERVIÇO SOCIAL",
            "RELAÇÕES INTERNACIONAIS",
            "SECRETARIADO EXECUTIVO",
            "CIÊNCIA DA INFORMAÇÃO",
            "CIÊNCIAS SOCIAIS",
        ],
        "LINGUÍSTICA, LETRAS E ARTES": [
            "LETRAS",
            "ARTES CÊNICAS",
            "ANIMAÇÃO",
            "CINEMA",
        ],
    }

    for area, course in areas.items():
        for c in course:
            if c in course_name:
                return area

    return "OUTRAS"


def process_data(data):
    processed_data = []
    old_data = data.split("\n")

    for line in old_data:
        line = line.strip()

        if not line or any(
            word in line.upper()
            for word in [
                "COD CURSO CAMPUS",
                "LEGENDAS",
                "CATEGORIA",
                "UNIVERSIDADE FEDERAL",
                "COMISSÃO",
                "NOTAS MÁXIMAS",
                "Max Min",
                "3 / AC",
            ]
        ):
            continue

        if re.match(r"^\d+\s", line):
            try:
                match = re.search(
                    r"^(\d+)\s+(.+?)\s+(FLORIANÓPOLIS|CURITIBANOS|JOINVILLE|ARARANGUÁ|BLUMENAU)\s+(.+)",
                    line,
                )

                if match:
                    info = match.group(2)
                    info = info.split(" - ")
                    nome = info[0]
                    if nome != "LETRAS":
                        turno = info[2]
                        tipo = info[1]
                    else:
                        nome += " " + info[1]
                        turno = info[3]
                        tipo = info[2]
                    if len(turno.split()) != 1:
                        turno = turno.split()[0]
                    campus = match.group(3)
                    resto_linha = match.group(4)

                    notas = re.findall(r"\d+,\d+", resto_linha)

                    if len(notas) >= 2:
                        nota_corte = notas[1]

                        processed_data.append(
                            {
                                "curso": nome,
                                "campus": campus,
                                "duracao": guess_duration(nome, tipo),
                                "turno": turno,
                                "tipo": tipo,
                                "area": classify_area(nome),
                                "nota_corte": nota_corte,
                            }
                        )
            except Exception:
                # Em caso de erro, continua para a próxima linha
                continue

    return processed_data


def extract_data_clips(file_path):
    text = ""
    data = []

    try:
        text = read_pdf(file_path)
    except Exception:
        print("Erro no tratamento de dados")
        return

    try:
        data = process_data(text)

        if not data:
            print("No data was extracted")
            return
    except Exception:
        print("Error processing data")
        return

    for course in data:
        print(f"""
                  curso.assert_fact(nome='{course["curso"]}',
                                    campus='{course["campus"]},
                                    duracao='{course["duracao"]}',
                                    turno='{course["turno"]}'
                                    tipo='{course["tipo"]}'
                                    area='{course["area"]}'
                                    nota_corte='{course["nota_corte"]}')""")


if __name__ == "__main__":
    # df = extract_data("/home/caiofc/Documentos/notas-maximas-minimas-sisu2024.pdf")
    # df.to_csv("cursos.csv", index=False)

    extract_data_clips("data/notas-maximas-minimas-sisu2024.pdf")
