from docxtpl import DocxTemplate
import os

def generate_cv(template, output_path, context):
    doc = DocxTemplate(template)
    doc.render(context)
    doc.save(output_path)


def generate_cover_letter(template, output_path, context):
    doc = DocxTemplate(template)
    doc.render(context)
    doc.save(output_path)


def safe_filename(text):
    return text.replace(" ", "_").replace("/", "_")