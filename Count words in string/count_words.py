with open('README') as my_work_file:
    text = my_work_file.read()

    def count_words(text):
        return f'Text from README file contains {len(list(text.split()))} words.'

with open('REPORT', mode='w+') as my_work_report:
    my_work_report.write(f'This report is generated automatically \n{count_words(text)}')
