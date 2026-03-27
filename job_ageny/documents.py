from docxtpl import DocxTemplate
import os
import re

def generate_cv(template, output_path, context):
    doc = DocxTemplate(template)
    doc.render(context)
    doc.save(output_path)


def generate_cover_letter(template, output_path, context):
    doc = DocxTemplate(template)
    doc.render(context)
    doc.save(output_path)

def safe_filename(text):
    # Remove invalid Windows filename characters
    text = re.sub(r'[<>:"/\\|?*]', '', text)

    # Replace spaces with underscores
    text = text.replace(" ", "_")

    # Optional: limit length
    return text[:100]