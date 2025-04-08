import os
import re
import glob
import datetime
import random
import sys

def replace_image_line(directory, url_template, line_number):
	markdown_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')])
	image_pattern = re.compile(r'image: https?://[^\s]+')
	available_numbers = list(range(1, 771))
	used_numbers = []
	if not url_template:
		url_template = "https://banmaixanh.vercel.app/image/cover/001-{number}.jpg"
	for i, file_name in enumerate(markdown_files):
		file_path = os.path.join(directory, file_name)
		with open(file_path, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		if len(lines) > line_number:
			if available_numbers:
				if i < 770:
					number = available_numbers.pop(0)
					used_numbers.append(number)
				else:
					number = random.choice(used_numbers)
			else:
				number = random.choice(used_numbers)
			formatted_number = f"{number:03d}"
			new_image_url = url_template.format(number=formatted_number)
			lines[line_number] = f"image: {new_image_url}\n"
			with open(file_path, 'w', encoding='utf-8') as file:
				file.writelines(lines)
			print(f"Đã xử lý tệp: {file_name} - Số ảnh: {formatted_number}.")

def update_pubDatetime(file_path, new_datetime, line_number):
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		if len(lines) > line_number:
			lines[line_number] = f"pubDatetime: {new_datetime}\n"
			with open(file_path, 'w', encoding='utf-8') as file:
				file.writelines(lines)
			return True
		return False
	except Exception as e:
		print(f"Lỗi khi cập nhật pubDatetime trong tệp {file_path}: {str(e)}.")
		return False

def get_next_valid_date(current_date):
	next_date = current_date - datetime.timedelta(days=1)
	day = next_date.day
	month = next_date.month
	if day == 31:
		next_date -= datetime.timedelta(days=1)
	if month == 2 and day >= 29:
		next_date -= datetime.timedelta(days=day - 28)
	return next_date

def generate_valid_dates(start_date, count):
	dates = []
	current_date = start_date
	for _ in range(count):
		current_date = get_next_valid_date(current_date)
		dates.append(current_date)
	return dates

def process_markdown_files(directory, start_date, line_number):
	markdown_files = glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)
	if not markdown_files:
		print(f"Không tìm thấy tệp markdown nào trong {directory}.")
		return 0
	dates = generate_valid_dates(start_date, len(markdown_files))
	random.shuffle(markdown_files)
	count = 0
	for i, file_path in enumerate(markdown_files):
		new_datetime = dates[i].strftime('%Y-%m-%dT10:10:00Z')
		if update_pubDatetime(file_path, new_datetime, line_number):
			print(f"Đã cập nhật {file_path} với pubDatetime: {new_datetime}.")
			count += 1
	return count

if __name__ == "__main__":
	random.seed(datetime.datetime.now().timestamp())
	args = sys.argv[1:]
	if len(args) < 3:
		print("Usage: python markdown_processor.py <feature> <directory> <line_number> [custom_input]")
		sys.exit(1)
	
	feature, directory, line_number = args[0], args[1], int(args[2]) - 1
	custom_input = args[3] if len(args) > 3 else None

	if feature == "1":
		replace_image_line(directory, custom_input, line_number)
		print("Hoàn thành thay đổi hình ảnh!.")
	elif feature == "2":
		start_date = datetime.datetime.strptime(custom_input, '%Y-%m-%d') if custom_input else datetime.datetime.now()
		count = process_markdown_files(directory, start_date, line_number)
		print(f"Hoàn thành! Đã cập nhật {count}/{len(glob.glob(os.path.join(directory, '**', '*.md'), recursive=True))} tệp.")
	else:
		print("Tính năng không hợp lệ.")
		sys.exit(1)