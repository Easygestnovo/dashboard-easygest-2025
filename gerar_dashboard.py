
import pandas as pd

df = pd.read_excel("angariações 2025 Macro.xlsx")

total_angariador = df['Angariador'].value_counts().reset_index()
total_angariador.columns = ['Angariador', 'Total']
total_loja = df['Loja'].value_counts().reset_index()
total_loja.columns = ['Loja', 'Total']

df_exclusivo = df[df['RegimeContrato'].str.lower() == 'exclusivo']
exclusivo_angariador = df_exclusivo['Angariador'].value_counts().reset_index()
exclusivo_angariador.columns = ['Angariador', 'Exclusivos']
exclusivo_loja = df_exclusivo['Loja'].value_counts().reset_index()
exclusivo_loja.columns = ['Loja', 'Exclusivos']

def gerar_tabela(titulo, df, col1, col2):
    medalhas = ['🥇', '🥈', '🥉']
    html = f'<div class="chart"><h2>{titulo}</h2><table><thead><tr><th>Lugar</th><th>{col1}</th><th>{col2}</th></tr></thead><tbody>'
    for i, row in df.iterrows():
        lugar = f"{medalhas[i]} {i+1}º" if i < 3 else f"{i+1}º"
        html += f"<tr><td>{lugar}</td><td>{row[0]}</td><td>{row[1]}</td></tr>"
    html += '</tbody></table></div>'
    return html

html = f"""<!DOCTYPE html>
<html lang='pt'>
<head>
    <meta charset='UTF-8'>
    <title>Dashboard EasyGest 2025</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: #00264d;
            color: #ffffff;
            max-width: 1100px;
            margin: auto;
            padding: 20px;
        }}
        .banner {{
            display: flex;
            justify-content: center;
            padding: 40px 20px 20px 20px;
            border-radius: 12px;
        }}
        .banner img {{
            max-height: 240px;
        }}
        h1 {{
            text-align: center;
            margin-top: 30px;
            margin-bottom: 40px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}
        .chart {{
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.15);
            padding: 20px;
            overflow-x: auto;
            color: #111;
        }}
        .chart h2 {{
            font-size: 20px;
            color: #00264d;
            margin-bottom: 10px;
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            border: 1px solid #cbd5e1;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #f3f4f6;
            color: #00264d;
        }}
    </style>
</head>
<body>
<script>
  var password = prompt("🔒 Área Reservada \n\nIntroduza a palavra-passe:");
  if (password !== "easygest2025") {{
    alert("❌ Acesso negado.");
    window.location.href = "https://www.google.com/";
  }}
</script>
<div class='banner'>
    <img src='banner_dashboard_final.jpg' alt='Banner EasyGest Ranking'>
</div>
<h1>🏆 Dashboard TOP 10 - Angariações 2025</h1>
<div class='grid'>
{gerar_tabela("Angariador - Total", total_angariador.head(10), "Angariador", "Total")}
{gerar_tabela("Loja - Total", total_loja.head(10), "Loja", "Total")}
{gerar_tabela("Angariador - Exclusivo", exclusivo_angariador.head(10), "Angariador", "Exclusivos")}
{gerar_tabela("Loja - Exclusivo", exclusivo_loja.head(10), "Loja", "Exclusivos")}
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
