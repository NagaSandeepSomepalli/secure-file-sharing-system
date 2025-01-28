from itsdangerous import URLSafeSerializer

def generate_secure_url(file_id):
    s = URLSafeSerializer('your_secret_key')
    return s.dumps(file_id)

def validate_secure_url(token):
    s = URLSafeSerializer('your_secret_key')
    return s.loads(token)
