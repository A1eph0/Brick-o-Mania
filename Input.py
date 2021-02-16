"""Defining input class."""
import sys
import termios
import tty
import signal

class Get:
    """Class to get input."""

    def caller (self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def alarmHandler(self, signum, frame):
        """Handling timeouts."""
        raise TimeoutError


    def input_to(self, timeout=0.1):
        """Taking input from user."""
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = self.caller()
            signal.alarm(0)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None



