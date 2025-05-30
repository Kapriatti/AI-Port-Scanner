import math

def extract_features_for_port(port, service_name):
    """
    Extracts 10 features for a given port and service.
    """
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    service_keywords = {
        "ftp": 1,
        "ssh": 2,
        "telnet": 3,
        "smtp": 4,
        "dns": 5,
        "http": 6,
        "pop3": 7,
        "imap": 8,
        "https": 9,
        "smb": 10,
        "rdp": 11
    }

    # Basic numeric features
    features = [
        port,
        int(port in common_ports),                          # Is common port
        int(service_name.lower() in service_keywords),      # Known service name
        service_keywords.get(service_name.lower(), 0),      # Encoded service
        int(port % 2 == 0),                                 # Even port number
        math.log(port + 1),                                 # Log of port
        int(port < 1024),                                   # Well-known port range
        int(1024 <= port <= 49151),                         # Registered port range
        int(port > 49151),                                  # Dynamic/private port
        sum(c.isdigit() for c in service_name)              # Digits in service name
    ]

    return features
