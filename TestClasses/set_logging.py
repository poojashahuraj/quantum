import logging
import logging.config

log_levels = {0:"NO_SET", "DEBUG":10, "INFO":20, "WARN":30, "ERROR":40, "CRITICAL":50}
ERROR_FORMAT = "%(asctime)s %(levelname)s in %(filename)s %(funcName)s %(lineno)d : %(message)s: %(message)s"
DEBUG_FORMAT = " %(asctime)s %(levelname)s in %(filename)s %(lineno)d : %(message)s"
LOG_CONFIG = {'version':1,
              'formatters':{'error':{'format':ERROR_FORMAT},
                            'debug':{'format':DEBUG_FORMAT}},
              'handlers':{'console':{'class':'logging.StreamHandler',
                                     'formatter':'debug',
                                     'level':logging.DEBUG},
                          'file':{'class':'logging.FileHandler',
                                  'filename':'../ftpput.log',
                                  'formatter':'error',
                                  'level':logging.ERROR}},
              'root':{'handlers':('console', 'file'), 'level':'DEBUG'}}
logging.config.dictConfig(LOG_CONFIG)

