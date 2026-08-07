
##Reads "field names" of fillable PDF
from pypdf import PdfReader, PdfWriter

def get_pdf_fields(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        fields = reader.get_fields()
        if fields:
            return fields
        else:
            return "No fields found"
    except Exception as e:
        return f"Error reading PDF: {e}"

##Fills pdf form using a dictionary
def fill_pdf_form(input_pdf_path, output_pdf_path, data_dict):
   
    #Reads the template PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    #Append the template pages and form data structure to the writer
    writer.append(reader)
    
    #Update the form field values on the first page
    writer.update_page_form_field_values(
        writer.pages[0], 
        data_dict,)
    
    #Write the filled output to the destinated path
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)
        
    print(f"Successfully generated: {output_pdf_path}")