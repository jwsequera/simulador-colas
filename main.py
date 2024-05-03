import flet as ft

#DIMENSIONES 1300X900 PX

def main(page: ft.Page):
    page.title = "Flet counter example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def servidoresChange(e):
        print(e.control.value)

    def iniciarSimulacion(e):
        print("Simulacion iniciada")
        print("Numero de servidores: ", servidoresText.value)
        print("Tasa de clientes: ", clientesText.value)
        print("Tasa de servicios: ", serviciosText.value)
        print("Tiempo de ejecucion: ", tiempoEjecucionText.value)

    servidoresText = ft.TextField(
        label = "Numero de servidores",
        input_filter= ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            
    )

    clientesText = ft.TextField(
        label = "Tasa de clientes",
        input_filter= ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
    )

    serviciosText = ft.TextField(
        label = "Tasa de servicios",
        input_filter= ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
    )

    tiempoEjecucionText = ft.TextField(
        label = "Tiempo de ejecucion (horas)",
        input_filter= ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
    )

    btnEjecutar = ft.ElevatedButton(
        text="Ejecutar",
        width= 500,
        height=60,
        on_click= iniciarSimulacion
        )
    btnReiniciar = ft.ElevatedButton(
        text="Reiniciar",
        width= 500,
        height=60
        )

    container = ft.Column(
        [
            servidoresText,
            clientesText,
            serviciosText,
            tiempoEjecucionText,
            btnEjecutar,
            btnReiniciar
        ],
        width=500,
        height=100,
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    page.add(container)



ft.app(main)