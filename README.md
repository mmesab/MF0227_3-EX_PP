# Sistema de Gestión de Incidencias Técnicas (HelpDesk)
 
Aplicación web desarrollada con Python y Django para la gestión centralizada de incidencias técnicas, aplicando principios de Programación Orientada a Objetos (UF2404), desarrollo web y ORM (UF2405) y control de versiones/ciclo de vida (UF2406).
 
## Arquitectura del Proyecto
 
- **UF2404 (`core_modelos.py`):** Módulo independiente en Python puro que modela la lógica de negocio mediante encapsulamiento, herencia (`TicketTecnico` -> `TicketHardware`, `TicketSoftware`), polimorfismo (`calcular_sla()`) y control de flujo de estados mediante excepciones personalizadas (`EstadoInvalidoError`).
- **UF2405 (`helpdesk_project` y `incidencias`):** Capa web construida sobre el patrón MVT de Django. Utiliza ORM con modelos relacionales (`Tecnico` e `Incidencia`), panel de administración personalizado, formularios validados (`ModelForm`) y plantillas HTML con herencia (`base.html`), Google Fonts (Inter) y Bootstrap 5.
- **UF2406 (Git y Documentación):** Gestión del código fuente mediante ramas (`main` y `desarrollo`), commits atómicos semánticos, aislamiento de dependencias (`requirements.txt`) y plan de pruebas documentado.
---
 
## 🚀 Guía de Instalación y Ejecución
 
Sigue estos pasos en tu terminal para clonar el repositorio, configurar el entorno virtual y poner en marcha la aplicación localmente:
 
### 1. Clonar el repositorio y acceder a la carpeta
 
```bash
git clone https://github.com/mmesab/MF0227_3-EX_PP.git
cd MF0227_3-EX_PP
```
 
### 2. Crear y activar el entorno virtual
 
- **En macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
 
- **En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
 
### 3. Instalar las dependencias
 
```bash
pip install -r requirements.txt
```
 
### 4. Aplicar las migraciones de base de datos
 
> **Nota:** Si utilizas el archivo `.zip` de entrega, la base de datos `db.sqlite3` ya incluye registros precargados de prueba.
 
```bash
python3 manage.py migrate
```
 
### 5. Iniciar el servidor de desarrollo
 
```bash
python3 manage.py runserver
```
 
Una vez ejecutado, abre tu navegador web y accede a:
 
- **Interfaz web del HelpDesk:** http://127.0.0.1:8000/
- **Panel de Administración (Django Admin):** http://127.0.0.1:8000/admin/
---
 
## 📦 Notas sobre la Entrega y Datos de Prueba
 
- **Repositorio GitHub:** Se ha mantenido una estructura limpia de código fuente y control de versiones (ramas `main` y `desarrollo`), excluyendo los archivos binarios de base de datos local por buenas prácticas de desarrollo.
- **Archivo ZIP de Entrega:** El paquete `.zip` entregado incluye la base de datos precargada (`db.sqlite3`) con **técnicos e incidencias de prueba** ya creados, permitiendo evaluar la interfaz y el panel de administración de forma inmediata al iniciar el servidor local.