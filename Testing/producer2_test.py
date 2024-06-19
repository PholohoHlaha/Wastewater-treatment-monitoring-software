import unittest
from unittest.mock import patch, MagicMock
from producer import (
    generate_do, generate_mlss, generate_MLVSS, generate_ammonia,
    generate_nitrate, generate_Phosphorus, generate_turbidity, generate_ORP
)

class TestKafkaProducer(unittest.TestCase):

    @patch('producer.KafkaProducer')
    @patch('producer.Faker')
    def test_producer(self, MockFaker, MockKafkaProducer):

        mock_faker = MockFaker.return_value
        mock_faker.random_int.side_effect = [4, 3000, 15, 18]
        mock_faker.pyfloat.side_effect = [3500.55, 3.25, 1.75, 5.65, 6.75]


        mock_producer = MockKafkaProducer.return_value
        mock_producer.send.return_value = MagicMock()


        do = generate_do()
        mlss = generate_mlss()
        mlvss = generate_MLVSS()
        ammonia = generate_ammonia()
        nitrate = generate_nitrate()
        phosphorus = generate_Phosphorus()
        turbidity = generate_turbidity()
        orp = generate_ORP()


        self.assertEqual(do, '{"DO": 4}')
        self.assertEqual(mlss, '{"MLSS": 3000}')
        self.assertEqual(mlvss, '{"MLVSS": 3500.55}')
        self.assertEqual(ammonia, '{"ammonia": 3.25}')
        self.assertEqual(nitrate, '{"nitrate": 1.75}')
        self.assertEqual(phosphorus, '{"Phosphorus": 5.65}')
        self.assertEqual(turbidity, '{"turbidity": 18}')
        self.assertEqual(orp, '{"ORP": 6.75}')


        mock_producer.send('secondary_parameter', do.encode("utf-8"))
        mock_producer.send('secondary_parameter', mlss.encode("utf-8"))
        mock_producer.send('secondary_parameter', mlvss.encode("utf-8"))
        mock_producer.send('secondary_parameter', ammonia.encode("utf-8"))
        mock_producer.send('secondary_parameter', nitrate.encode("utf-8"))
        mock_producer.send('secondary_parameter', phosphorus.encode("utf-8"))
        mock_producer.send('secondary_parameter', turbidity.encode("utf-8"))
        mock_producer.send('secondary_parameter', orp.encode("utf-8"))


        self.assertEqual(mock_producer.send.call_count, 8)
        mock_producer.send.assert_any_call('secondary_parameter', do.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', mlss.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', mlvss.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', ammonia.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', nitrate.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', phosphorus.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', turbidity.encode("utf-8"))
        mock_producer.send.assert_any_call('secondary_parameter', orp.encode("utf-8"))

if __name__ == '__main__':
    unittest.main()

