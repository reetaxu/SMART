import xlrd, xlwt, openpyxl, os
from docx import Document
from modals.report_test_result import result_report
from common import settings
from docx.shared import Inches
from bs4 import BeautifulSoup


def get_report_module(report_name):
    for i in get_reports_by(IP_or_OP='IP'):
        module = 'Unknown'
        if report_name in i.report_name:
            module = i.report_module
            break
        else:
            pass

    return module


def get_log(report_name):
    str_ = 'get_log: ' + report_name
    save_log(str_)

    if 'CC/MCC' in report_name:
        report_name = 'Top 50 CC_MCC Diagnoses'

    log_path = '../../auto_results/logs/' + report_name + '.txt'
    f = open(log_path, 'r')
    lines = f.readlines()
    steps_ = ''
    for i in lines:
        steps_ = steps_ + i + '\n'
    return steps_


def get_logs():
    log_path = '../auto_results/logs/log.txt'
    log_path_target = '../auto_results/logs/'
    f = open(log_path, 'r')

    lines = f.readlines()
    steps_ = {}
    steps = []
    j = 0
    for i in lines:
        steps.append(i)
        if 'report_separator' in i:
            report_name = i.strip()[17:].rstrip('#')
            if 'CC/MCC' in report_name:
                report_name = 'Top 50 CC_MCC Diagnoses'
            j += 1
            print(j)
            print(report_name)
        if 'close browser' in i:
            f_report = open(log_path_target + report_name + '.txt', 'w')
            f_report.writelines(steps)
            f_report.close()
            steps_[report_name] = steps
            steps.clear()
    return steps_


def save_log(str_):

    print(str_)
    log_path = '../../auto_results/logs/log.txt'
    f = open(log_path, 'a')
    f.write(str_ + '\n')
    f.close()


def save_reports_screenshot_as_html(result_report):
    str_='save_reports_screenshot_as_html: ' + result_report.report_name
    save_log(str_)

    file_path_target = '../../auto_results/test_results/Test Results Screenshots.html'
    Fobj = open(file_path_target)
    Data = Fobj.read()
    Fobj.close()
    soup_elements = BeautifulSoup(Data, features="lxml")

    # get container_div
    container_div = soup_elements.select_one('#container')

    # create img div
    attrs_div = {'class': result_report.report_test_result}
    screenshot_div = soup_elements.new_tag('div', attrs=attrs_div)

    # create img title
    screenshot_title_p = soup_elements.new_tag('p')
    screenshot_title_p.string = result_report.report_name

    screenshot_msg_p = soup_elements.new_tag('p')
    screenshot_msg_p.string = result_report.msg

    steps_btn_attri = {
        'class': 'steps'
    }
    screenshot_steps_btn = soup_elements.new_tag('button', attrs=steps_btn_attri)
    screenshot_steps_btn.string = 'Steps'
    steps_attri = {
        'style': 'display:none',
    }
    screenshot_steps_p = soup_elements.new_tag('p', attrs=steps_attri)
    screenshot_steps_p.string = result_report.steps

    # create img tag
    attrs = {'class': result_report.report_test_result,
             'id': result_report.report_name,
             'alt': result_report.report_name,
             'src': '../../auto_results/screenshots/' + result_report.screen_shot}
    screenshot_img = soup_elements.new_tag('img', attrs=attrs)

    # insert into container
    screenshot_div.insert(new_child=screenshot_img, position=4)
    screenshot_div.insert(new_child=screenshot_steps_p, position=3)
    screenshot_div.insert(new_child=screenshot_steps_btn, position=2)
    screenshot_div.insert(new_child=screenshot_msg_p, position=1)
    screenshot_div.insert(new_child=screenshot_title_p, position=0)

    container_div.insert(new_child=screenshot_div, position=0)

    # save file
    file = open(file_path_target, 'w')
    file.write(str(soup_elements))
    file.close()


def save_html_resource(page_resourece, report):
    str_ = 'save_html_resource: ' + report
    save_log(str_)
    file_path = '../../auto_results/report_view_html_resources/' + report + '.html'
    print(file_path)
    f = open(file_path, 'w')
    f.write(page_resourece)
    f.close()


def clear_previous_auto_result():
    pass


def get_reports_by(IP_or_OP):
    str_ = 'get_reports_by: ' + IP_or_OP
    save_log(str_)
    f = '../../resources/Legacy & Enhanced Report.xlsx'
    book = xlrd.open_workbook(f)  # 打开一个excel
    sheet_ip = book.sheet_by_name(IP_or_OP)
    nrow = sheet_ip.nrows

    reports = []

    for i in range(1, nrow):
        report_module = sheet_ip.cell(i, 0).value.strip()
        report_name = sheet_ip.cell(i, 1).value.strip()
        report_name_saved_search = sheet_ip.cell(i, 2).value.strip()

        result = result_report(
            report_module=report_module,
            report_name=report_name,
            report_name_saved_search=report_name_saved_search,
        )
        reports.append(result)

    return reports


def write_test_result_report_word(result_report):
    str_ = 'write_test_result_report_word: ' + result_report.report_name
    save_log(str_)

    image_path = '../../auto_results/screenshots/' + result_report.report_name + '.png'

    if os.path.exists('../../auto_results/test_results/' + settings.test_result_file_name):
        document = Document('../../auto_results/test_results/' + settings.test_result_file_name)
    else:
        document = Document()
    document.add_heading(result_report.report_name + ':' + result_report.report_test_result, level=1)
    document.add_paragraph(text='Test Result: ' + result_report.msg)
    document.add_picture(image_path, width=Inches(6.43))
    document.save('../../auto_results/test_results/' + settings.test_result_file_name)


def write_test_result_report_excel(result_report):
    str_ = 'write_test_result_report_excel: ' + result_report.report_name
    save_log(str_)

    test_result_report_path = '../../auto_results/test_results/legacy reports auto test result.xlsx'
    path_screen_shot_path = r'C:\Users\yyang212\PycharmProjects\SMART_Auto\auto_results\screenshots\\' + result_report.screen_shot
    wb = openpyxl.load_workbook(test_result_report_path)
    ip_sheet = wb['IP']

    # insert test result
    ip_sheet.append([
        result_report.report_module,
        result_report.report_name,
        result_report.report_name_saved_search,
        result_report.report_test_result,
    ])

    # screenshot 设置超链接
    row_max = ip_sheet.max_row  # 获取最后一行
    ip_sheet.cell(row=row_max, column=5).hyperlink = path_screen_shot_path
    ip_sheet.cell(row=row_max, column=5).style = 'Hyperlink'
    ip_sheet.cell(row=row_max, column=5).value = result_report.screen_shot

    ip_sheet.cell(row=row_max, column=6).value = result_report.msg

    try:
        wb.save(test_result_report_path)
    except Exception as e:
        print('------write_test_result_report failed-------')
        print(e)


def write_test_result_com():
    test_result_report = result_report()

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    sheet = book.add_sheet('IP', cell_overwrite_ok=True)

    book.save('../legacy reports.xlsx')
