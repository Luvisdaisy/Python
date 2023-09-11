import PyPDF2


def split_pdf(input_pdf, output_folder):
    # 读取输入的PDF文件
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        # 遍历PDF文件的每一页
        for page_num in range(reader.numPages):
            # 提取当前页
            page = reader.getPage(page_num)

            # 创建一个新的PDF文件
            output_pdf = f"{output_folder}/page_{page_num + 1}.pdf"
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(page)

            # 将新页面添加到输出文件中
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)


# 调用函数，传入输入PDF文件路径和输出文件夹路径
split_pdf("./材料.pdf",
          "./")
