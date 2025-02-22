# Proyecto: IndiLingo

## 1. Requisitos y Casos de Uso

### Actores:
- **Estudiantes:** Pueden buscar palabras y repasar vocabulario.
- **Profesores:** Pueden agregar, editar y eliminar palabras.
- **Administrador (Opcional):** Puede gestionar usuarios y controlar contenido.


## Definición de Requisitos:

## 1. Introducción
Este documento define los requisitos para **diccioNativo**, una plataforma en línea diseñada para el aprendizaje de una lengua indígena mediante un enfoque gramatical. La plataforma ofrece lecciones interactivas y ejercicios para hacer el aprendizaje accesible y ameno. El proceso de desarrollo se rige por el método ICONIX, que permite transformar de forma ágil y estructurada los requisitos en un diseño orientado a objetos.

## 2. Objetivos del Proyecto
- **Facilitar el aprendizaje** de una lengua indígena utilizando un enfoque gramatical.
- **Proveer lecciones interactivas** y ejercicios prácticos que refuercen la adquisición del idioma.
- **Ofrecer una experiencia personalizada** a través del seguimiento del progreso del estudiante.
- **Permitir una gestión sencilla** del contenido y usuarios por parte de los administradores.

## 3. Alcance
El sistema abarcará funcionalidades básicas para dos tipos de usuarios:
- **Estudiantes:** Registro, autenticación, acceso a lecciones, ejercicios, descargas de material de apoyo, consulta de glosario, seguimiento del progreso y configuración del perfil.
- **Administradores:** Gestión de usuarios e instructores, creación y edición de lecciones, control del contenido, monitoreo de actividad y administración de roles y contraseñas.


## 1. Requisitos Funcionales

### 1.1 Gestión de Usuarios
- **RF01:** El sistema debe permitir el registro de nuevos estudiantes mediante correo electrónico y contraseña.
- **RF02:** El sistema debe implementar un mecanismo de autenticación para acceso seguro.
- **RF03:** El sistema debe permitir a los usuarios modificar su perfil y preferencias.
- **RF04:** El sistema debe permitir a los administradores gestionar roles de usuarios.
- **RF05:** El sistema debe implementar un mecanismo de recuperación de contraseñas.

### 1.2 Gestión de Contenido Educativo
- **RF06:** El sistema debe organizar el contenido en lecciones secuenciales.
- **RF07:** El sistema debe permitir la descarga de material complementario PDF.
- **RF08:** El sistema debe incluir un glosario de términos con definiciones y pronunciación.
- **RF09:** El sistema debe proporcionar ejercicios de traducción bidireccional (del idioma indígena al español y viceversa).
- **RF10:** El sistema debe permitir a los administradores crear y editar lecciones interactivas.

### 1.3 Seguimiento y Evaluación
- **RF11:** El sistema debe registrar el progreso de aprendizaje de cada estudiante.
- **RF12:** El sistema debe proporcionar retroalimentación inmediata en los ejercicios.
- **RF13:** El sistema debe generar estadísticas de uso y aprovechamiento.
- **RF14:** El sistema debe mantener un registro de actividades para administración.

---

## 2. Requisitos No Funcionales

### 2.1 Usabilidad
- **RNF01:** La interfaz debe ser intuitiva y fácil de usar.
- **RNF02:** El sistema debe ser accesible en una plataforma
- **RNF03:** Los tiempos de respuesta no deben exceder 3 segundos.
- **RNF04:** El sistema debe proporcionar mensajes de error claros y orientativos.

### 2.2 Seguridad
- **RNF05:** Se intetera 3 veces el acceso al sistema.
- **RNF06:** El acceso a funciones administrativas debe estar restringido.

### 2.3 Confiabilidad
- **RNF09:** El sistema debe mantener coherencia en los datos almacenados.

---

## 3. Notas de Integración con el Proceso ICONIX

- **Modelo de Dominio:** Se identificarán entidades clave como `Usuario`, `Lección`, `Ejercicio`, `Progreso` y `Glosario` que representarán la estructura de la plataforma y sus relaciones.
- **Casos de Uso:** Cada requisito funcional se traducirá en casos de uso detallados (como los presentados para Estudiantes profesores y Administradores) que servirán de base para el análisis de robustez.
- **Análisis de Robustez:** Se diseñarán diagramas que vinculen los objetos límite (interfaces), de control (lógica de negocio) y entidad (datos) para cada caso de uso.
- **Diseño Detallado:** Se desarrollarán diagramas de secuencia y de clases, que asignen comportamientos a las entidades y detallen la interacción entre los componentes.
- **Implementación:** Se utilizará Django para desarrollar la plataforma, aplicando una arquitectura en tres capas que separe la lógica de negocio, la presentación y el acceso a datos.
---

### Casos de Uso para Estudiantes:

