# 📋 Formulario de Registro de Estudiantes - Proyecto Integrador Unidad 1

Aplicación de escritorio/web desarrollada con **Python** y **Flet** que simula un formulario de registro de estudiantes con validaciones y visualización de datos mediante una ventana modal (AlertDialog). El sistema implemeta validaciones de entrada, controles de selección restringida y una ventana modal de confirmación, garantizando integridad de datos y una mejor experiencia para el usuario. La aplicación se ejecuta en el navegador mediante Flet, funcionando como una aplicación web ligera generada desde Python.

---

##  Objetivo del Proyecto
 . Implementar un formulario interactivo
 
 . Aplicar validaciones de datos
 
 . Utilizar controles gráficos avanzados 
 
 . Manejar eventos mediante programación orientada a eventos
 
 . Mejorar la experiencia del usuario mediante retroalimentación visual

---

## Mejoras implementadas

### 1.  Validación de campos vacíos

Antes de procesar el formulario, se verifica que **ningún campo esté vacío**. Si el usuario intenta enviar sin completar alguno, se muestra el mensaje:
> ⚠ Por favor completa todos los campos.

**Esto se implementó verificando el valor de cada control antes de continuar:**
```python
if (
    not txt_nombre.value or
    not txt_control.value or
    not txt_email.value or
    not dd_carrera.value or
    not dd_semestre.value or
    not genero_group.value
):
    txt_error.value = "⚠ Por favor completa todos los campos."
```
**Explicación técnica**

. Se evalua la propiedad .value de cada control.

. Si algún valor es None o vacío, se interrumpe el flujo.

. Se muestra un mensaje en color rojo.

. Se evita continuar con la ejecución del evento.

   Esto garantiza integridad de los datos capturados.


   <img width="992" height="437" alt="Captura" src="https://github.com/user-attachments/assets/b1cc29cb-5b11-49c1-b757-ed0903ec1ff3" />

---

### 2. 📧 Validación de formato de Email
Se agregó una función que utiliza **expresiones regulares** (`regex`) para verificar que el email tenga un formato válido como `usuario@dominio.com`. Si el formato es incorrecto, se muestra:
> ⚠ El formato del email no es válido. Ejemplo: usuario@dominio.com

**Función de validación:**
```python
import re

def es_email_valido(email: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, email) is not None
```
**Análisis de la expresión regula:**
. `^[\w\.-]+` Parte local del correo.

. `@` Separador obligatorio.

. `[\w\.-]+` Dominio.

. `\.\w{2,}` Extensión válida (.com, .mx, .org, etc.).

. `$` Fin de cadena

Si es incorrecto se muestra el mensaje
<img width="988" height="458" alt="Captura1" src="https://github.com/user-attachments/assets/33fbae87-a3e4-478e-84b3-50273d5214c5" />

---

### 3. 📂 Control Dropdown
Se sustituyeron los campos de texto de Carrera y Semestre por controles **Dropdown**, lo que evita que el usuario ingrese datos inválidos y hace la selección más clara:

```python
dd_carrera = ft.Dropdown(
    label="Carrera",
    options=[
        ft.dropdown.Option("Ingeniería en Sistemas"),
        ft.dropdown.Option("Ingeniería Civil"),
        ft.dropdown.Option("Ingeniería Industrial"),
    ]
)

dd_semestre = ft.Dropdown(
    label="Semestre",
    options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
)
```
<img width="964" height="452" alt="Captura2" src="https://github.com/user-attachments/assets/1eb9d35d-80cd-4210-860a-d497cf33f842" />

---

### 4. Control Radio Button (Género)
Se agregó un **RadioGroup** para seleccionar el género del estudiante, con las opciones: Masculino, Femenino y Otro. Esto reemplaza un campo de texto libre:

```python
genero_group = ft.RadioGroup(
    content=ft.Row([
        ft.Radio(value="Masculino", label="Masculino"),
        ft.Radio(value="Femenino", label="Femenino"),
        ft.Radio(value="Otro", label="Otro"),
    ])
)
```
** Características:**
. Selección exclusiva.

. Control del estado mediante `.value`.

.Incluido dentro de la validación general.

<img width="316" height="74" alt="Captura3" src="https://github.com/user-attachments/assets/9d1520d3-8a48-41e9-a044-21b309a26e89" />

---

### 5. Ventana Modal (AlertDialog)
En lugar de mostrar los datos en un simple texto en pantalla, se implementó un **AlertDialog** que se abre al enviar el formulario exitosamente. Muestra todos los datos capturados de forma ordenada y al cerrarlo limpia automáticamente todos los campos:

```python
dialog = ft.AlertDialog(
    title=ft.Text("✅ Registro Exitoso"),
    content=ft.Column([
        ft.Text(f"👤 Nombre:     {txt_nombre.value}"),
        ft.Text(f"🔢 N° Control: {txt_control.value}"),
        ft.Text(f"📧 Email:       {txt_email.value}"),
        ft.Text(f"🎓 Carrera:    {dd_carrera.value}"),
        ft.Text(f"📚 Semestre:  {dd_semestre.value}"),
        ft.Text(f"⚧  Género:     {genero_group.value}"),
    ]),
    actions=[ft.TextButton("Cerrar", on_click=cerrar_dialog)]
)
```
**Características:**
. Se genera dinámicamente con los valores ingresados.

. Confirma visualmente la información registrada.

. Limpia los campos automáticamente al cerrarse.
<img width="347" height="432" alt="Captura4" src="https://github.com/user-attachments/assets/32ce5e39-e61b-44f2-9703-3d7ff6d32c42" />

---

## 🗂️ Campos del formulario

| Campo            | Tipo        | Validación                        |
|------------------|-------------|-----------------------------------|
| Nombre           | TextField   | No vacío                          |
| Número de control| TextField   | No vacío                          |
| Email            | TextField   | No vacío + formato válido         |
| Carrera          | Dropdown    | Selección obligatoria             |
| Semestre         | Dropdown    | Selección obligatoria             |
| Género           | RadioGroup  | Selección obligatoria             |

---

## Tecnologías utilizadas

- **Python 3.10+**
- **Flet** - Framework para construir aplicaciones con Flutter desde Python

---


## Funcionamiento

1. El usuario llena todos los campos del formulario.
2. Al presionar **Enviar**, se validan los datos.
3. Si hay algún error (campo vacío o email inválido), se muestra un mensaje en rojo.
4. Si todo es correcto, se abre un **AlertDialog** con los datos capturados.
5. Al cerrar el modal los campos se limpian automáticamente.

---

