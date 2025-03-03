# Proyecto: IndiLingo

## 1. Definición de Requisitos:

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
- **RF02:** El sistema debe implementar un mecanismo de usuario y contraseña para acceso seguro.
- **RF03:** El sistema debe permitir a los usuarios modificar su perfil y preferencias.
- **RF04:** El sistema debe permitir a los administradores gestionar roles de usuarios.
- **RF05:** El sistema debe implementar un mecanismo de recuperación de contraseñas.

### 1.2 Gestión de Contenido Educativo
- **RF06:** El sistema debe organizar el contenido en lecciones secuenciales.
- **RF07:** El sistema debe permitir la descarga de material complementario PDF.
- **RF08:** El sistema debe incluir un glosario de términos con definiciones y pronunciación.
- **RF09:** El sistema debe proporcionar ejercicios de traducción del idioma indígena al español.
- **RF10:** El sistema debe permitir a los administradores crear y editar lecciones interactivas.

### 1.3 Seguimiento y Evaluación
- **RF11:** El sistema debe proporcionar retroalimentación inmediata en los ejercicios.
- **RF12:** El sistema debe mantener un registro de actividades para administración.

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


## Actores:
- **Estudiantes:** Pueden buscar palabras y repasar vocabulario.
- **Profesores:** Pueden agregar, editar y eliminar palabras.
- **Administrador:** Puede gestionar usuarios y controlar contenido.

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
- **Propósito:** Permitir al estudiante descargar recursos adicionales PDFs.
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

### Diagramas de Robustez Administrador.
Asignar Roles de Usuario

![Asignar Roles de Usuario](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Asignar%20Roles%20de%20Usuario.png)

Crear Nueva Lección

![Crear Nueva Lección](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Crear%20Nueva%20Leccion.png)

Editar o Eliminar Contenido

![Editar o Eliminar Contenido](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Editar%20o%20Eliminar%20Contenido.png)

Registrar Nuevo Instructor

![Registrar Nuevo Instructor](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Registrar%20Nuevo%20Instructor.png)

Restablecer Contraseña de Usuario

![Restablecer Contraseña de Usuario](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Restablecer%20Contrase%C3%B1a%20de%20Usuario.png)

Ver Registro de Actividades (Log)

![Ver Registro de Actividades (Log)](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Ver%20Registro%20de%20Actividades(Log).png)

Visualizar Lista de Usuarios Registrados

