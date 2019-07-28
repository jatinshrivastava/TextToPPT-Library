import unittest
from chatParser import WhatsAppChatParser


class TestWhatsAppChatParser(unittest.TestCase):
    def test_ignore_deleted_messages(self):
        test_data_file = "deletedLinesTestData.txt"
        expected_output_text = "Quote 3"

        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.SetMessageAuthor("Aashish")
        chatparser.ExtractQuoteList(test_data_file)
        first_quote = chatparser.getNextQuote()
        second_quote = chatparser.getNextQuote()
        Third_quote = chatparser.getNextQuote()
        actual_output = Third_quote

        self.assertEqual(actual_output, expected_output_text)

    def test_multiline_is_supported(self):
        test_data_file = "multilineTestData.txt"
        expected_output_text = "Ignorance is bliss\n"
        expected_output_text += "Its so painful to be aware of negative effects of my own actions\n"
        expected_output_text += "Still falling victim of this uncontrolled mind"
        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.SetMessageAuthor("Aashish")
        chatparser.ExtractQuoteList(test_data_file)
        actual_output = chatparser.getNextQuote()

        self.assertEqual(actual_output, expected_output_text)

    def test_messages_on_or_after_a_date(self):
    	test_data_file = "dateFilterTestData.txt"
    	message1 = "Quote 3"
    	message2 = "Quote 4"
    	message3 = "Quote 5"
    	chatparser = WhatsAppChatParser(test_data_file)
    	chatparser.SetMessageAuthor("All")
    	chatparser.SetStartDate("15/11/19")
    	chatparser.ExtractQuoteList(test_data_file)
    	self.assertEqual(chatparser.getNextQuote(), message1)
    	self.assertEqual(chatparser.getNextQuote(), message2)
    	self.assertEqual(chatparser.getNextQuote(), message3)

    def test_messages_on_or_before_a_date(self):
    	test_data_file = "dateFilterTestData.txt"
    	message1 = "Quote 1"
    	message2 = "Quote 2"
    	message3 = "Quote 3"
    	chatparser = WhatsAppChatParser(test_data_file)
    	chatparser.SetMessageAuthor("All")
    	chatparser.SetEndDate("15/11/19")
    	chatparser.ExtractQuoteList(test_data_file)
    	self.assertEqual(chatparser.getNextQuote(), message1)
    	self.assertEqual(chatparser.getNextQuote(), message2)
    	self.assertEqual(chatparser.getNextQuote(), message3)

    def test_emoji(self):
        test_data_file = "emojiTestData.txt"
        message1 = "Quote 11"
        message2 = "Quote 12"
        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.ExtractQuoteList(test_data_file)
        self.assertEqual(chatparser.getNextQuote(), message1)
        self.assertEqual(chatparser.getNextQuote(), message2)

    def test_capability_to_process_two_digits_date(self):
        pass

    def test_capability_to_process_android_dateformat(self):
        test_data_file = "androidDateTestData.txt"
        message1 = "Quote 1"
        message2 = "Quote 3"
        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.ExtractQuoteList(test_data_file)
        self.assertEqual(chatparser.getNextQuote(), message1)
        self.assertEqual(chatparser.getNextQuote(), message2)

    def test_capability_to_process_ios_dateformat(self):
        test_data_file = "iosDateTestData.txt"
        message1 = "Quote 1"
        message2 = "Quote 3"
        chatparser = WhatsAppChatParser(test_data_file)
        chatparser.ExtractQuoteList(test_data_file)
        self.assertEqual(chatparser.getNextQuote(), message1)
        self.assertEqual(chatparser.getNextQuote(), message2)
