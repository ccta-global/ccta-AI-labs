import importlib
import os
import unittest
from unittest.mock import patch


class TestGroqChatbot(unittest.TestCase):
    def test_prompt_constants_are_valid(self):
        import prompt

        self.assertTrue(prompt.SYSTEM_PROMPT.strip().startswith("You are a helpful assistant"))
        self.assertTrue(prompt.SYSTEM_PROMPT_2.strip().startswith("You are a helpful assistant"))
        self.assertTrue(prompt.SYSTEM_PROMPT_3.strip().startswith("You are a helpful assistant"))

    def test_client_uses_groq_api_key_from_environment(self):
        with patch.dict(os.environ, {"GROQ_API_KEY": "test-api-key"}, clear=False):
            import client as client_module
            importlib.reload(client_module)
            self.assertEqual(client_module.client.api_key, "test-api-key")


if __name__ == "__main__":
    unittest.main()
