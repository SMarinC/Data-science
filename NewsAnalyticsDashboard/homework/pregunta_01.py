"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # Rutas
    csv_path = os.path.join("files", "input", "news.csv")
    out_dir = os.path.join("files", "plots")
    out_path = os.path.join(out_dir, "news.png")

    # Crear carpeta de salida si no existe
    os.makedirs(out_dir, exist_ok=True)

    # Leer datos
    df = pd.read_csv(csv_path, index_col=0)

    # Preparar figura
    fig, ax = plt.subplots(figsize=(8, 5))

    # Graficar cada medio
    for col in df.columns:
        ax.plot(df.index.astype(str), df[col], marker='o', label=col)

    ax.set_title("News consumption by medium (2001-2010)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")
    ax.legend()
    ax.grid(alpha=0.3)

    # Guardar imagen
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