![Visualizar Lista de Usuarios Registrados](https://raw.githubusercontent.com/Altraoz/diccionativo-project/main/documentation/Diagramas%20de%20Robustez%20Administrador/Visualizar%20Lista%20de%20Usuarios%20Registrados.png)

---

## 4. Diagramas de Secuencia  
Definir la interacción entre los objetos en cada caso de uso, como la adición de una nueva palabra por parte de un profesor.  

### Diagrama de Secuencia Administrador
![Diagrama Generado](https://www.plantuml.com/plantuml/png/jPN1QXin48RlVeeXbvn2xmMNE4umWJY56FS-rexD5Araf5tJverwwA7q4VnY7KbhhMNMn2NavhN-_zVCDqYwzGswfgqrN4-gcWtxnc5btVK8LMCT57-Ejg9bnLiq3LmzceRS6b-XeYEPulrVSmNeOVbOwXUoJZK6-Ony4tJXzzAtwDZww5dCbXUPfbOsDrnbs_IiRMuDIoTaat9U2k_GKr3TOzDbtT-DHkCnlD0czkFWkQMTXKSZNsraCXwF2YnmyqMQXS-YsJZo25K8arGDd5qZKOXE6XJXWzdjVv_HYKA4KeRe9hf6HGP1Mp-i5jbDZXKgQtPYEM1ogGaBz8F5R4DuhlRPDhncXR3_5LPZWR9Mj2QoUKlX0seo7hz7MEfudqXhwgWZXV14AYwSvpHHYYG6GKMRYJRTsJAegIWNLhFY1c5jNTrgT1nwcEQa5n88fbY-R3IW1tSiHnEsohEOjUWgB7mP_lG8FcoYiCg5lXDsCaJA3vMWS63XGRFuqFNdu3pi1SLwhUaB1mIAKP-e2ng6FWWhCqaz-rQBaasO00vWkQTTItf7cMXcafjDAyFLpssLk5deQXsQbi9wnIVpcgYcHSsls3NvnjoAa0yv8z_87MuL6nHI8E-umehy-UdbMUp8vUFi3mpcFGAVX6qLTeOrwwWJnUci-fJCOPvFKbxDtc9Is9Vy5egS4rhDlWI2VPgCWoVHuF4hS049VV2qdQUuMWzjvjL39HBcYylrwwfXCZIGrr-g6Kn_8onFgQI0jtZayFIuY6EbIL4wmWuzxV_W1OSu1nLDpyYGm-uYLNrWqMy-4A0SLMGKewQYsTF3y8xtOg0OQAZUMeSw8fXutXYK4s4r-Vzf77x6Q0lEwXv2qT-MNCs-77U-IO8Fo816MAN7Fuxsuq2eqrSvHSglsC8jcQgjzJy0)

### Diagrama de Secuencia - Estudiante
![Diagrama Generado](https://www.plantuml.com/plantuml/png/XPH1Rjmw38RtFWKncwnoWG3pa9StmM0MmGioJRhcIFIKWIovb6GqkL4NMNMNxLoiiZs655HjbxP-_kH7KRps0IN4pi35hGzHCzf05msgu0JodwPFAbRSfmzOxT8VQV4LFjDX1UZXSVTHi6SVg4FG15loWKy_xAJRRnkD0G_e2LOtw6bKR30uFnrlRffclOO7EgPuSK0M3CAzII6ja-ItNZUv9hZy9oM-WlzSrniA2ACc6XHsewsSNPh7NLAcr5TmQuVJ6u8U4twGxBT9aj9VmJQYQ0IsKq8rLfwK1YYtOdC3bxDXIcrRJhhIQIdhBgOOGUZ8UdnEl1dh6wS2t6g2tLbMZ09xycEoAc8I7OKyWXBIP9FUa2-udj2m_dXQ83sHSCiA8VeuDgS4UA3Wn28CeyECMo0aF9Ki0PKYxwPoD-GLoX45xZ0aOpIG1F_sxiNLIz-J8QNOMOHkYK3GYqr1iNU65GS45FM5X_9M_Zy49akmE9G86neYcO6AiDosP9YJJG29oKSJK61hd5-6vTFfktHidVzp_yCicq8EftV_DPB66eAcbYtdyLa2CzDII3QjGfL6Bz2b0Ev8CrO6JMZoq_D5FR6FQFWL1Ux5ZUMx-QQ4h4w_dwcAcX464l0H-dDmGRdSHfzzpJ9SDK3o0VNfpGTMw2lJjpp8x5YXcryaZIeSq2fQRhFbOnHSMWtt92sREjkTq-DBo0aDz9FyTpi2LPYRg9t_TKaex0wSL6GXErMsGxOf7rXrHypLbtddBN7xJA9OdOTLK4Ub_hukGY5CST4Yj8AUIjm1pUaTmKppqu_rOEKEyo4e9q8gO6rSAx8AxNoqp7GVROZdpZJNP7Nip4y0)

### Diagrama de Secuencia - Profesor
![Diagrama Generado](https://www.plantuml.com/plantuml/png/fLP1RYCt4BpFAnew9K3y0GCAB5k28I1EZ2XspYso9N318GSaHrZxJpxj4_InRLAS5MT5xIomju5PNLtLNQHrvmEwqBUwGH6iWsTdT-IjQpfqGGdLeGamMvj0ReVly3zjPu0UNjPZm4RvG2s297Wa7zJnYudV3vOBZPBMfwhDuqCZCU0MFS7i7Zr5q193Fb_UDyry3ekUYvWRHUAPpvj15TpyoQrlOMtsZZm2WaReD0RSMTTYyxAE26vp2w_ar8uv04Ti3HyoXblTHdM-rm51E99aX49DlbdUmyr0yY_vhcS_qLYLAEjP2C7oG5WZIBBTQ8EBzye7Xmx-xkc0y1U9guOsfEEfDGYpCNfMcjfOhOGA2D5khz4foygY_a9KfdoAmbq9lUZwODjEqvZkj_-E7w7NzWyGUNdyoOT1jMmDVo_bhCpX-84WumAZ3erWadWsSp7jnnwTn0gc73YlPATSYs98q3vLILjprfBn-8bWDimg3K8Yq6V5Yf3F0ytIBb8ehK472MiD-QarL4hgkz3A1rQO1Z0WI-F_R8CYG-MOV84ixI_fq9C-P6pDSsesRXNzhQGAw7usOhqvZnywT0YKwgls90NKchBoeQv-aPJPsN9x9Nvyhu9r9YUd04vdcC5HR49UM7ooCjtvStJXBIS81BPRPVtL-A88FMhrZjAEjhSO_Wvw8hDdYfgFUcABjb6rSoH2cTkLLgqolxJPp53ThVZ-kcNqnOQpZiaPL0Yc9f0h99uSBxpQHyDF6CWfr57LehDlTkg-NYtymQsDc3RZOyALxwnHM_wknhk44c0ahyQwJbaPHubCs_BV3BdhPizb76_9HCfWG5TFjpyPxcMId6PqxMakJil1L1UTmTDx7jQH2wGjObvvdf_phugpZ9LdyGfDc7woNsc2e1Q5uXNgHhNL2BZJF_KJNZ6dGt6-FUTErLpmEShZ1tiLM6bOcMDTM-NfMvZqYiJtBiyIzFWzRkx8oBxLNm40)



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
