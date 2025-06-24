import csv
from fpdf import FPDF

file_path = "sales_data.csv"
rows = []
total_units = 0
total_revenue = 0

with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)
        total_units += int(row["Units Sold"])
        total_revenue += int(row["Revenue"])

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Sales Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Units Sold: {total_units}", ln=True)
pdf.cell(0, 10, f"Total Revenue: Rs. {total_revenue}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Date", 1)
pdf.cell(50, 10, "Product", 1)
pdf.cell(40, 10, "Units Sold", 1)
pdf.cell(40, 10, "Revenue", 1)
pdf.ln()

pdf.set_font("Arial", '', 12)
for row in rows:
    pdf.cell(40, 10, row["Date"], 1)
    pdf.cell(50, 10, row["Product"], 1)
    pdf.cell(40, 10, row["Units Sold"], 1)
    pdf.cell(40, 10, row["Revenue"], 1)
    pdf.ln()

pdf.output("sales_report.pdf")
print("PDF report generated: sales_report.pdf")
