import unittest
from unittest.mock import patch, MagicMock
from producer import generate_ss, generate_bod, generate_ph, generate_temperature

class TestKafkaProducer(unittest.TestCase):
    
    @patch('producer.KafkaProducer')
    @patch('producer.Faker')
    def test_producer(self, MockFaker, MockKafkaProducer):

        mock_faker = MockFaker.return_value
        mock_faker.random_int.side_effect = [20, 5]
        mock_faker.pyfloat.side_effect = [7.5, 25.0]
        

        mock_producer = MockKafkaProducer.return_value
        mock_producer.send.return_value = MagicMock()
        

        ss = generate_ss()
        bod = generate_bod()
        ph = generate_ph()
        temperature = generate_temperature()
        

        self.assertEqual(ss, '{"SS": 20}')
        self.assertEqual(bod, '{"BOD": 5}')
        self.assertEqual(ph, '{"pH": 7.5}')
        self.assertEqual(temperature, '{"Temperature": 25.0}')
        

        mock_producer.send('primary_parameter', ss.encode("utf-8"))
        mock_producer.send('primary_parameter', bod.encode("utf-8"))
        mock_producer.send('primary_parameter', ph.encode("utf-8"))
        mock_producer.send('primary_parameter', temperature.encode("utf-8"))
        

        self.assertEqual(mock_producer.send.call_count, 4)
        mock_producer.send.assert_any_call('primary_parameter', ss.encode("utf-8"))
        mock_producer.send.assert_any_call('primary_parameter', bod.encode("utf-8"))
        mock_producer.send.assert_any_call('primary_parameter', ph.encode("utf-8"))
        mock_producer.send.assert_any_call('primary_parameter', temperature.encode("utf-8"))

if __name__ == '__main__':
    unittest.main()
