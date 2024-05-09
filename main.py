import flet as ft
from montecarlo import simulacion

#DIMENSIONES 1300X900 PX

def main(page: ft.Page):
    page.title = "Flet counter example"
    metricas = []
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def servidoresChange(e):
        print(e.control.value)

    def reiniciar_simulacion(e):
        servidoresText.value = ""
        clientesText.value = ""
        serviciosText.value = ""
        tiempoEjecucionText.value = ""
        numSimulacionesText.value = ""
        tiempo_espera_promedio_text.value = "Ingresa los valores para continuar"
        tiempo_sistema.value = ""
        utilizacion_servidores.value = ""
        results.visible = True
        loading_column.visible = False
        page.update()

    def iniciarSimulacion(e):

        if servidoresText.value == "" or clientesText.value == "" or serviciosText.value == "" or tiempoEjecucionText.value == "" or numSimulacionesText.value == "":
            tiempo_espera_promedio_text.value = "Ingresa todos los campos correspondientes"
            return

        results.visible = False
        loading_column.visible = True
        page.update()
        print("Simulacion iniciada")
        print("Numero de servidores: ", servidoresText.value)
        print("Tasa de clientes: ", clientesText.value)
        print("Tasa de servicios: ", serviciosText.value)
        print("Tiempo de ejecucion: ", tiempoEjecucionText.value)
        metricas = simulacion(int(serviciosText.value), int(clientesText.value), int(serviciosText.value), int(tiempoEjecucionText.value), int(numSimulacionesText.value))
        tiempo_espera_promedio_text.value = f"Tiempo de espera promedio: {round(metricas['tiempo_espera_promedio'], 2)}"
        tiempo_sistema.value = f"Tiempo de sistema: {round(metricas['tiempo_sistema'], 2)}"
        utilizacion_servidores.value = f"Utilizacion de servidores: {round(metricas['utlizizacion_servidores'],2) * 100}%"
        results.visible = True
        loading_column.visible = False
        page.update()
        print(metricas)

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
        label = "Tiempo de ejecucion",
        input_filter= ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
    )

    numSimulacionesText = ft.TextField(
        label = "Numero de simulaciones",
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
        height=60,
        on_click= reiniciar_simulacion
        )

    loading_circle = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=10
    )

    container = ft.Column(
        [
            servidoresText,
            clientesText,
            serviciosText,
            tiempoEjecucionText,
            numSimulacionesText,
            btnEjecutar,
            btnReiniciar
        ],
        width=100,
        height=650,
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        
    )

    loading_column = ft.Column(
        [
            loading_circle
        ],
        width=250,
        height=650,
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        visible=False
    )

    tiempo_espera_promedio_text = ft.Text("Ingresa los valores para continuar", theme_style=ft.TextThemeStyle.TITLE_LARGE)
    tiempo_sistema = ft.Text("", theme_style=ft.TextThemeStyle.TITLE_LARGE)
    utilizacion_servidores = ft.Text("", theme_style=ft.TextThemeStyle.TITLE_LARGE)

    results = ft.Column(
        [
            tiempo_espera_promedio_text,
            tiempo_sistema,
            utilizacion_servidores
        ],
        width=700,
        height=650,
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    page.add(ft.Row(
        [
            container,
            loading_column,
            results
        ],
        spacing=300,
    ))



ft.app(main)