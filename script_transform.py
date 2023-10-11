import csv
import os

def transform_csv_to_md(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            lei, texto = row  # Adapte conforme as colunas do CSV
            md_filename = f"{lei}.md"
            with open(md_filename, 'w', encoding='utf-8') as md_file:
                # Aqui, transformamos o texto para usar links do Obsidian quando apropriado.
                texto_transformado = transform_text_to_obsidian_links(texto)
                md_file.write(texto_transformado)

def transform_text_to_obsidian_links(texto):
    # Esta função deve transformar o texto para usar links no formato Obsidian. 
    # Por exemplo, convertendo referências a outras leis em links [[Nome da Lei]]
    # Esta é uma lógica complexa que precisa ser adaptada de acordo com o conteúdo exato do CSV.
    return texto  # Isto é um placeholder. A lógica real precisa ser implementada.

if __name__ == "__main__":
    transform_csv_to_md("leis.csv")
