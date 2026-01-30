# 🎧 Audio Platform

Audio Platform es una aplicación web que permite a los usuarios **subir, organizar y reproducir archivos de audio**, con un sistema de acceso controlado basado en **invitaciones, compartición entre usuarios y grupos**.

El proyecto está pensado como una **plataforma personal de streaming de audio**, similar en concepto a Spotify, pero enfocada en contenido propio y privado. También funciona como un **proyecto de portfolio**, orientado a demostrar diseño de sistemas, arquitectura y buenas prácticas de desarrollo.

---

## 🚀 Funcionalidad principal

- Subir archivos de audio en distintos formatos.
- Reproducir audios desde cualquier dispositivo con acceso a la web.
- Visualizar una biblioteca personal de audios.
- Compartir audios con otros usuarios de la plataforma.
- Controlar la visibilidad de los audios:
  - Privados
  - Públicos
  - Compartidos con grupos específicos
- Crear y gestionar grupos de usuarios para compartir audios de forma colectiva.

---

## 🔐 Sistema de acceso

- El registro de nuevos usuarios **solo es posible mediante invitación**.
- Solo usuarios ya registrados pueden enviar invitaciones.
- Cada usuario accede únicamente a los audios que:
  - Ha subido
  - Han sido compartidos explícitamente con él
  - Pertenecen a grupos de los que forma parte

---

## 👥 Grupos de usuarios

- Los usuarios pueden crear grupos.
- Un grupo puede contener múltiples usuarios.
- Los audios pueden compartirse con uno o varios grupos.
- Los permisos se gestionan automáticamente según la pertenencia al grupo.

---

## 🧱 Arquitectura general

La aplicación sigue una arquitectura desacoplada:

- **Backend**: API responsable de la lógica de negocio, autenticación y control de permisos.
- **Frontend**: Interfaz web para interacción del usuario y reproducción de audio.
- **Base de datos**: Almacenamiento relacional para usuarios, audios, grupos e invitaciones.
- **Almacenamiento de archivos**: Manejo de archivos de audio de forma segura y escalable.

---

## 🎯 Objetivos del proyecto

- Construir una aplicación web funcional y realista.
- Diseñar un sistema con control de acceso y permisos no triviales.
- Aplicar buenas prácticas de organización de código.
- Servir como proyecto de aprendizaje y portfolio profesional.

---

## 📦 Estado del proyecto

🚧 En desarrollo  
Las funcionalidades se están implementando de forma incremental, priorizando primero la arquitectura y el diseño del sistema.

---

## 📝 Licencia

Copyright (c) 2026 Cesar Londoño

All rights reserved.

This software is provided for educational and portfolio purposes only.
No part of this project may be used, copied, modified, or distributed
without explicit permission from the author.
