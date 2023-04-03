import logging.handlers

import config


class GetLogging:
    logger = None

    @classmethod
    def get_logger(cls):
        # 确保日志被多次调用是，使用的是一个日志器
        if cls.logger is None:
            # 1.获取日志器
            cls.logger = logging.getLogger()
            # 2.设置日志级别
            cls.logger.setLevel(logging.INFO)
            # 3.获取《控制台》处理器
            sh = logging.StreamHandler()
            # 4.获取本地项目路径
            file_path = config.file_path("log") + "page_all.log"
            # 5.获取《文件》处理器，文件以时间切割
            th = logging.handlers.TimedRotatingFileHandler(file_path,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 6.设置日志格式
            format = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s | %(funcName)s:%(lineno)d] - %(message)s'
            # 7.把格式添加到格式器
            fm = logging.Formatter(format)
            # 8.将格式器添加到处理器 --> 控制台
            sh.setFormatter(fm)
            # 9.将格式器添加到处理器 --> log文件
            th.setFormatter(fm)
            # 10.获取处理器，添加日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        # 11.返回日志器
        return cls.logger