#### Caso de uso UC01: Registro en la Plataforma
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir que un nuevo usuario cree una cuenta en la plataforma.
- **Resumen:** El estudiante completa un formulario de registro proporcionando sus datos personales. El sistema verifica la validez de los datos e inicia la creación de la cuenta.
- **Entradas:** Nombre, correo electrónico, contraseña.
- **Salida:** Confirmación de cuenta creada, acceso a la plataforma.
- **Precondiciones:** El estudiante debe tener una dirección de correo válida.
- **Postcondiciones:** El estudiante tiene acceso al contenido inicial de la plataforma.

---

#### Caso de uso UC02: Iniciar Sesión
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir el acceso al sistema mediante credenciales válidas.
- **Resumen:** El estudiante proporciona sus credenciales, y el sistema valida la información.
- **Entradas:** Correo electrónico, contraseña.
- **Salida:** Acceso concedido a la cuenta del usuario.
- **Precondiciones:** El estudiante debe estar registrado.
- **Postcondiciones:** El estudiante accede a su panel personalizado.

---

#### Caso de uso UC03: Descarga de Material de Apoyo
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir al estudiante descargar recursos adicionales (PDFs, audios, videos).
- **Resumen:** El estudiante accede a una sección de materiales complementarios y realiza la descarga.
- **Entradas:** Solicitud de descarga.
- **Salida:** Archivo descargado localmente.
- **Precondiciones:** Estar registrado y haber completado la lección asociada.
- **Postcondiciones:** Acceso a recursos complementarios offline.

---

#### Caso de uso UC04: Consultar el Glosario de Términos
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir a los estudiantes consultar definiciones de palabras en la lengua indígena.
- **Resumen:** El estudiante busca términos específicos y accede a su definición y pronunciación.
- **Entradas:** Término a buscar.
- **Salida:** Definición y recursos multimedia asociados.
- **Precondiciones:** El estudiante debe estar autenticado.
- **Postcondiciones:** Registro de consultas para análisis de uso del sistema.
  
- ---

#### Caso de uso UC05: Visualizar Progreso de Aprendizaje
- **Actores:** Estudiante, Sistema
- **Propósito:** Mostrar el avance del estudiante en las lecciones y ejercicios completados.
- **Resumen:** El estudiante accede a una sección donde puede ver su progreso.
- **Entradas:** Solicitud de visualización de progreso.
- **Salida:** Reporte con porcentaje de avance, niveles completados y estadísticas.
- **Precondiciones:** El estudiante debe haber completado al menos una lección.
- **Postcondiciones:** Visualización de datos actualizados del progreso.

---

#### Caso de uso UC06:  Configuración de Perfil
- **Actores:** Estudiante, Sistema
- **Propósito:** Personalizar información del perfil de usuario.
- **Resumen:** El estudiante modifica su foto, idioma de interfaz o preferencias.
- **Entradas:** Nuevos datos (ej: imagen, configuración).
- **Salida:** Perfil actualizado.
- **Precondiciones:** Usuario autenticado.
- **Postcondiciones:** Cambios guardados en la base de datos.

---

#### Caso de uso UC07: Ejercicio de Traducción
- **Actores:**  Estudiante, Sistema
- **Propósito:** Traducir frases del idioma indígena al español o viceversa.
- **Resumen:** El estudiante escribe la traducción de una frase y el sistema la valora.
- **Entradas:** Texto ingresado por el usuario.
- **Salida:** Corrección inmediata con explicaciones gramaticales.
- **Precondiciones:** Lección de vocabulario completada.
- **Postcondiciones:**  Puntuación añadida al progreso

---

### Casos de Uso para Administradores:

#### Caso de uso UC01: Registrar Nuevo Instructor
- **Actores:** Administrador, Sistema de Gestión de Usuarios
- **Propósito:** Permitir la creación de cuentas de instructores.
- **Resumen:** El administrador ingresa los datos del instructor y asigna roles.
- **Entradas:** Nombre, correo, permisos.
- **Salida:** Confirmación de registro exitoso.
- **Precondiciones:** El administrador debe tener acceso autorizado.
- **Postcondiciones:** El nuevo instructor recibe sus credenciales por correo.

---

#### Caso de uso UC02: Crear Nueva Lección
- **Actores:** Administrador, Sistema de Gestión de Contenidos
- **Propósito:** Agregar nuevas lecciones al sistema.
- **Resumen:** El administrador configura el contenido, añade ejercicios y define objetivos de aprendizaje.
- **Entradas:** Título, descripción, contenido multimedia.
- **Salida:** Lección publicada.
- **Precondiciones:** El administrador debe estar autenticado.
- **Postcondiciones:** La lección aparece disponible para los estudiantes.

---

