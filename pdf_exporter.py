import pandas as pd
from fpdf import FPDF

def export_to_pdf(df, filename="Data_Report.pdf"):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        # Title
        pdf.cell(40, 10, "NijayaTest: Data Export Report")
        pdf.ln(20) # Line break
        
        # Table Headers
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(95, 10, "Name", border=1)
        pdf.cell(95, 10, "Value", border=1)
        pdf.ln()
        
        # Table Content
        pdf.set_font("Arial", size=12)
        for index, row in df.iterrows():
            pdf.cell(95, 10, str(row['Name']), border=1)
            pdf.cell(95, 10, str(row['Value']), border=1)
            pdf.ln()
            
        pdf.output(filename)
        print(f"Successfully exported to {filename}!")
        
    except Exception as e:
        print(f"Error exporting PDF: {e}")

if __name__ == "__main__":
    # Load your existing data.csv
    data = pd.read_csv('data.csv')
    export_to_pdf(data)
