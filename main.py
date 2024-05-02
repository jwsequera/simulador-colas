import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"

    def servidoresChange(e):
        if e.control.value.contains("a"):
                e.control.value = e.control.value.replace("a", "")
                page.update()

        else:
            serviciosText.value = e.control.value
            page.update()


    servidoresText = ft.TextField(
        label = "Numero de servidores",
        value = 0,
        on_change= servidoresChange
            
    )

    clientesText = ft.TextField(
        label = "Tasa de clientes",
        value = 0
    )

    serviciosText = ft.TextField(
        label = "Tasa de servicios",
        value = 0
    )

    btnEjecutar = ft.ElevatedButton(
        text="Ejecutar",
        width= 300
        )
    btnReiniciar = ft.ElevatedButton(
        text="Reiniciar",
        width= 300
        )

    inputCol = ft.Column(
            [
                servidoresText,
                clientesText,
                serviciosText,
                btnEjecutar,
                btnReiniciar
            ],
            height= 600,
            spacing=50
        )

    mainRow = ft.Row([
        inputCol,
    ])

    page.add(mainRow)



ft.app(main)