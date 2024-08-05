# app/utils/logger.py

import logging

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

app_logger.addHandler(handler)
