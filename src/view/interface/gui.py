from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from datetime import datetime
import sys
sys.path.append("src")
from model.calculadora import calcular_retencion

# Añade la ruta donde está la fuente Roboto
resource_add_path('fonts')

class ResultadosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, padding=60, spacing=30)
        self.add_widget(self.layout)
        Window.clearcolor = get_color_from_hex('FF0000')  # Cambio del color de fondo a rojo
        self.resultados_label = Label(text="", font_name='fonts/Roboto-Regular.ttf', font_size=14, halign='left', valign='top', color=get_color_from_hex('1D1D1'))
        self.layout.add_widget(self.resultados_label)

    def mostrar_resultados(self, resultados_text):
        self.resultados_label.text = resultados_text

class RentaApp(App):
    def build(self):
        # Configura el administrador de pantallas
        self.screen_manager = ScreenManager()

        # Parte donde se agregan los datos
        self.ingreso_screen = Screen(name="ingreso")
        self.ingreso_layout = GridLayout(cols=2, padding=20, spacing=10)
        self.ingreso_screen.add_widget(self.ingreso_layout)

        self.ingreso_layout.add_widget(Label(text="Salario básico:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.salario_input = TextInput(hint_text="Salario básico", multiline=False)
        self.ingreso_layout.add_widget(self.salario_input)

        self.ingreso_layout.add_widget(Label(text="Otros ingresos:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.otros_ingresos_input = TextInput(hint_text="Otros ingresos", multiline=False)
        self.ingreso_layout.add_widget(self.otros_ingresos_input)

        self.ingreso_layout.add_widget(Label(text="Retención en la fuente:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.retencion_input = TextInput(hint_text="Retención en la fuente", multiline=False)
        self.ingreso_layout.add_widget(self.retencion_input)

        self.ingreso_layout.add_widget(Label(text="Seguridad social:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.seguridad_social_input = TextInput(hint_text="Seguridad social", multiline=False)
        self.ingreso_layout.add_widget(self.seguridad_social_input)

        self.ingreso_layout.add_widget(Label(text="Aportes de pensión:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.aportes_pension_input = TextInput(hint_text="Aportes de pensión", multiline=False)
        self.ingreso_layout.add_widget(self.aportes_pension_input)

        self.ingreso_layout.add_widget(Label(text="Gastos en créditos hipotecarios:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.creditos_hipotecarios_input = TextInput(hint_text="Gastos en créditos hipotecarios", multiline=False)
        self.ingreso_layout.add_widget(self.creditos_hipotecarios_input)

        self.ingreso_layout.add_widget(Label(text="Donaciones:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.donaciones_input = TextInput(hint_text="Donaciones", multiline=False)
        self.ingreso_layout.add_widget(self.donaciones_input)

        self.ingreso_layout.add_widget(Label(text="Gastos en educación:", font_name='fonts/Roboto-Regular.ttf', color=get_color_from_hex('#FFFFFF')))
        self.gastos_educacion_input = TextInput(hint_text="Gastos en educación", multiline=False)
        self.ingreso_layout.add_widget(self.gastos_educacion_input)

        self.calcular_button = Button(text="Calcular", size_hint_x=None, width=150, font_name='fonts/Roboto-Regular.ttf')
        self.calcular_button.bind(on_press=self.calcular)  # Enlaza el botón con la función calcular
        self.ingreso_layout.add_widget(self.calcular_button)

        # Agrega la pantalla de ingreso a la administración de pantallas
        self.screen_manager.add_widget(self.ingreso_screen)

        # Se agrega la pantalla donde aparecen los resultados
        self.resultados_screen = ResultadosScreen(name="resultados")
        self.screen_manager.add_widget(self.resultados_screen)  # Se agrega la pantalla de resultados al ScreenManager
        return self.screen_manager

    def calcular(self, instance):
        try:
            # Verifica si algún campo está en blanco o no es numérico
            if '' in [self.salario_input.text, self.otros_ingresos_input.text, self.retencion_input.text,
                    self.seguridad_social_input.text, self.aportes_pension_input.text,
                    self.creditos_hipotecarios_input.text, self.donaciones_input.text,
                    self.gastos_educacion_input.text] or not self.salario_input.text.isnumeric():
                # Si hay campos en blanco o el salario básico no es numérico, muestra un mensaje de error y no realiza el cálculo
                self.resultados_screen.mostrar_resultados("Error: Por favor ingresa un salario básico válido.")
                self.screen_manager.current = "resultados"
                return

            # Si todos los campos están llenos y el salario básico es numérico, procede con el cálculo
            salario_basico = float(self.salario_input.text)
            valor_uvt = 35611  # Aquí debes proporcionar el valor actual de la UVT
            retencion_calculada = calcular_retencion(salario_basico, valor_uvt)  # Pasamos el salario básico y el valor de la UVT como argumentos
            resultado_text = f"La retención calculada es: {retencion_calculada}"
            self.resultados_screen.mostrar_resultados(resultado_text)
            self.screen_manager.current = "resultados"  # Se hace el cambio de pantalla a donde están los resultados
        except Exception as e:
            print("Error durante el cálculo:", e)



    def on_start(self):
        self.root_window.title = "Calculadora de Declaración de Renta"

if __name__ == "__main__":
    RentaApp().run()
