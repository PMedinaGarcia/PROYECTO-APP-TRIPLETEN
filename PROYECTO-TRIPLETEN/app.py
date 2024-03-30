import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos del archivo CSV
car_data = pd.read_csv(r'C:\Users\patri\OneDrive\Escritorio\PROYECTO TRIPLETEN PMG\vehicles_us.csv')

# Encabezado y contexto cddel análisis
st.title('Análisis Exploratorio de Datos de Vehículos')
st.markdown("""
Este anális explora un conjunto de datos de vehículos de segunda mano para entender las tendencias del mercado automotriz. 
A través de la aplicación, podrás interactuar con los datos y visualizar distintos aspectos mediante filtros y gráficos interactivos.

**Conclusiones clave:**
- Los SUVs y camionetas son los tipos de vehículos más populares.
- Existe una clara relación entre el año del modelo y el precio, indicando la depreciación con el tiempo.
- El kilometraje tiene un impacto significativo en el precio, donde menos kilometraje implica un precio más alto.
""")

# Definir filtros en la barra lateral
st.sidebar.header('Filtros')
year_range = st.sidebar.slider('Año del Modelo', int(car_data['model_year'].min()), int(car_data['model_year'].max()), (int(car_data['model_year'].min()), int(car_data['model_year'].max())))
type_filter = st.sidebar.multiselect('Tipo de Vehículo', options=car_data['type'].unique())
condition_filter = st.sidebar.multiselect('Condición del Vehículo', options=car_data['condition'].unique())

# Configura el encabezado de la aplicación
st.header('Visualización de Datos de Vehículos')

# Botón para aplicar filtros y mostrar datos
if st.button('Mostrar Datos Según Preferencias Filtradas'):
    # Filtrar datos según las selecciones del usuario
    filtered_data = car_data[(car_data['model_year'].between(*year_range)) & (car_data['type'].isin(type_filter)) & (car_data['condition'].isin(condition_filter))]
    
    if filtered_data.empty:
        st.write('No se encontraron datos con estos filtros.')
    else:
        # Mostrar datos filtrados
        st.write(f'Datos filtrados para vehículos del {year_range[0]} al {year_range[1]}, Tipo: {type_filter}, Condición: {condition_filter}')
        st.dataframe(filtered_data)

# Botón para construir el histograma
if st.button('Mostrar Histograma de Kilometraje'):
    st.write('Histograma del Kilometraje de los Vehículos')
    fig = px.histogram(car_data, x="odometer", title='Distribución del Kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión Precio vs Año'):
    st.write('Gráfico de Dispersión de Precio vs Año del Modelo')
    fig = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año del Modelo')
    st.plotly_chart(fig, use_container_width=True)
