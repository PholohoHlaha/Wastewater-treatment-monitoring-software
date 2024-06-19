import unittest
from unittest.mock import patch, MagicMock
from producer import (
    generate_turbidity, generate_tss, generate_ph, generate_bod,
    generate_Coliforms, generate_average_inflow, generate_total_grid
)

class TestKafkaProducer(unittest.TestCase):

    @patch('producer.KafkaProducer')
    @patch('producer.Faker')
    def test_producer(self, MockFaker, MockKafkaProducer):

        mock_faker = MockFaker.return_value
        mock_faker.random_int.side_effect = [0, 0]  # For turbidity and TSS
        mock_faker.pyfloat.side_effect = [7.5, 5.5, 90.5, 9500.75, 50.25]


        mock_producer = MockKafkaProducer.return_value
        mock_producer.send.return_value = MagicMock()


        turbidity = generate_turbidity()
        tss = generate_tss()
        ph = generate_ph()
        bod = generate_bod()
        coliforms = generate_Coliforms()
        average_inflow = generate_average_inflow()
        total_grid = generate_total_grid()


        self.assertEqual(turbidity, '{"Turbidity": 0}')
        self.assertEqual(tss, '{"TSS": 0}')
        self.assertEqual(ph, '{"pH": 7.5}')
        self.assertEqual(bod, '{"BOD": 5.5}')
        self.assertEqual(coliforms, '{"Corliforms": 90.5}')
        self.assertEqual(average_inflow, '{"Average_inflow": 9500.75}')
        self.assertEqual(total_grid, '{"Total_grid": 50.25}')


        mock_producer.send('tertiary_parameter', turbidity.encode("utf-8"))
        mock_producer.send('tertiary_parameter', tss.encode("utf-8"))
        mock_producer.send('tertiary_parameter', ph.encode("utf-8"))
        mock_producer.send('tertiary_parameter', bod.encode("utf-8"))
        mock_producer.send('tertiary_parameter', coliforms.encode("utf-8"))
        mock_producer.send('tertiary_parameter', average_inflow.encode("utf-8"))
        mock_producer.send('tertiary_parameter', total_grid.encode("utf-8"))


        self.assertEqual(mock_producer.send.call_count, 7)
        mock_producer.send.assert_any_call('tertiary_parameter', turbidity.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', tss.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', ph.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', bod.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', coliforms.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', average_inflow.encode("utf-8"))
        mock_producer.send.assert_any_call('tertiary_parameter', total_grid.encode("utf-8"))

if __name__ == '__main__':
    unittest.main()

