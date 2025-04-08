# Markdown attribute modifier (MAM)

(Original Vietnamese below)
 
_Markdown attribute modifier (MAM) is a Python tool designed to automate the modification of date (`pubDatetime`) and cover image (`image`) attributes in Markdown files. It streamlines content updates by processing multiple files efficiently, supporting custom inputs for directories, line numbers, and URLs, with sensible defaults for ease of use. Ideal for bloggers and content managers._

## Installation Guide

To install, run the following command in your terminal:

```
npm i markdown-attribute
```

## Purpose

– Updates publication dates in Markdown files to reflect the latest information.

– Changes cover images in Markdown files with customizable or default URLs.

## Workflow

– Select feature: Input `1` to modify cover images, `2` to update dates, or `0` to exit. No default value; users must choose explicitly to proceed with the desired action.

– Specify directory: Enter the path to the folder containing Markdown files or leave blank to use the current directory (`.`). Defaults to the current directory for convenience.

– Set line number: Input the line number (starting from 1) to modify, or leave blank for default (line 5 for images, line 2 for dates). Simplifies targeting attributes.

– Provide optional input: For images, enter a URL template or use the default (`https://banmaixanh.vercel.app/image/cover/001-{number}.jpg`). For dates, input a date (`YYYY-MM-DD`) or use today’s date.

– Process and complete: The tool processes all Markdown files in the specified directory and displays the number of updated files (_Updated X/Y files_).

## Contact & support

– Email: info@nhavantuonglai.com.

– Website: nhavantuonglai.com.

If you have any questions or suggestions, don't hesitate to contact us for the quickest support.

Don't forget to star this repository if you find it useful.

# Công cụ sửa thuộc tính markdown (MAM)

_Công cụ sửa thuộc tính markdown (MAM) là một tiện ích Python tự động hóa việc thay đổi thuộc tính ngày tháng (`pubDatetime`) và ảnh bìa (`image`) trong tệp Markdown. Nó giúp cập nhật nội dung nhanh chóng, hỗ trợ tùy chỉnh thư mục, số dòng và URL, với các giá trị mặc định tiện lợi. Phù hợp cho blogger và quản lý nội dung._

## Hướng dẫn cách cài đặt

Để cài đặt, chạy lệnh sau trong terminal:

```
npm i markdown-attribute
```

## Công dụng

– Cập nhật ngày xuất bản trong tệp Markdown để phản ánh thông tin mới nhất.

– Thay đổi ảnh bìa trong tệp Markdown với URL tùy chỉnh hoặc mặc định.

## Flow thao tác

– Chọn tính năng: Nhập `1` để thay đổi ảnh bìa, `2` để cập nhật ngày tháng, hoặc `0` để thoát. Không có giá trị mặc định; người dùng phải chọn rõ ràng để tiếp tục với hành động mong muốn.

– Chỉ định thư mục: Nhập đường dẫn đến thư mục chứa tệp Markdown hoặc để trống để dùng thư mục hiện tại (`.`). Mặc định là thư mục hiện tại để thuận tiện cho người dùng.

– Chọn số dòng: Nhập số dòng (tính từ 1) cần thay đổi hoặc để trống để dùng mặc định (dòng 5 cho ảnh, dòng 2 cho ngày). Giúp dễ dàng định vị thuộc tính cần sửa.

– Cung cấp thông tin tùy chọn: Với ảnh, nhập URL mẫu hoặc dùng mặc định (`https://banmaixanh.vercel.app/image/cover/001-{number}.jpg`). Với ngày, nhập ngày (`YYYY-MM-DD`) hoặc dùng ngày hiện tại.

– Xử lý và hoàn tất: Công cụ xử lý tất cả tệp Markdown trong thư mục đã chọn và hiển thị số lượng tệp được cập nhật (Ví dụ: _Đã cập nhật X/Y tệp_).

## Liên hệ & hỗ trợ

– Email: info@nhavantuonglai.com.

– Website: nhavantuonglai.com.

Nếu bạn có bất kỳ câu hỏi hoặc đề xuất nào, đừng ngần ngại liên hệ với chúng tôi để được hỗ trợ nhanh nhất.

Đừng quên star repository này nếu bạn thấy nó hữu ích.