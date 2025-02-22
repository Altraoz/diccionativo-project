# Proyecto: IndiLingo

## 1. Requisitos y Casos de Uso

### Actores:
- **Estudiantes:** Pueden buscar palabras y repasar vocabulario.
- **Profesores:** Pueden agregar, editar y eliminar palabras.
- **Administrador (Opcional):** Puede gestionar usuarios y controlar contenido.

### Casos de Uso:
- Un estudiante busca palabras en el diccionario.
- Un estudiante repasa vocabulario mediante ejercicios.
- Un profesor agrega una nueva palabra con su definición y pronunciación.
- Un profesor edita o elimina palabras existentes.
- (Opcional) Un administrador gestiona usuarios y contenido.

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
