import pandas as pd
import numpy as np
import os

def get_gdp_data():
    """Завантажує дані про ВВП на душу населення з локального CSV-файлу."""
    file_path = 'API_NY.GDP.PCAP.CD_DS2_en_csv_v2_1387693.csv'
    
    if not os.path.exists(file_path):
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        print("Будь ласка, завантажте його за посиланням:")
        print("https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=csv")
        print("і помістіть в ту ж папку, де знаходиться цей скрипт.")
        return None

    try:
        gdp_df = pd.read_csv(file_path, skiprows=4)
        
        gdp_2019 = gdp_df[['Country Name', 'Country Code', '2019']]
        
        gdp_2019 = gdp_2019.dropna(subset=['2019'])
        
        return gdp_2019
    except Exception as e:
        print(f"Помилка обробки даних: {e}")
        return None

def print_gdp_data(df):
    """Виводить весь вміст DataFrame на екран."""
    if df is not None:
        print("ВВП на душу населення (2019, US$) для усіх країн:")
        print(df.to_string())

def search_and_save_gdp(df):
    """Шукає дані для введених користувачем країн і зберігає їх у CSV-файл."""
    if df is None:
        return

    print("\nВведіть назви країн для пошуку (розділяйте їх комами або пробілами).")
    input_countries_str = input("Назви країн: ").strip()
    
    if not input_countries_str:
        print("Введіть хоча б одну назву країни.")
        return

    search_countries = [country.strip() for country in input_countries_str.replace(',', ' ').split()]
    
    found_countries = df[df['Country Name'].isin(search_countries)]

    if not found_countries.empty:
        output_filename = 'gdp_2019_selected.csv'
        found_countries.to_csv(output_filename, index=False)
        print(f"\nДані для вибраних країн збережено у файл '{output_filename}'.")
        print("\nЗнайдені дані:")
        print(found_countries)
    else:
        print("\nДані для введених країн не знайдено.")

if __name__ == '__main__':
    gdp_data = get_gdp_data()
    if gdp_data is not None:
        print_gdp_data(gdp_data)
        search_and_save_gdp(gdp_data)