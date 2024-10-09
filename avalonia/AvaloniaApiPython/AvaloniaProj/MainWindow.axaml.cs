using Avalonia;
using Avalonia.Controls;
using Avalonia.Interactivity;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace AvaloniaProj
{
    public partial class MainWindow : Window
    {
        private readonly HttpClient _httpClient;

        public MainWindow()
        {
            InitializeComponent();
            _httpClient = new HttpClient();
        }

        private async void GenerarInstalador_Click(object sender, RoutedEventArgs e)
        {
            string sistemaOperativo = ((ComboBoxItem)SistemaOperativoComboBox.SelectedItem)?.Content?.ToString();
            List<string> fuentes = new List<string>();

            if (ApplicationCheckBox.IsChecked == true)
                fuentes.Add("Application");
            if (SecurityCheckBox.IsChecked == true)
                fuentes.Add("Security");
            if (SystemCheckBox.IsChecked == true)
                fuentes.Add("System");

            if (string.IsNullOrEmpty(sistemaOperativo) || fuentes.Count == 0)
            {
                ResultadoTextBlock.Text = "Por favor, selecciona un sistema operativo y al menos una fuente de ingesta.";
                ResultadoTextBlock.Foreground = Avalonia.Media.Brushes.Red;
                return;
            }

            var solicitud = new
            {
                sistema_operativo = sistemaOperativo,
                fuentes = fuentes
            };

            string json = JsonConvert.SerializeObject(solicitud);
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            try
            {
                ResultadoTextBlock.Text = "Generando instalador...";
                ResultadoTextBlock.Foreground = Avalonia.Media.Brushes.Black;

                var response = await _httpClient.PostAsync("http://127.0.0.1:8000/generar_instalador/", content);
                var respuestaJson = await response.Content.ReadAsStringAsync();

                if (response.IsSuccessStatusCode)
                {
                    dynamic respuesta = JsonConvert.DeserializeObject(respuestaJson);
                    string mensaje = respuesta.mensaje;
                    string archivo = respuesta.archivo;

                    ResultadoTextBlock.Text = $"{mensaje}\nArchivo: {archivo}";
                    ResultadoTextBlock.Foreground = Avalonia.Media.Brushes.Green;
                }
                else
                {
                    dynamic respuesta = JsonConvert.DeserializeObject(respuestaJson);
                    string error = respuesta.detail;
                    ResultadoTextBlock.Text = $"Error: {error}";
                    ResultadoTextBlock.Foreground = Avalonia.Media.Brushes.Red;
                }
            }
            catch (Exception ex)
            {
                ResultadoTextBlock.Text = $"Error de conexión: {ex.Message}";
                ResultadoTextBlock.Foreground = Avalonia.Media.Brushes.Red;
            }
        }
    }
}
