import joblib

def load_model(model_path):
    """
    Carrega o modelo de previsão a partir de um arquivo pickle.
    """
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None


def load_preprocessor(path):
    """
    Carrega o modelo de previsão a partir de um arquivo pickle.
    """
    try:
        preprocessor = joblib.load(path)
        return preprocessor
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None