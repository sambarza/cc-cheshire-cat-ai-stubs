from _typeshed import Incomplete
from datetime import datetime

class WhiteRabbit:
    """The WhiteRabbit

    Here the cron magic happens

    """
    scheduler: Incomplete
    def __init__(self) -> None: ...
    def get_job(self, job_id: str) -> dict[str, str] | None:
        """
        Gets a scheduled job

        Parameters
        ----------
        job_id: str
            The id assigned to the job.

        Returns
        -------
        Dict[str, str] | None
            A dict with id, name and next_run if the job exists, otherwise None.
        """
    def get_jobs(self) -> list[dict[str, str]]:
        """
        Returns a list of scheduled jobs

        Returns
        -------
        List[Dict[str, str]]
            A list of jobs. Each job is a dict with id, name and next_run.
        """
    def pause_job(self, job_id: str) -> bool:
        """
        Pauses a scheduled job

        Parameters
        ----------
        job_id: str
            The id assigned to the job.

        Returns
        -------
        bool
            The outcome of the pause action.
        """
    def resume_job(self, job_id: str) -> bool:
        """
        Resumes a paused job

        Parameters
        ----------
        job_id: str
            The id assigned to the job.

        Returns
        -------
        bool
            The outcome of the resume action.
        """
    def remove_job(self, job_id: str) -> bool:
        """
        Removes a scheduled job

        Parameters
        ----------
        job_id: str
            The id assigned to the job.

        Returns
        -------
        bool
            The outcome of the removal.
        """
    def schedule_job(self, job, job_id: str = None, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0, **kwargs) -> str:
        """
        Schedule a job

        Parameters
        ----------
        job: function
            The function to be called.
        job_id: str
            The id assigned to the job.
        days: int
            Days to wait.
        hours: int
            Hours to wait.
        minutes: int
            Minutes to wait.
        seconds: int
            Seconds to wait.
        milliseconds: int
            Milliseconds to wait.
        microseconds: int
            Microseconds to wait.
        **kwargs
            The arguments to pass to the function.

        Returns
        -------
        str
            The job id.
        """
    def schedule_interval_job(self, job, job_id: str = None, start_date: datetime = None, end_date: datetime = None, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0, **kwargs) -> str:
        """
        Schedule an interval job

        Parameters
        ----------
        job: function
            The function to be called.
        job_id: str
            The id assigned to the job
        start_date: datetime
            Start date. If None the job can start instantaneously
        end_date: datetime
            End date. If None the job never ends.
        days: int
            Days to wait.
        hours: int
            Hours to wait.
        minutes: int
            Minutes to wait.
        seconds: int
            Seconds to wait.
        **kwargs
            The arguments to pass to the function

        Returns
        -------
        str
            The job id.
        """
    def schedule_cron_job(self, job, job_id: str = None, start_date: datetime = None, end_date: datetime = None, year: Incomplete | None = None, month: Incomplete | None = None, day: Incomplete | None = None, week: Incomplete | None = None, day_of_week: Incomplete | None = None, hour: Incomplete | None = None, minute: Incomplete | None = None, second: Incomplete | None = None, **kwargs) -> str:
        """
        Schedule a cron job

        Parameters
        ----------
        job: function
            The function to be called.
        job_id: str
            The id assigned to the job
        start_date: datetime
            Start date. If None the job can start instantaneously
        end_date: datetime
            End date. If None the job never ends.
        year: int|str
            4-digit year
        month: int|str
            month (1-12)
        day: int|str
            day of month (1-31)
        week: int|str
            ISO week (1-53)
        day_of_week: int|str
            number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour: int|str
            hour (0-23)
        minute: int|str
            minute (0-59)
        second: int|str
            second (0-59)
        **kwargs
            The arguments to pass to the function

        Returns
        -------
        str
            The job id.
        """
    def schedule_chat_message(self, content: str, cat, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> str:
        """
        Schedule a chat message

        Parameters
        ----------
        content: str
            The message to be sent.
        cat: StrayCat
            Stray Cat instance.
        days: int
            Days to wait.
        hours: int
            Hours to wait.
        minutes: int
            Minutes to wait.
        seconds: int
            Seconds to wait.
        milliseconds: int
            Milliseconds to wait.
        microseconds: int
            Microseconds to wait.

        Returns
        -------
        str
            The job id.
        """
