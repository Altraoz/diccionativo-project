# Proyecto: IndiLingo

## 1. Requisitos y Casos de Uso

### Actores:
- **Estudiantes:** Pueden buscar palabras y repasar vocabulario.
- **Profesores:** Pueden agregar, editar y eliminar palabras.
- **Administrador (Opcional):** Puede gestionar usuarios y controlar contenido.

---

### Casos de Uso para Estudiantes:

#### Caso de uso UC01-01: Registro en la Plataforma
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir que un nuevo usuario cree una cuenta en la plataforma.
- **Resumen:** El estudiante completa un formulario de registro proporcionando sus datos personales. El sistema verifica la validez de los datos e inicia la creación de la cuenta.
- **Entradas:** Nombre, correo electrónico, contraseña, país, nivel de conocimiento del idioma.
- **Salida:** Confirmación de cuenta creada, acceso a la plataforma.
- **Precondiciones:** El estudiante debe tener una dirección de correo válida.
- **Postcondiciones:** El estudiante tiene acceso al contenido inicial de la plataforma.

---

#### Caso de uso UC01-02: Iniciar Sesión
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir el acceso al sistema mediante credenciales válidas.
- **Resumen:** El estudiante proporciona sus credenciales, y el sistema valida la información.
- **Entradas:** Correo electrónico, contraseña.
- **Salida:** Acceso concedido a la cuenta del usuario.
- **Precondiciones:** El estudiante debe estar registrado.
- **Postcondiciones:** El estudiante accede a su panel personalizado.

---

#### Caso de uso UC01-03: Completar Lección Interactiva
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir al estudiante participar en ejercicios prácticos.
- **Resumen:** El estudiante realiza actividades de escritura, lectura o comprensión.
- **Entradas:** Respuestas a preguntas o ejercicios interactivos.
- **Salida:** Retroalimentación inmediata, puntuación obtenida.
- **Precondiciones:** El estudiante debe estar autenticado.
- **Postcondiciones:** El progreso se actualiza con los resultados obtenidos.

---

#### Caso de uso UC01-04: Consultar el Glosario de Términos
- **Actores:** Estudiante, Sistema
- **Propósito:** Permitir a los estudiantes consultar definiciones de palabras en la lengua indígena.
- **Resumen:** El estudiante busca términos específicos y accede a su definición y pronunciación.
- **Entradas:** Término a buscar.
- **Salida:** Definición y recursos multimedia asociados.
- **Precondiciones:** El estudiante debe estar autenticado.
- **Postcondiciones:** Registro de consultas para análisis de uso del sistema.

#### Caso de uso UC01-05: Visualizar Progreso de Aprendizaje
- **Actores:** Estudiante, Sistema
- **Propósito:** Mostrar el avance del estudiante en las lecciones y ejercicios completados.
- **Resumen:** El estudiante accede a una sección donde puede ver su progreso.
- **Entradas:** Solicitud de visualización de progreso.
- **Salida:** Reporte con porcentaje de avance, niveles completados y estadísticas.
- **Precondiciones:** El estudiante debe haber completado al menos una lección.
- **Postcondiciones:** Visualización de datos actualizados del progreso.

---

#### Caso de uso UC01-06:  Configuración de Perfil
- **Actores:** Estudiante, Sistema
- **Propósito:** Personalizar información del perfil de usuario.
- **Resumen:** El estudiante modifica su foto, idioma de interfaz o preferencias.
- **Entradas:** Nuevos datos (ej: imagen, configuración).
- **Salida:** Perfil actualizado.
- **Precondiciones:** Usuario autenticado.
- **Postcondiciones:** Cambios guardados en la base de datos.

---

#### Caso de uso UC01-07: Ejercicio de Traducción
- **Actores:**  Estudiante, Sistema
- **Propósito:** Traducir frases del idioma indígena al español o viceversa.
- **Resumen:** El estudiante escribe la traducción de una frase y el sistema la valora.
- **Entradas:** Texto ingresado por el usuario.
- **Salida:** Corrección inmediata con explicaciones gramaticales.
- **Precondiciones:** Lección de vocabulario completada.
- **Postcondiciones:**  Puntuación añadida al progreso

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
