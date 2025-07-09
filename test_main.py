import unittest
from unittest.mock import patch, MagicMock
import main

class TestStartMessage(unittest.TestCase):

    @patch("main.bot.send_message")
    def test_start_message(self, mock_send_message):
        message = MagicMock()
        message.chat.id = 1345
        message.text = "/start"

        main.start(message)

        mock_send_message.assert_called_once_with(1345, "Hello! In this bot, you can see Club World Cup statistics of all time.\n First of all, you should register.")