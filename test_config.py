from config import LLM_CONFIGURATION as config


class TestConfig:
    def test_model(self):
        assert "gpt-3.5-turbo" == config["model"]["model_name"]

    def test_content(self):
        assert "You are a machine learning expert." == config["model"]["system_role"]["content"]
