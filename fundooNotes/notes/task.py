from celery import shared_task


@shared_task(bind=True)
def test(self):
    print("rabit")
    return "Done"