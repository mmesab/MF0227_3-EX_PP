# Sistema de Gestión de Incidencias Técnicas (HelpDesk)

Aplicación web desarrollada con Python y Django para la gestión centralizada de incidencias técnicas, aplicando principios de Programación Orientada a Objetos (UF2404), desarrollo web y ORM (UF2405) y control de versiones/ciclo de vida (UF2406).

## Arquitectura del Proyecto
* **UF2404 (`core_modelos.py`):** Módulo independiente en Python puro que modela la lógica de negocio mediante encapsulamiento, herencia (`TicketTecnico` -> `TicketHardware`, `TicketSoftware`), polimorfismo (`calcular_sla()`) y control de flujo de estados mediante excepciones personalizadas (`EstadoInvalidoError`).
* **UF2405 (`helpdesk_project` y `incidencias`):** Capa web construida sobre el patrón MVT de Django. Utiliza ORM con modelos relacionales (`Tecnico` e `Incidencia`), panel de administración personalizado, formularios validados (`ModelForm`) y plantillas HTML con herencia (`base.html`) y Bootstrap 5.
* **UF2406 (Git y Documentación):** Gestión del código fuente mediante ramas (`main` y `desarrollo`), commits atómicos semánticos, aislamiento de dependencias (`requirements.txt`) y plan de pruebas documentado.

## Instalación y Despliegue Local

1. **Clonar el repositorio o descomprimir el proyecto:**
   ```bash
   cd helpdesk_system

---

## 📦 Notas sobre la Entrega y Datos de Prueba

- **Repositorio GitHub:** Se ha mantenido una estructura limpia de código fuente y control de versiones (ramas `main` y `desarrollo`), excluyendo los archivos binarios de base de datos local por buenas prácticas de desarrollo.
- **Archivo ZIP de Entrega:** El paquete `.zip` entregado incluye la base de datos precargada (`db.sqlite3`) con **técnicos e incidencias de prueba** ya creados, permitiendo evaluar la interfaz y el panel de administración de forma inmediata al iniciar el servidor local.