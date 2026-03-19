from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / 'email_automation' / '.env')


def secrets(request):
    
    return {"gtag": env.get_value('GOOGLE_ANALYTICS', default='')}