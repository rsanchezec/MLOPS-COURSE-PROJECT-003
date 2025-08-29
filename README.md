# MLOPS-PROJECT-003

## Resumen del Proyecto

**MLOPS-PROJECT-003** es un proyecto de MLOps que combina Apache Airflow para la orquestación de pipelines con un modelo de machine learning para la predicción de supervivencia del Titanic. Este proyecto fue generado usando la CLI de Astronomer y ha sido extendido con componentes personalizados de ML.

## Estructura del Proyecto

```
MLOPS-PROJECT-003/
├── artifacts/                  # Artefactos del modelo y datos
│   ├── models/
│   │   └── random_forest_model.pkl
│   └── raw/
│       ├── titanic_test.csv
│       └── titanic_train.csv
├── config/                     # Configuraciones del proyecto
│   ├── __init__.py
│   ├── database_config.py
│   └── paths_config.py
├── dags/                       # DAGs de Apache Airflow
│   ├── exampledag.py
│   ├── extract_data_from_gcp.py
│   ├── extract_data_from_gcp_fixed.py
│   ├── simple_etl_dag.py
│   └── simple_test_dag.py
├── include/                    # Archivos adicionales
│   └── gcp-key.json          # Credenciales de GCP
├── logs/                       # Logs del sistema
│   └── log_2025-08-29.log
├── notebook/                   # Notebooks de Jupyter
│   └── titanic.ipynb
├── pipeline/                   # Pipeline de entrenamiento
│   ├── __init__.py
│   └── training_pipeline.py
├── plugins/                    # Plugins de Airflow
├── src/                        # Código fuente principal
│   ├── __init__.py
│   ├── custom_exception.py
│   ├── data_ingestion.py
│   ├── data_processing.py
│   ├── feature_store.py
│   ├── logger.py
│   └── model_training.py
├── templates/                  # Templates HTML para Flask
│   └── index.html             # Interfaz web principal
├── tests/                      # Pruebas
│   └── dags/
│       └── test_dag_example.py
├── application.py              # Aplicación Flask principal
├── Dockerfile                  # Imagen Docker de Astro Runtime
├── airflow_settings.yaml      # Configuraciones locales de Airflow
├── packages.txt               # Paquetes del sistema
├── requirements.txt           # Dependencias de Python
└── setup.py                  # Configuración del paquete
```

## Componentes Principales

### 🔄 DAGs de Airflow
- **simple_etl_dag.py**: Pipeline ETL principal
- **extract_data_from_gcp.py**: Extracción de datos desde Google Cloud Platform
- **simple_test_dag.py**: DAG de pruebas

### 🌐 Aplicación Web Flask
- **application.py**: Servidor Flask con API de predicciones
- **templates/index.html**: Interfaz web interactiva para predicciones
- **Feature Store Integration**: Conexión con Redis para almacenamiento de características
- **Data Drift Detection**: Monitoreo automático de deriva de datos usando Alibi Detect

### 🧠 Pipeline de Machine Learning
- **data_ingestion.py**: Ingesta y carga de datos
- **data_processing.py**: Procesamiento y transformación de datos
- **model_training.py**: Entrenamiento del modelo
- **feature_store.py**: Gestión del almacén de características

### ⚙️ Configuración
- **database_config.py**: Configuración de base de datos
- **paths_config.py**: Configuración de rutas del proyecto
- **custom_exception.py**: Excepciones personalizadas
- **logger.py**: Sistema de logging

### 📊 Monitoreo y Métricas
- **Prometheus Metrics**: Métricas de predicciones y deriva de datos
- **Logging Sistema**: Registro detallado de eventos y predicciones
- **Health Checks**: Endpoints para verificar el estado del sistema

## Despliegue Local

### Prerrequisitos
- Docker y Docker Compose
- Astronomer CLI
- Python 3.8+
- Redis (para Feature Store)

### Iniciar el Proyecto

#### 1. Iniciar Airflow
```bash
astro dev start
```

Este comando creará cinco contenedores Docker:

- **Postgres**: Base de datos de metadatos de Airflow
- **Scheduler**: Componente responsable del monitoreo y activación de tareas
- **DAG Processor**: Componente responsable del análisis de DAGs
- **API Server**: Componente responsable de servir la UI y API de Airflow
- **Triggerer**: Componente responsable de activar tareas diferidas

#### 2. Iniciar la Aplicación Flask
```bash
python application.py
```

### Acceso a las Aplicaciones

