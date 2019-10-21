# Spanish translations for PROJECT.
# Copyright (C) 2017 ORGANIZATION
# This file is distributed under the same license as the PROJECT project.
# FIRST AUTHOR <EMAIL@ADDRESS>, 2017.
#
msgid ""
msgstr ""
"Project-Id-Version: PROJECT VERSION\n"
"Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
"POT-Creation-Date: 2017-11-25 18:26-0800\n"
"PO-Revision-Date: 2017-09-29 23:25-0700\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language: es\n"
"Language-Team: es <LL@li.org>\n"
"Plural-Forms: nplurals=2; plural=(n != 1)\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: Babel 2.5.1\n"

#: app/__init__.py:18
msgid "Please log in to access this page."
msgstr "Por favor ingrese para acceder a esta página."

#: app/translate.py:10
msgid "Error: the translation service is not configured."
msgstr "Error: el servicio de traducciones no está configurado."

#: app/translate.py:18
msgid "Error: the translation service failed."
msgstr "Error el servicio de traducciones ha fallado."

#: app/auth/email.py:8
msgid "[Microblog] Reset Your Password"
msgstr "[Microblog] Nueva Contraseña"

#: app/auth/forms.py:10 app/auth/forms.py:17 app/main/forms.py:10
msgid "Username"
msgstr "Nombre de usuario"

#: app/auth/forms.py:11 app/auth/forms.py:19 app/auth/forms.py:42
msgid "Password"
msgstr "Contraseña"

#: app/auth/forms.py:12
msgid "Remember Me"
msgstr "Recordarme"

#: app/auth/forms.py:13 app/templates/auth/login.html:5
msgid "Sign In"
msgstr "Ingresar"

#: app/auth/forms.py:18 app/auth/forms.py:37
msgid "Email"
msgstr "Email"

#: app/auth/forms.py:21 app/auth/forms.py:44
msgid "Repeat Password"
msgstr "Repetir Contraseña"

#: app/auth/forms.py:23 app/templates/auth/register.html:5
msgid "Register"
msgstr "Registrarse"

#: app/auth/forms.py:28 app/main/forms.py:23
msgid "Please use a different username."
msgstr "Por favor use un nombre de usuario diferente."

#: app/auth/forms.py:33
msgid "Please use a different email address."
msgstr "Por favor use una dirección de email diferente."

#: app/auth/forms.py:38 app/auth/forms.py:46
msgid "Request Password Reset"
msgstr "Pedir una nueva contraseña"

#: app/auth/routes.py:20
msgid "Invalid username or password"
msgstr "Nombre de usuario o contraseña inválidos"

#: app/auth/routes.py:46
msgid "Congratulations, you are now a registered user!"
msgstr "¡Felicitaciones, ya eres un usuario registrado!"

#: app/auth/routes.py:61
msgid "Check your email for the instructions to reset your password"
msgstr "Busca en tu email las instrucciones para crear una nueva contraseña"

#: app/auth/routes.py:78
msgid "Your password has been reset."
msgstr "Tu contraseña ha sido cambiada."

#: app/main/forms.py:11
msgid "About me"
msgstr "Acerca de mí"

#: app/main/forms.py:13 app/main/forms.py:28 app/main/forms.py:44
msgid "Submit"
msgstr "Enviar"

#: app/main/forms.py:27
msgid "Say something"
msgstr "Dí algo"

#: app/main/forms.py:32
msgid "Search"
msgstr "Buscar"

#: app/main/forms.py:43
msgid "Message"
msgstr "Mensaje"

#: app/main/routes.py:36
msgid "Your post is now live!"
msgstr "¡Tu artículo ha sido publicado!"

#: app/main/routes.py:94
msgid "Your changes have been saved."
msgstr "Tus cambios han sido salvados."

#: app/main/routes.py:99 app/templates/edit_profile.html:5
msgid "Edit Profile"
msgstr "Editar Perfil"

#: app/main/routes.py:108 app/main/routes.py:124
#, python-format
msgid "User %(username)s not found."
msgstr "El usuario %(username)s no ha sido encontrado."

#: app/main/routes.py:111
msgid "You cannot follow yourself!"
msgstr "¡No te puedes seguir a tí mismo!"

#: app/main/routes.py:115
#, python-format
msgid "You are following %(username)s!"
msgstr "¡Ahora estás siguiendo a %(username)s!"

#: app/main/routes.py:127
msgid "You cannot unfollow yourself!"
msgstr "¡No te puedes dejar de seguir a tí mismo!"

