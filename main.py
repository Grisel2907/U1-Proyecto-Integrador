import flet as ft
import re

def main(page: ft.Page):
    # ---------------- CONFIGURACIÓN ----------------
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # ---------------- CONTROLES ----------------
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True)
    txt_control = ft.TextField(label="Número de control", border_color="#4D2A32", expand=True)
    txt_email = ft.TextField(label="Email", border_color="#4D2A32")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # ---------------- RADIO BUTTON GÉNERO ----------------
    genero_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro"),
        ])
    )

    # ---------------- MENSAJE DE ERROR ----------------
    txt_error = ft.Text("", color="red", weight=ft.FontWeight.BOLD)

    # ---------------- VALIDACIÓN EMAIL ----------------
    def es_email_valido(email: str) -> bool:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return re.match(patron, email) is not None

    # ---------------- FUNCIÓN CERRAR DIALOG ----------------
    def cerrar_dialog(e):
        dialog.open = False
        # Limpiar campos
        txt_nombre.value = ""
        txt_control.value = ""
        txt_email.value = ""
        dd_carrera.value = None
        dd_semestre.value = None
        genero_group.value = None
        txt_error.value = ""
        page.update()

    # ---------------- ALERT DIALOG ----------------
    dialog = ft.AlertDialog(
        title=ft.Text("✅ Registro Exitoso", weight=ft.FontWeight.BOLD, color="#4D2A32"),
        content=ft.Text(""),  # Se llenará dinámicamente
        actions=[
            ft.TextButton("Cerrar", on_click=cerrar_dialog)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # ---------------- FUNCIÓN ENVIAR ----------------
    def enviar_click(e):
        txt_error.value = ""

        # Validar campos vacíos
        if (
            not txt_nombre.value or
            not txt_control.value or
            not txt_email.value or
            not dd_carrera.value or
            not dd_semestre.value or
            not genero_group.value
        ):
            txt_error.value = "⚠ Por favor completa todos los campos."
            page.update()
            return

        # Validar formato de email
        if not es_email_valido(txt_email.value):
            txt_error.value = "⚠ El formato del email no es válido. Ejemplo: usuario@dominio.com"
            page.update()
            return

        # Mostrar datos en AlertDialog
        dialog.content = ft.Column([
            ft.Text(f"👤 Nombre:    {txt_nombre.value}"),
            ft.Text(f"🔢 N° Control: {txt_control.value}"),
            ft.Text(f"📧 Email:       {txt_email.value}"),
            ft.Text(f"🎓 Carrera:    {dd_carrera.value}"),
            ft.Text(f"📚 Semestre:  {dd_semestre.value}"),
            ft.Text(f"⚧  Género:     {genero_group.value}"),
        ], tight=True, spacing=8)

        dialog.open = True
        page.overlay.append(dialog)
        page.update()

    # ---------------- BOTÓN ----------------
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=400,
        on_click=enviar_click
    )

    # ---------------- INTERFAZ ----------------
    page.add(
        ft.Column([
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            ft.Text("Género:", color="#4D2A32", weight=ft.FontWeight.BOLD),
            genero_group,
            btn_enviar,
            txt_error,
        ], spacing=15)
    )

# Ejecutar en navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
