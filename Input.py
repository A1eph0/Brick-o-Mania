from Parameters import *

"""Defining input class."""
import sys, os, termios, tty, signal

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


    def input_to(self, timeout=1/FPS+0.15):
        """Taking input from user."""
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = self.caller()
            if text == '\x03':
                os.system("stty echo")
                os._exit(0)
            signal.alarm(0)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None



