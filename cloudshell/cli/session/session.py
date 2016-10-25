from collections import OrderedDict

from abc import ABCMeta, abstractmethod


class Session(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self, prompt, logger):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def _send(self, command, logger):
        pass

    @abstractmethod
    def send_line(self, command, logger):
        pass

    @abstractmethod
    def _receive(self, timeout, logger):
        pass

    @abstractmethod
    def hardware_expect(self, command, expected_string, logger, action_map=OrderedDict(), error_map=OrderedDict(),
                        timeout=None, retries=None, check_action_loop_detector=True, empty_loop_timeout=None,
                        **optional_args):
        pass

    @abstractmethod
    def reconnect(self, prompt, logger):
        pass

    @abstractmethod
    def _default_actions(self, logger):
        pass
