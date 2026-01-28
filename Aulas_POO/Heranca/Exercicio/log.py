from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError("implemente o método log")
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}"  )
    
    def log_success(self, msg):
        return self._log(f"Success: {msg}"  )


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print("salvando no log", msg)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)

if __name__ == '__main__':
    lg = LogPrintMixin()
    lg.log_error("qualquer coisa")
    lg.log_success("qualquer coisa")

    lf = LogFileMixin()
    lf.log_error("quaquer coisa")
    lf.log_success("qualquer coisa")