#: app/main/routes.py:131
#, python-format
msgid "You are not following %(username)s."
msgstr "No estás siguiendo a %(username)s."

#: app/main/routes.py:170
msgid "Your message has been sent."
msgstr "Tu mensaje ha sido enviado."

#: app/main/routes.py:172
msgid "Send Message"
msgstr "Enviar Mensaje"

#: app/templates/_post.html:16
#, python-format
msgid "%(username)s said %(when)s"
msgstr "%(username)s dijo %(when)s"

#: app/templates/_post.html:27
msgid "Translate"
msgstr "Traducir"

#: app/templates/base.html:4
msgid "Welcome to Microblog"
msgstr "Bienvenido a Microblog"

#: app/templates/base.html:21
msgid "Home"
msgstr "Inicio"

#: app/templates/base.html:22
msgid "Explore"
msgstr "Explorar"

#: app/templates/base.html:33
msgid "Login"
msgstr "Ingresar"

#: app/templates/base.html:36 app/templates/messages.html:4
msgid "Messages"
msgstr "Mensajes"

#: app/templates/base.html:45
msgid "Profile"
msgstr "Perfil"

#: app/templates/base.html:46
msgid "Logout"
msgstr "Salir"

#: app/templates/base.html:83
msgid "Error: Could not contact server."
msgstr "Error: el servidor no pudo ser contactado."

#: app/templates/index.html:5
#, python-format
msgid "Hi, %(username)s!"
msgstr "¡Hola, %(username)s!"

#: app/templates/index.html:17 app/templates/user.html:34
msgid "Newer posts"
msgstr "Artículos siguientes"

#: app/templates/index.html:22 app/templates/user.html:39
msgid "Older posts"
msgstr "Artículos previos"

#: app/templates/messages.html:12
msgid "Newer messages"
msgstr "Mensajes siguientes"

#: app/templates/messages.html:17
msgid "Older messages"
msgstr "Mensajes previos"

#: app/templates/search.html:4
msgid "Search Results"
msgstr ""

#: app/templates/search.html:12
msgid "Previous results"
msgstr ""

#: app/templates/search.html:17
msgid "Next results"
msgstr ""

#: app/templates/send_message.html:5
#, python-format
msgid "Send Message to %(recipient)s"
msgstr "Enviar Mensaje a %(recipient)s"

#: app/templates/user.html:8
msgid "User"
msgstr "Usuario"

#: app/templates/user.html:11 app/templates/user_popup.html:9
msgid "Last seen on"
msgstr "Última visita"

#: app/templates/user.html:13 app/templates/user_popup.html:11
#, python-format
msgid "%(count)d followers"
msgstr "%(count)d seguidores"

#: app/templates/user.html:13 app/templates/user_popup.html:11
#, python-format
msgid "%(count)d following"
msgstr "siguiendo a %(count)d"

#: app/templates/user.html:15
msgid "Edit your profile"
msgstr "Editar tu perfil"

#: app/templates/user.html:17 app/templates/user_popup.html:14
msgid "Follow"
msgstr "Seguir"

#: app/templates/user.html:19 app/templates/user_popup.html:16
msgid "Unfollow"
msgstr "Dejar de seguir"

#: app/templates/user.html:22
msgid "Send private message"
msgstr "Enviar mensaje privado"

#: app/templates/auth/login.html:12
msgid "New User?"
msgstr "¿Usuario Nuevo?"

#: app/templates/auth/login.html:12
msgid "Click to Register!"
msgstr "¡Haz click aquí para registrarte!"

#: app/templates/auth/login.html:14
msgid "Forgot Your Password?"
msgstr "¿Te olvidaste tu contraseña?"

#: app/templates/auth/login.html:15
msgid "Click to Reset It"
msgstr "Haz click aquí para pedir una nueva"

#: app/templates/auth/reset_password.html:5
msgid "Reset Your Password"
msgstr "Nueva Contraseña"

#: app/templates/auth/reset_password_request.html:5
msgid "Reset Password"
msgstr "Nueva Contraseña"

#: app/templates/errors/404.html:4
msgid "Not Found"
msgstr "Página No Encontrada"

#: app/templates/errors/404.html:5 app/templates/errors/500.html:6
msgid "Back"
msgstr "Atrás"

#: app/templates/errors/500.html:4
msgid "An unexpected error has occurred"
msgstr "Ha ocurrido un error inesperado"

#: app/templates/errors/500.html:5
msgid "The administrator has been notified. Sorry for the inconvenience!"
msgstr "El administrador ha sido notificado. ¡Lamentamos la inconveniencia!"