- **Airflow UI**: http://localhost:8080/
- **Aplicación Web de Predicciones**: http://localhost:5000/
- **Métricas de Prometheus**: http://localhost:5000/metrics
- **Servidor de Métricas**: http://localhost:8000
- **Base de Datos Postgres**: localhost:5432/postgres
  - Usuario: `postgres`
  - Contraseña: `postgres`

### Comandos Útiles

```bash
# Detener el entorno
astro dev stop

# Reiniciar el entorno
astro dev restart

# Ver logs
astro dev logs

# Ejecutar comandos en el contenedor
astro dev bash
```

## Tecnologías Utilizadas

- **Apache Airflow**: Orquestación de workflows
- **Flask**: Framework web para la aplicación de predicciones
- **Python**: Lenguaje de programación principal
- **scikit-learn**: Biblioteca de machine learning
- **pandas**: Manipulación de datos
- **Redis**: Feature Store y almacenamiento en caché
- **Prometheus**: Monitoreo y métricas del sistema
- **Alibi Detect**: Detección de deriva de datos (Data Drift)
- **Docker**: Contenedorización
- **Google Cloud Platform**: Almacenamiento y servicios en la nube
- **HTML/CSS/JavaScript**: Frontend interactivo

## Características del Modelo ML

El proyecto incluye un modelo de Random Forest para predecir la supervivencia de pasajeros del Titanic:

- **Dataset**: Titanic (train/test)
- **Algoritmo**: Random Forest
- **Objetivo**: Clasificación binaria (supervivencia)
- **Formato del modelo**: Pickle (.pkl)
- **Features utilizadas**: Age, Fare, Pclass, Sex, Embarked, Familysize, Isalone, HasCabin, Title, Pclass_Fare, Age_Fare

## Funcionalidades Avanzadas

### 🔍 Detección de Deriva de Datos (Data Drift)
- Implementación de **Kolmogorov-Smirnov Drift** para detectar cambios en la distribución de datos
- Monitoreo automático en tiempo real durante las predicciones
- Alertas y métricas cuando se detecta deriva significativa

### 📊 Sistema de Monitoreo
- **Prometheus Metrics**:
  - `prediction_count`: Contador de predicciones realizadas
  - `drift_count`: Contador de detecciones de deriva
- **Endpoints de métricas**: `/metrics` para integración con sistemas de monitoreo
- **Logging detallado**: Registro de eventos, predicciones y alertas

### 🏪 Feature Store con Redis
- Almacenamiento eficiente de características en Redis
- Recuperación rápida de datos históricos para comparación
- Escalado de datos usando StandardScaler
- Gestión de lotes de características para entrenamiento

### 🌐 Interfaz Web Interactiva
- **Formulario inteligente**: Auto-cálculo de campos derivados
- **Diseño responsive**: Compatible con dispositivos móviles
- **Tooltips informativos**: Ayuda contextual para cada campo
- **Animaciones CSS**: Experiencia de usuario fluida
- **Validación en tiempo real**: Verificación de datos antes del envío

## Despliegue en Astronomer

Para desplegar en Astronomer:

1. Crear una cuenta en Astronomer
2. Seguir la documentación oficial: https://www.astronomer.io/docs/astro/deploy-code/

## Uso de la Aplicación

### Predicciones via Web Interface

1. Accede a http://localhost:5000/
2. Completa el formulario con la información del pasajero:
   - **Datos básicos**: Edad, sexo, clase del boleto, tarifa
   - **Información familiar**: Tamaño de familia, si viaja solo
   - **Detalles del viaje**: Puerto de embarque, si tiene camarote
   - **Campos derivados**: Se calculan automáticamente (Pclass_Fare, Age_Fare)
3. Haz clic en "Realizar Predicción"
4. Observa el resultado y las métricas de deriva de datos

### API Endpoints

- `GET /`: Interfaz web principal
- `POST /predict`: Endpoint para realizar predicciones
- `GET /metrics`: Métricas de Prometheus

### Monitoreo del Sistema

```bash
# Ver métricas en tiempo real
curl http://localhost:5000/metrics

# Monitorear logs
tail -f logs/log_$(date +%Y-%m-%d).log
```

## Pruebas

Ejecutar las pruebas con:

```bash
# Pruebas de DAGs
python -m pytest tests/dags/

# Validar DAGs
astro dev parse

# Probar la aplicación Flask
python -m pytest tests/ -v
```

## Contribución

1. Fork el proyecto
2. Crear una rama para la feature (`git checkout -b feature/AmazingFeature`)
3. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Soporte

Para reportar bugs o sugerir cambios, contacta al equipo de Astronomer o crea un issue en el repositorio del proyecto.
