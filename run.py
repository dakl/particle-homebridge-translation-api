import logging

from app.setup import app
from app.views import *

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting particle-homebridge-translation-api")
    app.run(debug=True)
