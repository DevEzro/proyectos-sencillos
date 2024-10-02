using Avalonia.Controls;
using Avalonia.Interactivity;
using System;

namespace Prueba
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void OnShowTimeClick(object sender, RoutedEventArgs e)
        {
            TimeTextBlock.Text = DateTime.Now.ToString("hh:mm:ss tt"); // Muestra la hora actual
            TimeTextBlock.IsVisible = true; // Asegúrate de que el TextBlock de la hora sea visible
            OperationPanel.IsVisible = false; // Oculta el panel de operación combinada
        }

        private void OnCombinedOperationClick(object sender, RoutedEventArgs e)
        {
            OperationPanel.IsVisible = true; // Muestra el panel para la operación
            TimeTextBlock.IsVisible = false; // Oculta el TextBlock de la hora
        }

        private void OnSumClick(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(Num1TextBox.Text, out double num1) && double.TryParse(Num2TextBox.Text, out double num2))
            {
                double result = num1 + num2;
                ResultTextBox.Text = result.ToString(); // Muestra el resultado de la suma
                TimeTextBlock.IsVisible = false; // Oculta el TextBlock de la hora después de la suma
            }
            else
            {
                ResultTextBox.Text = "Error: Introduce números válidos."; // Maneja error de entrada
            }
        }

        private void OnCloseClick(object sender, RoutedEventArgs e)
        {
            Close(); // Cierra la aplicación
        }
    }
}