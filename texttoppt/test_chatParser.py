import unittest
from chatParser import WhatsAppChatParser


class TestWhatsAppChatParser(unittest.TestCase):
    def test_ignore_deleted_messages(self):
        test_data_file = "deletedLinesTestData.txt"
        expected_output_text = "Quote 2\n"

        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.SetMessageAuthor("Aashish")
        chatparser.ExtractQuoteList(test_data_file)
        first_quote = chatparser.getNextQuote()
        second_quote = chatparser.getNextQuote()
        actual_output = second_quote

        self.assertEqual(actual_output, expected_output_text)

    def test_multiline_is_supported(self):
        test_data_file = "multilineTestData.txt"
        expected_output_text = "Ignorance is bliss\n\n"
        expected_output_text += "Its so painful to be aware of negative effects of my own actions\n\n"
        expected_output_text += "Still falling victim of this uncontrolled mind\n"
        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.SetMessageAuthor("Aashish")
        chatparser.ExtractQuoteList(test_data_file)
        actual_output = chatparser.getNextQuote()

        self.assertEqual(actual_output, expected_output_text)
