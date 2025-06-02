import pdfplumber
import pandas as pd
import re

# List of known categories
KNOWN_CATEGORIES = [
    "Femenino 18 a 35 años",
    "Femenino 36 a 49 años",
    "Femenino 50 a 65 años",
    "Masculino 18 a 35 años",
    "Masculino 36 a 49 años",
    "Masculino 50 a 65 años",
    "Masculino +66 años"
]

def is_category(line_text):
    """Check if a line exactly matches one of the known categories."""
    return line_text.strip() in KNOWN_CATEGORIES

def parse_time_to_seconds(time_str):
    """Convert time string HH:MM:SS,mm to total seconds as float."""
    try:
        parts = time_str.split(':')
        if len(parts) == 3:
            h = int(parts[0])
            m = int(parts[1])
            s_ms = parts[2].split(',')
            s = int(s_ms[0])
            ms = int(s_ms[1]) if len(s_ms) > 1 else 0
            return float(h * 3600 + m * 60 + s + ms / 100.0)
        elif len(parts) == 2:
            m = int(parts[0])
            s_ms = parts[1].split(',')
            s = int(s_ms[0])
            ms = int(s_ms[1]) if len(s_ms) > 1 else 0
            return float(m * 60 + s + ms / 100.0)
    except ValueError:
        return None

data_rows = []
current_category = None
pdf_path = "data/ruta_medellin_2025/resultados_consolidados_preliminares_0.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if is_category(line):
                current_category = line.strip()
            elif re.match(r"^\d+\.\s+\d+", line.strip()) and len(line.split()) > 8: # Expect at least Rank, No, Name, S1,S2,S3,Total,Speed
                tokens = line.split()
                try:
                    rank = int(tokens[0].replace(".", ""))
                    number = int(tokens[1])
                    lastname = tokens[2]
                    # Names can be multiple tokens. The times and speed are the last 5 tokens.
                    names = " ".join(tokens[3:-5])
                    seg1_str, seg2_str, seg3_str, total_str, speed_str = tokens[-5:]

                    seg1_secs = parse_time_to_seconds(seg1_str)
                    seg2_secs = parse_time_to_seconds(seg2_str)
                    seg3_secs = parse_time_to_seconds(seg3_str)
                    total_secs = parse_time_to_seconds(total_str)

                    data_rows.append({
                        "Category": current_category,
                        "CategoryRank": rank,
                        "Number": number,
                        "Lastname": lastname.title(),
                        "Names": names.title(),
                        "Segment 1": seg1_str,
                        "Segment 1 Secs": seg1_secs,
                        "Segment 2": seg2_str,
                        "Segment 2 Secs": seg2_secs,
                        "Segment 3": seg3_str,
                        "Segment 3 Secs": seg3_secs,
                        "Total": total_str,
                        "Total Secs": total_secs,
                        "Speed (km/h)": float(speed_str.replace(",","."))
                    })
                except Exception as e:
                    continue

# Save to CSV
df_export = pd.DataFrame(data_rows)
csv_path = "data/ruta_medellin_2025/race_results_by_category.csv"
df_export.to_csv(csv_path, index=False)
print(f"Data saved to {csv_path}")