#### Caso de uso UC03: Editar o Eliminar Contenido
- **Actores:** Administrador, Sistema de Gestión de Contenidos
- **Propósito:** Modificar o eliminar contenido de lecciones existentes.
- **Resumen:** El administrador edita texto, cambia archivos multimedia o elimina lecciones obsoletas.
- **Entradas:** Modificaciones a realizar.
- **Salida:** Confirmación de cambios.
- **Precondiciones:** El administrador debe tener permisos de edición.
- **Postcondiciones:** Contenido actualizado en la plataforma.

---

#### Caso de uso UC04: Ver Registro de Actividades (Log)
- **Actores:** Administrador, Sistema
- **Propósito:** Monitorear todas las actividades de los usuarios en el sistema.
- **Resumen:** El administrador revisa un registro que almacena eventos como inicio de sesión, lecciones completadas, etc
- **Entradas:**  Filtros de búsqueda por fecha o usuario.
- **Salida:** Registro de actividades ordenado por fecha.
- **Precondiciones:** El administrador debe tener permisos avanzados.
- **Postcondiciones:** Registro actualizado de todas las actividades recientes.

---
#### UC05: Visualizar Lista de Usuarios Registrados
- **Actores:** Administrador
- **Propósito:** Permitir al administrador ver una lista de todos los usuarios registrados en la plataforma.
- **Resumen:** El administrador accede a una lista que muestra información básica de cada usuario, como nombre, correo y rol asignado.
- **Entradas:** Solicitud de lista de usuarios.
- **Salida:** Lista con nombres, correos electrónicos y roles.
- **Precondiciones:** El administrador debe estar autenticado.
- **Postcondiciones:** Visualización actualizada de usuarios activos en la plataforma.

---
#### Caso de uso UC06: Restablecer Contraseña de Usuario
- **Actores:** Administrador, Sistema 
- **Propósito:** Permitir al administrador restablecer contraseñas de usuarios que lo soliciten.
- **Resumen:** El administrador selecciona un usuario y genera una nueva contraseña temporal.
- **Entradas:** Selección del usuario afectado.
- **Salida:** Nueva contraseña temporal generada.
- **Precondiciones:** El usuario debe haber solicitado la recuperación.
- **Postcondiciones:** El usuario puede iniciar sesión con la nueva contraseña temporal.

---
#### Caso de uso UC07: Asignar Roles de Usuario
- **Actores:** Administrador, Sistema.
- **Propósito:** Definir el rol de cada usuario registrado en la plataforma.
- **Resumen:** El administrador puede cambiar el rol de un usuario (estudiante, profesor, etc.).
- **Entradas:**  ID del usuario y rol a asignar.
- **Salida:** Confirmación de cambio de rol.
- **Precondiciones:** El usuario debe estar registrado en la plataforma.
- **Postcondiciones:** El usuario tiene permisos según el nuevo rol asignado.

---



## 2. Modelado de Dominio

### Clases principales:
- **Palabra**  
  - `id`: Identificador único  
  - `nombre`: Nombre de la palabra  
  - `definicion`: Definición en español  
  - `pronunciacion`: Guía de pronunciación  
  - `audio`: Archivo de audio con la pronunciación  
  - `categoria`: Grupo de palabras relacionadas (colores, animales, etc.)  

- **Usuario**  
  - `id`: Identificador único  
  - `nombre`: Nombre del usuario  
  - `email`: Correo electrónico  
  - `rol`: Estudiante o profesor  

- **Lección**  
  - `id`: Identificador único  
  - `titulo`: Nombre de la lección  
  - `descripcion`: Breve explicación  
  - `palabras`: Lista de palabras asociadas  

---

## 3. Diseño Robustness  
Utilizar diagramas de robustez para conectar los casos de uso con las clases y definir interacciones.  

---

## 4. Diagramas de Secuencia  
Definir la interacción entre los objetos en cada caso de uso, como la adición de una nueva palabra por parte de un profesor.  

---

## 5. Implementación  

### Base de Datos  
Tablas principales:  
- `usuarios` (id, nombre, email, rol)  
- `palabras` (id, nombre, definicion, pronunciacion, audio, categoria)  
- `lecciones` (id, titulo, descripcion)  
- `leccion_palabra` (id_leccion, id_palabra)  

### Tecnologías  
- **Backend:** Node.js (Express) o Laravel  
- **Frontend:** Vue 3 + Pinia  
- **Base de datos:** PostgreSQL o MongoDB  

---

## 6. Pruebas  
Realizar pruebas con usuarios reales y pruebas automatizadas en cada funcionalidad clave.  

---

## 7. Despliegue  
Subir el proyecto a un servidor y habilitar accesos para los usuarios.  
Posibles opciones:  
- **Backend:** Deploy en Vercel, Render o un VPS.  
- **Frontend:** Netlify, Vercel o Firebase Hosting.  
- **Base de datos:** Supabase, Firebase
