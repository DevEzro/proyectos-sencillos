using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Interactivity;
using System;
using System.Diagnostics;

namespace MiApp;

public partial class MainWindow : Window
{

    public MainWindow()
    {
        InitializeComponent();
        // Tamaño de la venta y la propiedad de redimensionar en false
        this.Width=880;
        this.Height=190;
        this.CanResize = false;
    }
    
    # region OPERACIONES
    // Cadena a rellenar con el simbolo de la operación para más adelante
    private string operacionSeleccionada = "";

    // Suma de las operaciones
    public void SetSuma(object sender, RoutedEventArgs e)
    {   
        // Operacion seleccionada se inicializará con la que corresponde
        // El simbolo de la operación pertinente
        operacionSeleccionada = "Suma";
        SimboloOperacion.Text = "+";
    }

    public void SetResta(object sender, RoutedEventArgs e)
    {
        operacionSeleccionada = "Resta";
        SimboloOperacion.Text = "-";
    }

    public void SetMultiplicacion(object sender, RoutedEventArgs e)
    {
        operacionSeleccionada = "Multiplicacion";
        SimboloOperacion.Text = "x";
    }

    public void SetDivision(object sender, RoutedEventArgs e)
    {
        operacionSeleccionada = "Division";
        SimboloOperacion.Text = "/";
    }

    // Se comprueban las cadenas de la operacion seleccionada y se realizan
    public void EjecutarOperacion(object sender, RoutedEventArgs e)
    {
        if (double.TryParse(Num1TextBox.Text, out double num1) && double.TryParse(Num2TextBox.Text, out double num2))
        {
            double resultado = 0;

            switch (operacionSeleccionada)
            {
                case "Suma":
                    resultado = num1 + num2;
                    break;
                case "Resta":
                    resultado = num1 - num2;
                    break;
                case "Multiplicacion":
                    resultado = num1 * num2;
                    break;
                case "Division":
                    if (num2 != 0)
                    {
                        resultado = num1 / num2;
                    }
                    else
                    {
                        ResultTextBox.Text = "Error: División por cero."; // Maneja división por cero
                        return;
                    }
                    break;
                default:
                    ResultTextBox.Text = "Error: Seleccione una operación."; // Manejo de error si no hay operación seleccionada
                    return;
            }
            ResultTextBox.Text = resultado.ToString(); // Muestra el resultado
        }
        else
        {
            ResultTextBox.Text = "Error: Introduce números válidos."; // Maneja error de entrada
        }
    }
    #endregion

    // Redirije a la URL indicada tras pulsar sobre la imagen
    # region Pulsar imagen -> Navegador
    private void Border_PointerPressed(object sender, PointerPressedEventArgs e)
    {
        string url = "https://github.com/DevEzro";
        Process.Start(new ProcessStartInfo{
            FileName = url,
            UseShellExecute = true
        });
    }
    # endregion
}