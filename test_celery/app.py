# coding: utf-8

# $Id: $
from celery import Celery
from celery.utils.log import get_task_logger, get_logger

CELERY_CONFIG = {
    'BROKER_URL': 'amqp://guest@localhost/',
    'CELERY_RESULT_BACKEND': "redis://localhost/0",
    'CELERY_TASK_SERIALIZER': "pickle",
    'CELERY_RESULT_SERIALIZER': "pickle",
    'CELERYD_LOG_FORMAT': '[%(asctime)s] %(levelname)s: %(message)s',
    'CELERYD_TASK_LOG_FORMAT': '[%(asctime)s] %(levelname)s <%(sid)s> %(task_name)s: %(message)s',
}


from logcollect.boot import celery_config

celery_config('amqp://guest:guest@127.0.0.1/',
              collect_root_logs=True,
              activity_identity={'project': 'logcollect',
                                 'subsystem': 'celery_test'})


celery = Celery(CELERY_CONFIG)


@celery.task
def sample_task(msg='CELERY'):
    get_task_logger("sample_task").info("get task logger message")
    get_logger("celery_sample_logger").info("get logger message")
