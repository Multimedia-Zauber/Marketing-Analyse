import os
from datetime import datetime
import pandas as pd


def erstelle_beispieldaten(filepath="umsatzdaten.csv"):
    """Erstellt Testdaten, falls du noch keine eigene CSV-Datei hast."""
    data = {
        "Datum": pd.date_range(
            start="2026-01-01", periods=100, freq="D"
        ).strftime("%Y-%m-%d"),
        "Kategorie": [
            "Elektronik",
            "Möbel",
            "Kleidung",
            "Elektronik",
            "Software",
        ]
        * 20,
        "Produkt": ["Laptop", "Stuhl", "T-Shirt", "Smartphone", "Lizenz A"]
        * 20,
        "Menge": [1, 4, 10, 2, 5] * 20,
        "Preis_Euro": [1200, 150, 25, 800, 50] * 20,
    }
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"ℹ️ Beispieldatei '{filepath}' wurde neu erstellt.")


def erstelle_bericht(input_file="umsatzdaten.csv"):
    # 1. Beispieldaten erzeugen, falls Datei fehlt
    if not os.path.exists(input_file):
        erstelle_beispieldaten(input_file)

    print("📊 Starte Datenanalyse...")

    # 2. Daten einlesen
    df = pd.read_csv(input_file)
    df["Datum"] = pd.to_datetime(df["Datum"])

    # 3. Berechnungen / Analysen durchführen
    df["Gesamtumsatz"] = df["Menge"] * df["Preis_Euro"]

    gesamt_umsatz = df["Gesamtumsatz"].sum()
    gesamt_menge = df["Menge"].sum()
    durchschnitt_bestellung = df["Gesamtumsatz"].mean()

    umsatz_kategorie = (
        df.groupby("Kategorie")["Gesamtumsatz"]
        .sum()
        .reset_index()
        .sort_values(by="Gesamtumsatz", ascending=False)
    )

    top_produkte = (
        df.groupby("Produkt")[["Menge", "Gesamtumsatz"]]
        .sum()
        .reset_index()
        .sort_values(by="Gesamtumsatz", ascending=False)
    )

    # 4. Bericht generieren (Excel mit mehreren Reitern)
    datum_heute = datetime.now().strftime("%Y-%m-%d")
    output_file = f"Management_Bericht_{datum_heute}.xlsx"

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        # Kennzahlen-Übersicht
        kpis = pd.DataFrame({
            "Kennzahl": [
                "Gesamtumsatz (€)",
                "Verkaufte Stückzahl Gesamt",
                "Durchschnittlicher Bestellwert (€)",
            ],
            "Wert": [
                round(gesamt_umsatz, 2),
                gesamt_menge,
                round(durchschnitt_bestellung, 2),
            ],
        })

        kpis.to_excel(writer, sheet_name="KPI Übersicht", index=False)
        umsatz_kategorie.to_excel(
            writer, sheet_name="Umsatz nach Kategorie", index=False
        )
        top_produkte.to_excel(
            writer, sheet_name="Top Produkte", index=False
        )
        df.to_excel(writer, sheet_name="Rohdaten", index=False)

    print(f"✅ Analyse abgeschlossen! Bericht gespeichert unter: {output_file}")


if __name__ == "__main__":
    erstelle_bericht()