# 📌 Especificación de Requerimientos del Sistema

---

## 🔐 Sistema de Autenticación

### ✅ Requerimientos funcionales

- El sistema deberá permitir registro de usuarios mediante email y contraseña.
- El sistema deberá permitir inicio de sesión con credenciales válidas.
- El sistema deberá permitir cerrar sesión.
- El sistema deberá identificar al usuario autenticado en cada solicitud.
- El sistema deberá restringir el acceso a recursos no autenticados.

### ⚙️ Requerimientos no funcionales

- Las contraseñas deberán almacenarse de forma segura (no texto plano).
- Las sesiones deberán ser persistentes y seguras.
- El sistema deberá responder a intentos inválidos sin exponer información sensible.
- El sistema deberá ser escalable para múltiples usuarios concurrentes.

---

## ✉️ Sistema de Invitaciones a Registro

### ✅ Requerimientos funcionales

- El sistema deberá permitir enviar invitaciones a registrarse únicamente a usuarios autenticados.
- El sistema deberá generar una invitación única asociada al emisor.
- El sistema deberá permitir registrarse solo mediante una invitación válida.
- El sistema deberá invalidar la invitación una vez utilizada.

### ⚙️ Requerimientos no funcionales

- Las invitaciones deberán ser difíciles de adivinar.
- El sistema deberá prevenir el uso múltiple de una misma invitación.
- El sistema deberá manejar invitaciones expiradas de forma segura.
- El sistema deberá registrar quién envió cada invitación.

---

## 🎧 Subida de Archivos de Audio

### ✅ Requerimientos funcionales

- El sistema deberá permitir al usuario subir archivos de audio.
- El sistema deberá aceptar múltiples formatos de audio.
- El sistema deberá asociar cada archivo subido al usuario autenticado.
- El sistema deberá almacenar metadatos básicos del archivo.

### ⚙️ Requerimientos no funcionales

- El sistema deberá rechazar archivos corruptos o no válidos.
- La subida deberá ser confiable ante interrupciones.
- Los archivos deberán almacenarse de forma segura y escalable.
- El sistema deberá manejar archivos de gran tamaño sin degradar el servicio.

---

## 🔗 Compartición de Audios

### ✅ Requerimientos funcionales

- El sistema deberá permitir al usuario compartir audios cargados con otros usuarios.
- El sistema deberá permitir definir con quién se comparte cada audio.
- El sistema deberá permitir revocar el acceso a un audio compartido.
- El sistema deberá permitir a los usuarios autorizados reproducir audios compartidos.

### ⚙️ Requerimientos no funcionales

- El sistema deberá respetar los permisos de acceso en todo momento.
- El acceso a audios compartidos deberá ser seguro y controlado.
- El sistema deberá evitar accesos no autorizados a audios privados.
- Los cambios en permisos deberán reflejarse de forma inmediata.

---

## 🔍 Filtrado de Audios

### ✅ Requerimientos funcionales

- El sistema deberá permitir filtrar audios según distintos criterios.
- El sistema deberá permitir combinar múltiples criterios de filtrado.
- El sistema deberá mostrar únicamente los audios que cumplan los criterios seleccionados.
- El sistema deberá permitir restablecer los filtros aplicados.

### ⚙️ Requerimientos no funcionales

- El filtrado deberá ejecutarse con bajo tiempo de respuesta.
- El sistema deberá soportar grandes volúmenes de audios.
- Los resultados deberán ser consistentes y reproducibles.
- El sistema deberá mantener la integridad de los permisos al filtrar.

---

## 📚 Lista de Audios del Usuario

### ✅ Requerimientos funcionales

- El sistema deberá mostrar una lista de todos los audios subidos por el usuario autenticado.
- Cada elemento de la lista deberá mostrar información básica del audio.
- El sistema deberá permitir acceder a la reproducción de cada audio desde la lista.
- El sistema deberá actualizar la lista cuando se agreguen o eliminen audios.

### ⚙️ Requerimientos no funcionales

- La lista deberá cargarse con tiempos de respuesta aceptables.
- El sistema deberá manejar listas extensas de audios.
- La información mostrada deberá ser consistente y precisa.
- El sistema deberá respetar la privacidad del usuario.

---

## 🌐 Lista de Audios Accesibles al Usuario

### ✅ Requerimientos funcionales

- El sistema deberá mostrar una lista de todos los audios a los que el usuario tiene acceso.
- La lista deberá incluir audios compartidos por otros usuarios.
- Cada elemento deberá mostrar información básica del audio y su propietario.
- El sistema deberá permitir reproducir los audios accesibles desde la lista.

### ⚙️ Requerimientos no funcionales

- La lista deberá mostrar solo audios autorizados para el usuario.
- El sistema deberá manejar volúmenes crecientes de audios compartidos.
- Los cambios en permisos deberán reflejarse en tiempo real o casi inmediato.
- El sistema deberá mantener consistencia entre permisos y visibilidad.

---

## 🔎 Filtrado en Listas de Audios

### ✅ Requerimientos funcionales

- El sistema deberá permitir filtrar ambas listas de audios (propios y accesibles).
- El sistema deberá aplicar los mismos criterios de filtrado a ambas listas.
- El sistema deberá permitir combinar múltiples criterios de filtrado.
- El sistema deberá actualizar los resultados dinámicamente al cambiar los filtros.

### ⚙️ Requerimientos no funcionales

- El filtrado deberá ejecutarse con baja latencia.
- El sistema deberá mantener la consistencia de permisos al filtrar.
- El sistema deberá soportar grandes volúmenes de datos.
- Los resultados deberán ser predecibles y estables.

---

## 👥 Gestión de Grupos de Usuarios

### ✅ Requerimientos funcionales

- El sistema deberá permitir crear grupos de usuarios.
- El sistema deberá permitir agregar y remover usuarios de un grupo.
- El sistema deberá permitir eliminar grupos existentes.
- El sistema deberá permitir listar los grupos a los que pertenece un usuario.

### ⚙️ Requerimientos no funcionales

- La gestión de grupos deberá ser segura y controlada.
- El sistema deberá mantener consistencia en la pertenencia a grupos.
- Las operaciones sobre grupos deberán reflejarse de forma inmediata.
- El sistema deberá escalar con múltiples grupos y usuarios.

---

## 🔐 Control de Visibilidad de Audios

### ✅ Requerimientos funcionales

- El sistema deberá permitir definir la visibilidad de un audio al momento de cargarlo.
- El sistema deberá soportar los siguientes niveles de acceso:
  - **Privado** (solo el propietario).
  - **Público** (usuarios autorizados del sistema).
  - **Restringido a un grupo específico**.
- El sistema deberá permitir modificar la visibilidad de un audio existente.
- El sistema deberá controlar el acceso a los audios según su nivel de visibilidad.

### ⚙️ Requerimientos no funcionales

- Los controles de acceso deberán aplicarse de forma estricta y consistente.
- Los cambios de visibilidad deberán reflejarse de inmediato.
- El sistema deberá prevenir accesos no autorizados a audios privados.
- La lógica de permisos deberá ser mantenible y escalable.
