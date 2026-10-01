from backend.config import settings, DATA_DIR, DATABASE_PATH

def test_settings_load():
    assert settings.app_name == "RiskPulse"
    assert settings.stress_test_threshold == 7

def test_directories_exist():
    assert DATA_DIR.exists(), f"DATA_DIR {DATA_DIR} does not exist"
    assert DATABASE_PATH.parent.exists(), f"Database directory {DATABASE_PATH.parent} does not exist"
