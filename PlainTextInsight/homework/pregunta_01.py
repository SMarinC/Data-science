"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import re
import pandas as pd


def _clean_keywords(raw_text: str) -> str:
  """Normalize keywords string:

  - Join lines, collapse multiple spaces
  - Split by comma, strip each keyword, remove trailing periods
  - Join by ", " ensuring single space after commas
  """
  # collapse newlines and multiple spaces
  s = re.sub(r"\s+", " ", raw_text.strip())
  # Split by comma, strip each part and remove trailing periods
  parts = [p.strip().rstrip(".") for p in s.split(",") if p.strip()]
  # Join with single comma + space
  return ", ".join(parts)


def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra.
  """

  path = "files/input/clusters_report.txt"

  records = []

  with open(path, encoding="utf-8") as fh:
    lines = fh.readlines()

  # find start after the dashed separator line
  start_idx = 0
  for i, line in enumerate(lines):
    if line.strip().startswith("---"):
      start_idx = i + 1
      break

  i = start_idx
  cur = None
  while i < len(lines):
    line = lines[i]
    # detect cluster start: line starting with number (cluster)
    m = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)$", line)
    if m:
      # finish previous
      if cur:
        # finalize keywords
        kw = _clean_keywords(" ".join(cur["kw_lines"]))
        cur_record = {
          "cluster": int(cur["cluster"]),
          "cantidad_de_palabras_clave": int(cur["cantidad"]),
          "porcentaje_de_palabras_clave": float(cur["porcentaje"].replace(",", ".")),
          "principales_palabras_clave": kw,
        }
        records.append(cur_record)

      cluster, cantidad, porcentaje, rest = m.groups()
      cur = {"cluster": cluster, "cantidad": cantidad, "porcentaje": porcentaje, "kw_lines": [rest]}
    else:
      # continuation lines: either keywords or blank
      if cur is not None:
        # lines that are not empty append to kw_lines
        if line.strip():
          cur["kw_lines"].append(line.strip())
    i += 1

  # append last
  if cur:
    kw = _clean_keywords(" ".join(cur["kw_lines"]))
    cur_record = {
      "cluster": int(cur["cluster"]),
      "cantidad_de_palabras_clave": int(cur["cantidad"]),
      "porcentaje_de_palabras_clave": float(cur["porcentaje"].replace(",", ".")),
      "principales_palabras_clave": kw,
    }
    records.append(cur_record)

  df = pd.DataFrame.from_records(records)
  # ensure proper column order and names (lowercase, spaces->underscores)
  df = df[["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]]

  return df


if __name__ == "__main__":
  print(pregunta_01().head())
