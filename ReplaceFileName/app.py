# Đọc file HTML mẫu
html_template = """
<div class="col-6 col-md-6 col-lg-4" data-aos="fade-up">
    <a href="../images/Lalen/DSC_0.jpg" class="d-block photo-item" data-fancybox="gallery">
      <img src="../images/Lalen/DSC_0.jpg" alt="Image" class="img-fluid">
      <div class="photo-text-more">
        <span class="icon icon-search"><br>DSC_0</span>
      </div>
    </a>
    <a class="download" href="../images/LaLen/DSC_0.jpg" download><span class="icon-download"></span></a>
</div>
"""

# Đọc file danhsach.txt
file_path = "D:\project\PhotoGallery\ReplaceFileName\input\danhsach.txt"
with open(file_path, 'r') as file:
    filenames = file.read().splitlines()

# Tạo chuỗi HTML thay thế cho từng tên file
result_html = ""
for filename in filenames:
    # Thay thế DSC_0 bằng tên file hiện tại
    html_content = html_template.replace("DSC_0", filename.split('.')[0])
    html_content = html_content.replace("DSC_0.jpg", filename)
    
    # Thêm vào kết quả cuối
    result_html += html_content + "\n\n"

# Ghi kết quả ra file mới
output_file = "D:\project\PhotoGallery\ReplaceFileName\output\output.html"
with open(output_file, 'w') as file:
    file.write(result_html)

print(f"File HTML đã được tạo tại {output_file}")
