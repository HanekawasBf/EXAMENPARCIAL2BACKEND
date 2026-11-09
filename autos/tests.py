from django.test import TestCase

from .models import Auto


class AutoViewsTests(TestCase):
    def test_lista_muestra_estado_vacio(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todavía no hay autos registrados.")

    def test_agregar_auto_y_mostrarlo_en_lista(self):
        response = self.client.post(
            "/nuevo/",
            {
                "marca": "Toyota",
                "modelo": "Corolla",
                "anio": 2024,
                "precio": "25000.00",
            },
        )

        self.assertRedirects(response, "/")
        auto = Auto.objects.get()
        self.assertEqual(auto.marca, "Toyota")
        self.assertEqual(auto.modelo, "Corolla")
        self.assertEqual(auto.anio, 2024)
        self.assertContains(self.client.get("/"), "Corolla")
