class EmailReporter(object):
    def __init__(self,report_generator,report_formatter,email_sender):
        self.report_generator= report_generator
        self.report_formatter= report_formatter
        self.email_sender= email_sender

    def send_email(self,start_time,end_time):
        # report=self.report_generator.generate_report(start_time,end_time)
        body=self.report_formatter.format_report()
        print(body)


from abc import  ABC,abstractmethod

class ReportFormatter(ABC):
    @abstractmethod
    def format_report(self):
        pass

class CSVFormatter(ReportFormatter):

    def format_report(self):
        return "CSV report formatted"

class HTMLFormatter(ReportFormatter):

    def format_report(self):
        return "HTML report formatted"
class ReportGenerator:
    pass

class EmailSender:
    pass

csv_fomatter=EmailReporter(ReportGenerator(),CSVFormatter(),EmailSender())
csv_fomatter.send_email(1,2)
html_fomatter=EmailReporter(ReportGenerator(),HTMLFormatter(),EmailSender())
html_fomatter.send_email(1,2)

